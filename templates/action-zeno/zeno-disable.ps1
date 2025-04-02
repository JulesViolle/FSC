# Disable Keyboard
try {
    $keyboard = Get-WmiObject Win32_PnPEntity | Where-Object { $_.Description -like "*keyboard*" }
    if ($keyboard) {
        $keyboard.PNPDeviceID | ForEach-Object {
            Disable-PnpDevice -InstanceId $_ -Confirm:$false
        }
        Write-Host "Keyboard disabled."
    } else {
        Write-Host "No keyboard found to disable."
    }
} catch {
    Write-Host "Error occurred while disabling keyboard: $_"
}

# Disable Mouse
try {
    $mouse = Get-WmiObject Win32_PnPEntity | Where-Object { $_.Description -like "*mouse*" }
    if ($mouse) {
        $mouse.PNPDeviceID | ForEach-Object {
            Disable-PnpDevice -InstanceId $_ -Confirm:$false
        }
        Write-Host "Mouse disabled."
    } else {
        Write-Host "No mouse found to disable."
    }
} catch {
    Write-Host "Error occurred while disabling mouse: $_"
}

# Disable Touchscreen
try {
    $touchscreen = Get-WmiObject Win32_PnPEntity | Where-Object { $_.Description -like "*touch*" }
    if ($touchscreen) {
        $touchscreen.PNPDeviceID | ForEach-Object {
            Disable-PnpDevice -InstanceId $_ -Confirm:$false
        }
        Write-Host "Touchscreen disabled."
    } else {
        Write-Host "No touchscreen found to disable."
    }
} catch {
    Write-Host "Error occurred while disabling touchscreen: $_"
}
