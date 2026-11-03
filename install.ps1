Write-Host "=== Starting Application Installation ===" -ForegroundColor Cyan

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

Write-Host "[INSTALL] Installing VS Code extensions..."
Get-Content .\extensions.txt | ForEach-Object {
    Write-Host "[EXTENSION] Installing $_"
    code --install-extension $_
    Write-Host "[EXTENSION] Finished $_"
}

Write-Host "[INSTALL] Installing Python packages..."
pip install pillow
Write-Host "[DEBUG] Python package installation completed."

Write-Host "=== Installation Script Finished ===" -ForegroundColor Green
