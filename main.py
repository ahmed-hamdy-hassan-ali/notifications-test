from flet import *
from flet_android_notifications import FletAndroidNotifications

def main(page: Page):
    notifications = FletAndroidNotifications()

    async def send(e):
        await notifications.request_permissions()
        await notifications.show_notification(
            notification_id=1, title="Hello", body="It works Abo Hamdy!",
        )

    page.add(Button(content="Send", on_click=send))
    page.update()

run(main)