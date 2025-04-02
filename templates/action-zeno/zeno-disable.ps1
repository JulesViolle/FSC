# Disable all connected keyboard, mouse, touchpad, or touchscreen devices

# Disable any keyboard (including internal laptop keyboards)
try {
    $inputDevices = Get-WmiObject Win32_PnPEntity | Where-Object { $_.DeviceID -match "HID" -or $_.Description -like "*keyboard*" }
    if ($inputDevices) {
        $inputDevices.PNPDeviceID | ForEach-Object {
            Disable-PnpDevice -InstanceId $_ -Confirm:$false
        }
        Write-Host "Keyboard(s) (including internal) disabled."
    } else {
        Write-Host "No keyboard(s) found to disable."
    }
} catch {
    Write-Host "Error occurred while disabling keyboard(s): $_"
}

# Disable any mouse or touchpad (including internal touchpads)
try {
    $inputDevices = Get-WmiObject Win32_PnPEntity | Where-Object { $_.Description -like "*mouse*" -or $_.Description -like "*touchpad*" }
    if ($inputDevices) {
        $inputDevices.PNPDeviceID | ForEach-Object {
            Disable-PnpDevice -InstanceId $_ -Confirm:$false
        }
        Write-Host "Mouse/Touchpad(s) (including internal) disabled."
    } else {
        Write-Host "No mouse/touchpad(s) found to disable."
    }
} catch {
    Write-Host "Error occurred while disabling mouse/touchpad(s): $_"
}

# Disable any touchscreen (if present)
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
