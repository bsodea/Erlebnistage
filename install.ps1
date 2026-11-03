#Requires -Version 5.1
$ErrorActionPreference = "Stop"
============================================================
Configuration
============================================================
$LogFile = Join-Path $PSScriptRoot "install.log"
$ExtensionsFile = Join-Path $PSScriptRoot "extensions.txt"
$Packages = @(
    @{ Name = "Git" Id = "Git.Git" Test = "git" Args = @("--version") },
    @{ Name = "Visual Studio Code" Id = "Microsoft.VisualStudioCode" Test = "code" Args = @("--version") },
    @{ Name = "Python" Id = "Python.Python.3.14" Test = "python" Args = @("--version") },
    @{ Name = "Ghostscript" Id = "ArtifexSoftware.GhostScript" Test = "gswin64c" Args = @("--version") }
)
$Failed = @()
============================================================
Logging
============================================================
function Write-Log {
    param(
        [string]$Message,
        [string]$Level = "INFO"
    )
    $Timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    $Line = "[$Timestamp] [$Level] $Message"
    Write-Host $Line
    Add-Content -Path $LogFile -Value $Line
}
============================================================
Initialization
============================================================
Clear-Host
"Installation started: $(Get-Date)" | Set-Content -Path $LogFile
Write-Log "Starting system setup..."
============================================================
Check winget
============================================================
Write-Log "Checking winget availability..."
$Winget = Get-Command winget.exe -ErrorAction SilentlyContinue
if (-not $Winget) { throw "winget is not available. Install or update Microsoft App Installer first." }
Write-Log "winget is available."
============================================================
Install applications
============================================================
foreach ($Package in $Packages) {
    Write-Log "Checking $($Package.Name)..."
    $Installed = Get-Command $Package.Test -ErrorAction SilentlyContinue
    if ($Installed) {
        Write-Log "$($Package.Name) is already available. Skipping installation."
        continue
    }
    Write-Log "Installing $($Package.Name)..."
    $Success = $false
    for ($Attempt = 1; $Attempt -le 3; $Attempt++) {
        try {
            Write-Log "Attempt $Attempt of 3..."
            & winget.exe install `
                --id $Package.Id `
                --exact `
                --silent `
                --accept-package-agreements `
                --accept-source-agreements `
                --disable-interactivity
            if ($LASTEXITCODE -ne 0) {
                throw "winget exited with code $LASTEXITCODE"
            }
            $Success = $true
            Write-Log "$($Package.Name) installed successfully."
            break
        }
        catch {
            Write-Log "Installation failed: $_" "ERROR"
            if ($Attempt -lt 3) {
                Write-Log "Retrying in 10 seconds..."
                Start-Sleep -Seconds 10
            }
        }
    }
    if (-not $Success) {
        $Failed += $Package.Name
        Write-Log "Could not install $($Package.Name)." "ERROR"
    }
}
============================================================
Refresh PATH
============================================================
Write-Log "Refreshing environment variables..."
$MachinePath = [Environment]::GetEnvironmentVariable("Path", "Machine")
$UserPath = [Environment]::GetEnvironmentVariable("Path", "User")
$env:Path = "$MachinePath;$UserPath"
============================================================
Verify installations
============================================================
Write-Log "Verifying installations..."
foreach ($Package in $Packages) {
    $Command = Get-Command $Package.Test -ErrorAction SilentlyContinue
    if ($Command) {
        try {
            $Output = & $Command.Source @($Package.Args) 2>&1
            if ($LASTEXITCODE -ne 0) {
                throw "Executable returned exit code $LASTEXITCODE"
            }
            Write-Log "$($Package.Name): $($Output -join ' ')"
        }
        catch {
            Write-Log "$($Package.Name): verification failed. $_" "ERROR"
            if ($Package.Name -notin $Failed) {
                $Failed += $Package.Name
            }
        }
    }
    else {
        Write-Log "$($Package.Name): executable not found in PATH." "ERROR"
        if ($Package.Name -notin $Failed) {
            $Failed += $Package.Name
        }
    }
}
============================================================
Install VS Code extensions
============================================================
Write-Log "Installing VS Code extensions..."
$CodeCommand = Get-Command code -ErrorAction SilentlyContinue
if ($CodeCommand -and (Test-Path $ExtensionsFile)) {
    $Extensions = Get-Content $ExtensionsFile |
        ForEach-Object { $_.Trim() } |
        Where-Object { $_ -and -not $_.StartsWith("#") }
    foreach ($Extension in $Extensions) {
        Write-Log "Installing extension: $Extension"
        try {
            & $CodeCommand.Source --install-extension $Extension --force
            if ($LASTEXITCODE -ne 0) {
                throw "VS Code exited with code $LASTEXITCODE"
            }
            Write-Log "Successfully installed extension: $Extension"
        }
        catch {
            Write-Log "Failed to install extension: $Extension. $_" "ERROR"
            $Failed += "VS Code extension: $Extension"
        }
    }
}
else {
    Write-Log "VS Code or extensions.txt unavailable. Skipping extensions." "ERROR"
    $Failed += "VS Code extensions"
}
============================================================
Summary
============================================================
Write-Log "============================================================"
$UniqueFailed = @($Failed | Select-Object -Unique)
if ($UniqueFailed.Count -eq 0) {
    Write-Log "ALL INSTALLATIONS COMPLETED SUCCESSFULLY."
}
else {
    Write-Log "INSTALLATION COMPLETED WITH ERRORS:" "ERROR"
    foreach ($Item in $UniqueFailed) {
        Write-Log "- $Item" "ERROR"
    }
}
Write-Log "Log file: $LogFile"
Write-Log "Setup finished."
Write-Host ""
Read-Host "Press Enter to close"
