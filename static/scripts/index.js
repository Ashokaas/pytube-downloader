function notifying(title = "ToDo List", message, icon_image = null, bg_image = null) {
    /* Asking for permission if notifications are not allowed */
    if (Notification.permission !== 'granted')
        Notification.requestPermission().then(r => {
            if (r === 'granted') {
                new Notification(title, {
                    body: message,
                    icon: icon_image,
                    image: bg_image
                });
            }
        });
    /* Else, printing notification */
    else {
        new Notification(title, {
            icon: icon_image,
            body: message,
            image: bg_image,
        });
    }
}