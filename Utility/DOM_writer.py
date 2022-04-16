import xml.dom.minidom
from xml.dom import minidom


class Writer:
    def __init__(self, file_name: str):
        self.file_name = file_name
        self.doc = minidom.Document()
        self.table = []

    def create_new_patient(self, dictionary: dict):
        patient = self.doc.createElement("pet")
        for value in dictionary:
            temp_child = self.doc.createElement(value)
            patient.appendChild(temp_child)
            node_text = self.doc.createTextNode(dictionary[value].strip())
            temp_child.appendChild(node_text)
        self.table.append(patient)

    def create_my_file(self):
        pass_table = self.doc.createElement("pass_table")
        for patient in self.table:
            pass_table.appendChild(patient)
        self.doc.appendChild(pass_table)

        self.doc.writexml(open(self.file_name, "w"), indent="  ",
                          addindent="  ",
                          newl='\n'
                          )
        self.doc.unlink()
