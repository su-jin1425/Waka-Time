# PowerShell Code to find Mouse Point

```powershell
while ($true) {
  Add-Type -Namespace User32 -Name Cursor -MemberDefinition '[DllImport("user32.dll")] public static extern bool GetCursorPos(out POINT lpPoint); public struct POINT { public int X; public int Y; }' | Out-Null; 
  $pos = New-Object User32.Cursor+POINT; 
  [User32.Cursor]::GetCursorPos([ref]$pos); 
  Write-Host "`rX=$($pos.X), Y=$($pos.Y)" -NoNewline; 
  Start-Sleep -Milliseconds 100 
}
