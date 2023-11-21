from pynput import mouse


class Recorder:
    def __init__(self, limit=10**5):
        self.click_count = 0
        self.limit = limit

    def on_click(self, x, y, button, pressed):
        if pressed:
            print(f"{self.click_count} Mouse clicked at ({x:.0f}, {y:.0f}) with button {button}")
            self.click_count += 1

        if self.click_count == self.limit:
            exit()


recorder = Recorder()
with mouse.Listener(on_click=recorder.on_click) as listener:
    print("Listening to mouse events. Click anywhere to see the event.")
    listener.join()
