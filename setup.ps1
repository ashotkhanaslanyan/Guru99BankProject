# Define the virtual environment directory
$venvPath = ".\venv"

# Create a virtual environment
Write-Output "Creating virtual environment..."
python -m venv $venvPath

# Define paths to activation scripts
$activateBatPath = Join-Path $venvPath "Scripts\Activate.bat"
$activatePs1Path = Join-Path $venvPath "Scripts\Activate.ps1"

# Update Activate.bat to set PYTHONPATH
Write-Output "Updating Activate.bat to set PYTHONPATH..."
Add-Content -Path $activateBatPath -Value 'set PYTHONPATH=%~dp0;%PYTHONPATH%'

# Define the new line to add to Activate.ps1
$newLine = '$env:PYTHONPATH="$PSScriptRoot;$env:PYTHONPATH"'

# Read the content of Activate.ps1, insert the new line at the specified position, and write it back
$insertPosition = 247
Write-Output "Updating Activate.ps1 to set PYTHONPATH..."
$ps1Content = Get-Content -Path $activatePs1Path
$updatedContent = $ps1Content | ForEach-Object -Begin { $i = 0 } -Process {
    if ($i -eq $insertPosition) { 
        $newLine 
        $_ 
    } else { 
        $_ 
    } 
    $i++
}
$updatedContent | Set-Content -Path $activatePs1Path

# Activate the virtual environment
Write-Output "Activating the virtual environment..."
& $activatePs1Path

Write-Output "Setup complete. The virtual environment is now activated."
