from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label


def screen_name(name_of_necessary_screen):
    sm.current = name_of_necessary_screen


class ScreenMenu(Screen):
    def __init__(self, **kw):
        super(ScreenMenu, self).__init__(**kw)
        box = BoxLayout(orientation="horizontal", padding=[20, 250], spacing=20)
        box.add_widget(Button(text="Add", on_press=lambda x: screen_name('add')))
        box.add_widget(Button(text="Delete", on_press=lambda x: screen_name("delete")))
        box.add_widget(Button(text="Search", on_press=lambda x: screen_name("search")))
        self.add_widget(box)


class AddMenu(Screen):
    def __init__(self, **kw):
        super(AddMenu, self).__init__(**kw)
        box = AnchorLayout(anchor_x='center', anchor_y='bottom')
        box.add_widget(Button(text="To the main screen", size_hint=(.2, .08), on_press=lambda x: screen_name('menu')))
        self.add_widget(box)
        box_second = GridLayout(cols=5, rows=11, padding=[10, 10, 10, 100], spacing=4)
        box_second.add_widget(Button(text="pet's name"))
        box_second.add_widget(Button(text="date of birth"))
        box_second.add_widget(Button(text="date of last admission"))
        box_second.add_widget(Button(text="veterinarian's name"))
        box_second.add_widget(Button(text="diagnosis"))
        x = 5
        for x in range(50):
            box_second.add_widget(TextInput())
        self.add_widget(box_second)


class DeleteMenu(Screen):
    def __init__(self, **kw):
        super(DeleteMenu, self).__init__(**kw)
        anch = AnchorLayout(anchor_x='center', anchor_y='bottom')
        anch.add_widget(Button(text="To the main screen", size_hint=(.2, .08), on_press=lambda x: screen_name('menu')))
        # box = BoxLayout(orientation="horizontal", padding=[20, 250], spacing=20)
        # box.add_widget(Button(text="Delete"))
        self.add_widget(anch)


class SearchMenuFirst(Screen):
    def __init__(self, first, **kw):
        self.first = first
        super(SearchMenuFirst, self).__init__(**kw)
        box = GridLayout(cols=2, rows=2, padding=[20, 20, 20, 520], spacing=4)
        box.add_widget(Button(text="pet's name"))
        box.add_widget(Button(text="date of birth"))
        x = 2
        for x in range(2):
            box.add_widget(TextInput())
        self.add_widget(box)


class SearchMenuSecond(Screen):
    def __init__(self, **kw):
        super(SearchMenuSecond, self).__init__(**kw)
        box = GridLayout(cols=2, rows=2, padding=[20, 20, 20, 520], spacing=4)
        box.add_widget(Button(text="date of last admission"))
        box.add_widget(Button(text="veterinarian's name"))
        x = 2
        for x in range(2):
            box.add_widget(TextInput())
        self.add_widget(box)


class SearchMenuThird(Screen):
    def __init__(self, **kw):
        super(SearchMenuThird, self).__init__(**kw)
        box = GridLayout(cols=1, rows=2, padding=[20, 20, 20, 520], spacing=4)
        box.add_widget(Button(text="diagnosis"))
        x = 1
        for x in range(1):
            box.add_widget(TextInput())
        self.add_widget(box)


class SearchMenu(Screen):
    def __init__(self, **kw):
        super(SearchMenu, self).__init__(**kw)
        anch = AnchorLayout(anchor_x='center', anchor_y='bottom')
        anch.add_widget(Button(text="To the main screen", size_hint=(.2, .08), on_press=lambda x: screen_name('menu')))
        # box = BoxLayout(orientation="horizontal", padding=[20, 250], spacing=20)
        # box.add_widget(Button(text="Search"))
        self.add_widget(anch)
        box1 = AnchorLayout(anchor_x='left', anchor_y='top', padding=[15, 30, 0, 0])
        box2 = AnchorLayout(anchor_x='left', anchor_y='top', padding=[15, 80, 0, 0])
        box3 = AnchorLayout(anchor_x='left', anchor_y='top', padding=[15, 130, 0, 0])
        box1.add_widget(Button(size_hint=(.01, .01), on_press=lambda x: screen_name('first search'), background_color=[2,0,0,1]))
        box2.add_widget(Button(size_hint=(.01, .01), on_press=lambda x: screen_name('second search'), background_color=[2,0,0,1]))
        box3.add_widget(Button(size_hint=(.01, .01), on_press=lambda x: screen_name('third search'), background_color=[2, 0, 0, 1]))
        box4 = Label(text="pet's name and date of birth", size_hint=(0.35, 1.9))
        box5 = Label(text="date of last admission and veterinarian's name", size_hint=(0.5, 1.73))
        box6 = Label(text="diagnosis", size_hint=(0.19, 1.56))
        self.add_widget(box1)
        self.add_widget(box2)
        self.add_widget(box3)
        self.add_widget(box4)
        self.add_widget(box5)
        self.add_widget(box6)

text="asd"
sm = ScreenManager()
sm.add_widget(ScreenMenu(name="menu"))
sm.add_widget(AddMenu(name="add"))
sm.add_widget(SearchMenu(name="search"))
sm.add_widget(DeleteMenu(name="delete"))
sm.add_widget(SearchMenuFirst(text, name="first search"))
sm.add_widget(SearchMenuSecond(name="second search"))
sm.add_widget(SearchMenuThird(name="third search"))

class MyApp(App):
    #def __init__(self, **kw):
     #   super(MyApp, self).__init__(**kw)

    def build(self):
        return sm

if __name__ == "__main__":
    MyApp().run()
