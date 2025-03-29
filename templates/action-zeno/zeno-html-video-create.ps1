# Define paths
$videoPath = "file:///$PWD/zeno-video.mp4"
$htmlPath = "$env:TEMP\zeno-fullscreen-video.html"

# HTML content
$htmlContent = @"
<!DOCTYPE html>
<html>
<head>
  <meta charset='UTF-8'>
  <style>
    html, body { margin: 0; padding: 0; height: 100%; background: black; }
    video { width: 100vw; height: 100vh; object-fit: cover; }
  </style>
</head>
<body>
  <video  width="700" height="500" src='$videoPath' autoplay loop muted playsinline></video>
  <script>
    document.addEventListener('DOMContentLoaded', () => {
      const vid = document.querySelector('video');
      vid.requestFullscreen().catch(err => {
        console.log('Fullscreen error:', err);
      });
    });
  </script>
</body>
</html>
"@

# Write HTML content to the file
$htmlContent | Out-File -FilePath $htmlPath -Encoding UTF8

# Open the HTML file in Firefox or Chrome
$chromePath = "C:\Program Files\Google\Chrome\Application\chrome.exe"
$firefoxPath = "C:\Program Files\Mozilla Firefox\firefox.exe"
if (Test-Path $firefoxPath) {
    Start-Process $firefoxPath -ArgumentList "-url $htmlPath"
elseif (Test-Path $chromePath) {
    Start-Process $chromePath -ArgumentList "--kiosk $htmlPath"
}

} else {
    Write-Host "Neither Chrome nor Firefox is installed."
}

powershell -ExecutionPolicy Bypass -File ".\zeno-disable.ps1"
