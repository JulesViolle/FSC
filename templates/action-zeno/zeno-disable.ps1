# Disable any connected keyboard, mouse, touchpad, or touchscreen

# Disable Keyboard
try {
    $inputDevices = Get-WmiObject Win32_PnPEntity | Where-Object { $_.Description -like "*keyboard*" }
    if ($inputDevices) {
        $inputDevices.PNPDeviceID | ForEach-Object {
            Disable-PnpDevice -InstanceId $_ -Confirm:$false
        }
        Write-Host "Keyboard(s) disabled."
    } else {
        Write-Host "No keyboard(s) found to disable."
    }
} catch {
    Write-Host "Error occurred while disabling keyboard(s): $_"
}

# Disable Mouse or Touchpad
try {
    $inputDevices = Get-WmiObject Win32_PnPEntity | Where-Object { $_.Description -like "*mouse*" -or $_.Description -like "*touchpad*" }
    if ($inputDevices) {
        $inputDevices.PNPDeviceID | ForEach-Object {
            Disable-PnpDevice -InstanceId $_ -Confirm:$false
        }
        Write-Host "Mouse/Touchpad(s) disabled."
    } else {
        Write-Host "No mouse/touchpad(s) found to disable."
    }
} catch {
    Write-Host "Error occurred while disabling mouse/touchpad(s): $_"
}

# Disable Touchscreen
try {
    $inputDevices = Get-WmiObject Win32_PnPEntity | Where-Object { $_.Description -like "*touchscreen*" }
    if ($inputDevices) {
        $inputDevices.PNPDeviceID | ForEach-Object {
            Disable-PnpDevice -InstanceId $_ -Confirm:$false
        }
        Write-Host "Touchscreen(s) disabled."
    } else {
        Write-Host "No touchscreen(s) found to disable."
    }
} catch {
    Write-Host "Error occurred while disabling touchscreen(s): $_"
}
