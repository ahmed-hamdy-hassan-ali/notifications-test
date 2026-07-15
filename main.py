from flet import *
from android_notify import Notification

def main(page: Page):
    

    async def send(e):
        Notification(title='Hello',message="Abo hamdy").send()
            

    page.add(Button(content="Send", on_click=send))
    page.update()

run(main)
