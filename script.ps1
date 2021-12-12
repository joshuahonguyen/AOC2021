echo "every year, change the key"
$year = 2021
[int] $id = Read-Host -Prompt "ID"

$savename = "$(($id*2)-1)$($id*2).txt"
$site = "https://adventofcode.com/$($year)/day/$($id)/input"
echo $savename

$session = New-Object Microsoft.PowerShell.Commands.WebRequestSession

$cookie = New-Object System.Net.Cookie 
$cookie.Name = "session"
$cookie.Value = "53616c7465645f5f509c590bc3409207a1bd4846aa9b51313138d9d7f73585c5178e33853bc1e7dadf988be2441da237"
$cookie.Domain = "adventofcode.com"

$session.Cookies.Add($cookie)
Invoke-WebRequest $site -WebSession $session -o $savename