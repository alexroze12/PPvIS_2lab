import os
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivy.metrics import dp
from ppvis2.Utility.DOM_writer import Writer
from kivy.uix.anchorlayout import AnchorLayout
from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable
from ppvis2.Utility.SAX_reader import SaxReader
from kivymd.uix.screen import Screen


Builder.load_file(os.path.join(os.path.dirname(__file__), "my_screen.kv"))


class GeneralScreen(BoxLayout, Screen):
    pass


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
        handler = SaxReader()
        handler.parser.setContentHandler(handler)
        handler.parser.parse("2_file.xml")
        i = 0
        for i in range(len(handler.table_data)):
            self.datatable.row_data.append(handler.table_data[i])

    def on_enter(self):
        self.__init__()


class ShowTable(AddMenuFirst, Screen):
    def __init__(self, **kw):
        super(ShowTable, self).__init__(**kw)
        s = AnchorLayout(anchor_x='center', anchor_y='top')
        s.add_widget(self.datatable)
        self.add_widget(s)


class AddMenu(AddMenuFirst, Screen):
    def __init__(self, **kw):
        super(AddMenu, self).__init__(**kw)
        self.data = []

    def new_information(self):
        s = AnchorLayout(anchor_x='center', anchor_y='top')
        self.data.append(self.ids.pets_name.text)
        self.data.append(self.ids.date_of_birth.text)
        self.data.append(self.ids.last_visit.text)
        self.data.append(self.ids.vets_name.text)
        self.data.append(self.ids.diagnosis.text)
        self.datatable.row_data.append(tuple(self.data))
        dom = Writer("2_file.xml")
        dictionary_with_data_pets = {}
        for data in self.datatable.row_data:
            dictionary_with_data_pets["name_of_an_animal"] = data[0]
            dictionary_with_data_pets["date_of_birth"] = data[1]
            dictionary_with_data_pets["date_of_last_admission"] = data[2]
            dictionary_with_data_pets["FIO_of_veterinary"] = data[3]
            dictionary_with_data_pets["diagnosis"] = data[4]
            dom.create_new_patient(dictionary_with_data_pets)
        dom.create_my_file()
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
        start_counter = len(self.datatable.row_data)
        for data in self.datatable.row_data:
            if self.ids.delete_pets_name.text == data[0] and self.ids.delete_date_of_birth.text == data[1]:
                continue
            elif self.ids.delete_last_visit.text == data[2] and self.ids.delete_vets_name.text == data[3]:
                continue
            elif self.ids.delete_diagnosis.text == data[4]:
                continue
            self.data_table.row_data.append(data)
        finish_counter = len(self.data_table.row_data)
        s.add_widget(self.data_table)
        self.add_widget(s)
        delete_counter = start_counter - finish_counter
        if delete_counter == 0:
            print("No such records found")
        else:
            print("Counter of my deleted records: "+str(delete_counter))

        dom = Writer("2_file.xml")
        dictionary_with_data_pets = {}
        for value in self.data_table.row_data:
            dictionary_with_data_pets["name_of_an_animal"] = value[0]
            dictionary_with_data_pets["date_of_birth"] = value[1]
            dictionary_with_data_pets["date_of_last_admission"] = value[2]
            dictionary_with_data_pets["FIO_of_veterinary"] = value[3]
            dictionary_with_data_pets["diagnosis"] = value[4]
            dom.create_new_patient(dictionary_with_data_pets)
        dom.create_my_file()


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
        for data in self.datatable.row_data:
            if self.ids.search_pets_name.text == data[0] and self.ids.search_date_of_birth.text == data[1]:
                self.data_table.row_data.append(data)
            elif self.ids.search_last_visit.text == data[2] and self.ids.search_vets_name.text == data[3]:
                self.data_table.row_data.append(data)
            elif self.ids.search_diagnosis.text == data[4]:
                self.data_table.row_data.append(data)
        s.add_widget(self.data_table)
        self.add_widget(s)


class BuildScreen(MDApp):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(GeneralScreen(name='menu'))
        sm.add_widget(ShowTable(name='show'))
        sm.add_widget(AddMenu(name='add'))
        sm.add_widget(SearchMenu(name="search"))
        sm.add_widget(DeleteMenu(name="delete"))
        return sm


BuildScreen().run()
