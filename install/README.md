# Erlebnistage

## Install Skript funktioniert nicht?

Common reasons a PowerShell script won't run:

1. **Execution policy** — Run this first in an elevated PowerShell:
   ```powershell
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser -Force
   ```

2. **Not running as Administrator** — winget installs to machine scope by default. Right-click PowerShell → "Run as Administrator"

3. **Running from a UNC path or network drive** — Copy the script locally first

4. **$PSScriptRoot is empty** — Happens if you paste the code directly into the console instead of running the `.ps1` file. Save as a file and execute:
   ```powershell
   .\install-fixed.ps1
   ```

5. **Windows Defender / SmartScreen blocking** — Check if the file is blocked (right-click → Properties → "Unblock")
