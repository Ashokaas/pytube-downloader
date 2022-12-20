Notification.requestPermission()

function SendNotification(message) {
    new Notification(title="Downloader Pytube", {body: message})
}