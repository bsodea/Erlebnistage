Write-Host "=== Starting Application Installation ===" -ForegroundColor Cyan

# --
# APP INSTALLING
# --

Write-Host "[INSTALL] Git..."
winget install --id Git.Git -e
Write-Host "[INSTALL] Git completed."

Write-Host "[INSTALL] Visual Studio Code..."
winget install --id Microsoft.VisualStudioCode -e
Write-Host "[INSTALL] VS Code completed."

Write-Host "[INSTALL] Python 3.14..."
winget install --id Python.Python.3.14 -e
Write-Host "[INSTALL] Python completed."

Write-Host "[INSTALL] Ghostscript..."
winget install --id ArtifexSoftware.GhostScript -e
Write-Host "[INSTALL] Ghostscript completed."

# --
# PATH REFRESH
# --

Write-Host "[DEBUG] Refreshing PATH..."
$MachinePath = [Environment]::GetEnvironmentVariable("Path", "Machine")
$UserPath = [Environment]::GetEnvironmentVariable("Path", "User")
$env:Path = "$MachinePath;$UserPath"
Write-Host "[DEBUG] PATH refreshed."

Write-Host "[CHECK] Git version:"
git --version

Write-Host "[CHECK] Python version:"
python --version

Write-Host "[CHECK] VS Code version:"
code --version

Write-Host "[CHECK] Ghostscript version:"
gswin64c --version

# --
# PACKAGE INSTALLATION
# --

Write-Host "[INSTALL] Installing VS Code extensions..."
Get-Content .\extensions.txt | ForEach-Object {
    Write-Host "[EXTENSION] Installing $_"
    code --install-extension $_
    Write-Host "[EXTENSION] Finished $_"
}

Write-Host "[INSTALL] Installing Python packages..."
pip install pillow
Write-Host "[DEBUG] Python package installation completed."

# --
# GIT CLONING
# --

# Configuration
$RepoUrl = "https://github.com/bsodea/Erlebnistage.git"
$FolderName = "Erlebnistag"
$DesktopPath = [Environment]::GetFolderPath("Desktop")
$TargetPath = Join-Path $DesktopPath $FolderName

# Create destination folder
Write-Host "[DEBUG] Creating destination folder..."
New-Item -ItemType Directory -Path $TargetPath -Force | Out-Null

# Clone repository
Write-Host "[DEBUG] Cloning repository..."
git clone $RepoUrl $TargetPath

# Check clone result
if ($LASTEXITCODE -ne 0) {
    Write-Host "[ERROR] Git clone failed!"
    exit 1
}

# Remove Git metadata
Write-Host "[DEBUG] Removing Git metadata..."
Remove-Item -Path (Join-Path $TargetPath ".git") -Recurse -Force

# Done
Write-Host "[DEBUG] Repository cloned successfully."
Write-Host "[DEBUG] Git metadata removed."
Write-Host "[DEBUG] Final folder: $TargetPath"

Write-Host "=== Installation Script Finished ===" -ForegroundColor Green
