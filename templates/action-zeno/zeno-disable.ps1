# Disable keyboard
try {
    $keyboard = Get-PnpDevice -Class Keyboard
    if ($keyboard) {
        $keyboard | ForEach-Object {
            try {
                Disable-PnpDevice -InstanceId $_.InstanceId -Confirm:$false
            } catch {
                Write-Host "Failed to disable keyboard: $_"
            }
        }
    } else {
        Write-Host "Keyboard not found."
    }
} catch {
    Write-Host "Error occurred while attempting to disable keyboard: $_"
}

# Disable mouse
try {
    $mouse = Get-PnpDevice -Class Mouse
    if ($mouse) {
        $mouse | ForEach-Object {
            try {
                Disable-PnpDevice -InstanceId $_.InstanceId -Confirm:$false
            } catch {
                Write-Host "Failed to disable mouse: $_"
            }
        }
    } else {
        Write-Host "Mouse not found."
    }
} catch {
    Write-Host "Error occurred while attempting to disable mouse: $_"
}

# Disable touchpad (or touchscreen)
try {
    $touchpad = Get-PnpDevice -Class "HIDClass" | Where-Object { $_.DeviceID -like "*touchpad*" -or $_.DeviceID -like "*touch*" }
    if ($touchpad) {
        $touchpad | ForEach-Object {
            try {
                Disable-PnpDevice -InstanceId $_.InstanceId -Confirm:$false
            } catch {
                Write-Host "Failed to disable touchpad: $_"
            }
        }
    } else {
        Write-Host "Touchpad or touchscreen not found."
    }
} catch {
    Write-Host "Error occurred while attempting to disable touchpad or touchscreen: $_"
}
