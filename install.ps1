# Install Apps
winget install --id Git.Git -e
winget install --id Microsoft.VisualStudioCode -e
winget install --id Python.Python.3.14 -e
winget install --id ArtifexSoftware.GhostScript -e

# Refresh Path
$MachinePath = [Environment]::GetEnvironmentVariable("Path", "Machine")
$UserPath = [Environment]::GetEnvironmentVariable("Path", "User")
$env:Path = "$MachinePath;$UserPath"

# Check install
git --version
python --vesion
code --version
gswin64c --version

# Install Code Extensions
Get-Content .\extensions.txt | ForEach-Object {
    code --install-extension $_
}

# Install python packages
pip install pillow
