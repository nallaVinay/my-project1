from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.image import Image


class CameraClick(Screen):
    def capture(self):
        self.ids.img = self.add_widget(Image(source='im.png'))
        print("Captured")


class MainWindow(Screen):
    pass


class ScreenManage(ScreenManager):
    pass


class TestCamera(App):

    def build(self):
        return ScreenManage()


TestCamera().run()
