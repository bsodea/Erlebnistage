# Install Apps
winget install --id Git.Git -e
winget install --id Microsoft.VisualStudioCode -e
winget install --id Python.Python.3.14 -e
winget install --id ArtifexSoftware.GhostScript -e

# Refresh Path
$MachinePath = [Environment]::GetEnvironmentVariable("Path", "Machine")
$UserPath = [Environment]::GetEnvironmentVariable("Path", "User")
$env:Path = "$MachinePath;$UserPath"

# Install Code Extensions
cat extensions.txt | xargs -L 1 code --install-extension
