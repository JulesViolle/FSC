# Disable All Input Devices (Keyboard, Mouse, Touchpad, Touchscreen)

# Disable All Input Devices (Including Built-in Devices)
try {
    # Get all input devices, including HID, keyboard, mouse, touchpad, touchscreen
    $inputDevices = Get-WmiObject Win32_PnPEntity | Where-Object { 
        $_.DeviceID -match "HID" -or 
        $_.Description -like "*keyboard*" -or 
        $_.Description -like "*mouse*" -or 
        $_.Description -like "*touchpad*" -or 
        $_.Description -like "*touchscreen*"
    }

    if ($inputDevices) {
        $inputDevices | ForEach-Object {
            try {
                # Attempt to disable each device by InstanceId
                Disable-PnpDevice -InstanceId $_.PNPDeviceID -Confirm:$false
                Write-Host "Device disabled: $($_.Description)"
            } catch {
                Write-Host "Failed to disable device: $($_.Description) - $_"
            }
        }
    } else {
        Write-Host "No input devices found to disable."
    }
} catch {
    Write-Host "Error occurred while attempting to disable input devices: $_"
}
