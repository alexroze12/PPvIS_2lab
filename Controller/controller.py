from xml.sax.__init__ import SAXParseException

from Utility.SAX_reader import SaxReader
from Model.model import MenuScreenModel
from Utility.DOM_writer import Writer


class Controller:
    def __init__(self, model):
        self.model = model
        self.table = []

    def read_information_from_file(self, name_file):
        handler = SaxReader()
        handler.parser.setContentHandler(handler)
        try:
            handler.parser.parse(name_file)
        except SAXParseException:
            handler.table_data = []
        for i in range(len(handler.table_data)):
            MenuScreenModel(self.model).add_information(handler.table_data[i])

    def write_information(self, name_file):
        dom = Writer(name_file)
        dictionary_with_data_pets = {}
        for data in self.model.row_data:
            dictionary_with_data_pets["name_of_an_animal"] = data[0]
            dictionary_with_data_pets["date_of_birth"] = data[1]
            dictionary_with_data_pets["date_of_last_admission"] = data[2]
            dictionary_with_data_pets["FIO_of_veterinary"] = data[3]
            dictionary_with_data_pets["diagnosis"] = data[4]
            dom.create_new_patient(dictionary_with_data_pets)
        dom.create_my_file()

    def delete(self, table_data, data):
        MenuScreenModel(self.model).delete_information(table_data, data)

    def search(self, table_data, data):
        MenuScreenModel(self.model).search_information(table_data, data)

    def add_information(self, data):
        MenuScreenModel(self.model).add_information(data)


def write_information_to_file(number_of_file):
    file = open('all_files.txt', 'w')
    file.write(number_of_file)
    file.close()


def read_information():
    file = open('all_files.txt', 'r')
    name_file = file.readline()
    return name_file


def create_new_empty_file(name_of_file):
    my_file = open(name_of_file, 'w+')
