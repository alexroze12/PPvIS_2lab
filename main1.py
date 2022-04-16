from kivymd.app import MDApp
from kivy.app import App
from ppvis2.test_app import BuildScreen


class TestCallScreen(MDApp):
    @property
    def build(self):
        return BuildScreen()


TestCallScreen().run()
