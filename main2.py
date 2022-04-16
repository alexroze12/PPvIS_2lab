from kivy.metrics import dp
from kivy.uix.anchorlayout import AnchorLayout
from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable
from Model.my_screen_model import MenuScreenModel
from ppvis2.Utility.SAX_reader import SaxReader
from ppvis2.Model.my_screen_model import MenuScreenModel
from kivymd.uix.screen import Screen


class View(MDApp):
    def build(self):
        s = AnchorLayout()
        self.datatable = MDDataTable(
            size_hint=(1, 1),
            use_pagination=True,
            rows_num=7,
            column_data=[
               ("Pet's name", dp(20)),
               ("Date of birth", dp(25)),
               ("Date of last admission", dp(37)),
               ("Veterinarian's FIO", dp(38)),
               ("Diagnosis", dp(15))
            ]
        )
        handler = SaxReader()
        handler.parser.setContentHandler(handler)
        handler.parser.parse("1_file.xml")
        i = 0
        for i in range(len(handler.table_data)):
            self.datatable.row_data.append(handler.table_data[i])
        s.add_widget(self.datatable)
        return s

#View().run()
