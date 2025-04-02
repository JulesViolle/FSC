# Disable keyboard
try {
    $keyboard = Get-WmiObject Win32_PnPEntity | Where-Object { $_.Description -like "*keyboard*" }
    if ($keyboard) {
        $keyboard.PNPDeviceID | ForEach-Object {
            Disable-PnpDevice -InstanceId $_ -Confirm:$false
        }
    }
} catch {
    Write-Host "Keyboard not found or failed to disable."
}

# Disable mouse
try {
    $mouse = Get-WmiObject Win32_PnPEntity | Where-Object { $_.Description -like "*mouse*" }
    if ($mouse) {
        $mouse.PNPDeviceID | ForEach-Object {
            Disable-PnpDevice -InstanceId $_ -Confirm:$false
        }
    }
} catch {
    Write-Host "Mouse not found or failed to disable."
}

# Disable touchpad
try {
    $touchpad = Get-WmiObject Win32_PnPEntity | Where-Object { $_.Description -like "*touchpad*" -or $_.Description -like "*touch*" }
    if ($touchpad) {
        $touchpad.PNPDeviceID | ForEach-Object {
            Disable-PnpDevice -InstanceId $_ -Confirm:$false
        }
    }
} catch {
    Write-Host "Touchpad or touchscreen not found or failed to disable."
}
