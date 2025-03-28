# Disable keyboard
$keyboard = Get-WmiObject Win32_PnPEntity | Where-Object { $_.Description -like "*keyboard*" }
$keyboard.PNPDeviceID | ForEach-Object {
    Disable-PnpDevice -InstanceId $_ -Confirm:$false
}
# Disable mouse
$mouse = Get-WmiObject Win32_PnPEntity | Where-Object { $_.Description -like "*mouse*" }
$mouse.PNPDeviceID | ForEach-Object {
    Disable-PnpDevice -InstanceId $_ -Confirm:$false
}
# Disable touchscreen
$touchscreen = Get-WmiObject Win32_PnPEntity | Where-Object { $_.Description -like "*touch*" }
$touchscreen.PNPDeviceID | ForEach-Object {
    Disable-PnpDevice -InstanceId $_ -Confirm:$false
}
