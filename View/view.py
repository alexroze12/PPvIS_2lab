import os
import re
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable
from Controller.controller import Controller
from Controller.controller import create_new_empty_file
from Controller.controller import read_information
from Controller.controller import write_information_to_file
Builder.load_file(os.path.join(os.path.dirname(__file__), "my_screen.kv"))


class GeneralScreen(Screen):
    pass


class FileScreen(Screen):
    def __init__(self, **kw):
        super(FileScreen, self).__init__(**kw)

    def first_button(self):
        try:
            pattern = re.compile("\w+.xml")
            if re.match(pattern, self.ids.name.text):
                create_new_empty_file(self.ids.name.text)
                write_information_to_file(self.ids.name.text)
        except ValueError:
            return False

    def second_button(self):
        try:
            pattern = re.compile("\w+.xml")
            if re.match(pattern, self.ids.file.text):
                write_information_to_file(self.ids.file.text)
        except ValueError:
            return False


class AddMenuFirst(Screen):
    def __init__(self, **kw):
        super(AddMenuFirst, self).__init__(**kw)
        self.data = []
        self.datatable = MDDataTable(
            size_hint=(1, 0.8),
            use_pagination=True,
            rows_num=7,
            column_data=[
                ("Pet's name", dp(20)),
                ("Date of birth", dp(25)),
                ("Date of last admission", dp(37)),
                ("Veterinarian's FIO", dp(38)),
                ("Diagnosis", dp(30))
            ]
        )

    def read(self):
        self.datatable.row_data = []
        name_file = read_information()
        Controller(self.datatable).read_information_from_file(name_file)

    def on_enter(self):
        self.read()


class AddMenu(AddMenuFirst, Screen):
    def add_information(self):
        Controller(self.datatable).add_information(
            [self.ids.pets_name.text, self.ids.date_of_birth.text, self.ids.last_visit.text, self.ids.vets_name.text,
             self.ids.diagnosis.text])
        name_file = read_information()
        Controller(self.datatable).write_information(name_file)


class ShowTable(AddMenuFirst, Screen):
    def __init__(self, **kw):
        super(ShowTable, self).__init__(**kw)
        s = AnchorLayout(anchor_x='center', anchor_y='top')
        s.add_widget(self.datatable)
        self.add_widget(s)


class DeleteMenu(AddMenuFirst, Screen):
    def __init__(self, **kw):
        super(DeleteMenu, self).__init__(**kw)

    def delete_information(self):
        s = AnchorLayout(anchor_x='center', anchor_y='bottom', pos_hint={'center_x': .5, 'center_y': .57})
        self.data_table = MDDataTable(
            size_hint=(1, 0.6),
            use_pagination=True,
            rows_num=7,
            column_data=[
                ("Pet's name", dp(20)),
                ("Date of birth", dp(25)),
                ("Date of last admission", dp(37)),
                ("Veterinarian's FIO", dp(38)),
                ("Diagnosis", dp(30))
            ]
        )
        counter_of_deleted = Controller(self.datatable).delete(self.data_table,
                                                                                [self.ids.delete_pets_name.text,
                                                                                 self.ids.delete_date_of_birth.text,
                                                                                 self.ids.delete_last_visit.text,
                                                                                 self.ids.delete_vets_name.text,
                                                                                 self.ids.delete_diagnosis.text])
        name_file = read_information()
        Controller(self.data_table).write_information(name_file)
        s.add_widget(self.data_table)
        self.add_widget(s)
        if counter_of_deleted == 0:
            self.ids.name.text = str(counter_of_deleted)
        else:
            self.ids.name.text = str(counter_of_deleted)


class SearchMenu(AddMenuFirst, Screen):
    def __init__(self, **kw):
        super(SearchMenu, self).__init__(**kw)

    def search_information(self):
        s = AnchorLayout(anchor_x='center', anchor_y='bottom', pos_hint={'center_x': .5, 'center_y': .57})
        self.data_table = MDDataTable(
            size_hint=(1, 0.6),
            use_pagination=True,
            rows_num=7,
            column_data=[
                ("Pet's name", dp(20)),
                ("Date of birth", dp(25)),
                ("Date of last admission", dp(37)),
                ("Veterinarian's FIO", dp(38)),
                ("Diagnosis", dp(30))
            ]
        )
        Controller(self.datatable).search(self.data_table, [self.ids.search_pets_name.text,
                                                            self.ids.search_date_of_birth.text,
                                                            self.ids.search_last_visit.text,
                                                            self.ids.search_vets_name.text,
                                                            self.ids.search_diagnosis.text])
        s.add_widget(self.data_table)
        self.add_widget(s)


class BuildScreen(MDApp):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(FileScreen(name='file'))
        sm.add_widget(GeneralScreen(name='menu'))
        sm.add_widget(ShowTable(name='show'))
        sm.add_widget(AddMenu(name='add'))
        sm.add_widget(SearchMenu(name="search"))
        sm.add_widget(DeleteMenu(name="delete"))
        return sm
