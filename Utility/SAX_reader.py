import xml.sax


class SaxReader(xml.sax.ContentHandler):
    def __init__(self):
        super().__init__()
        self.massiv = []
        self.table_data = []
        self.current = ""
        self.name_of_an_animal = ""
        self.date_of_birth = ""
        self.date_of_last_admission = ""
        self.FIO_of_veterinary = ""
        self.diagnosis = ""
        self.pet_data = []
        self.parser = xml.sax.make_parser()

    def startElement(self, tag, attrs):
        self.current = tag
        if tag == "pet":
            pass

    def characters(self, content):
        if self.current == "name_of_an_animal":
            self.name_of_an_animal = content
        elif self.current == "date_of_birth":
            self.date_of_birth = content
        elif self.current == "date_of_last_admission":
            self.date_of_last_admission = content
        elif self.current == "FIO_of_veterinary":
            self.FIO_of_veterinary = content
        elif self.current == "diagnosis":
            self.diagnosis = content

    def endElement(self, name):
        if self.current == "name_of_an_animal":
            self.pet_data.append(self.name_of_an_animal)
        elif self.current == "date_of_birth":
            self.pet_data.append(self.date_of_birth)
        elif self.current == "date_of_last_admission":
            self.pet_data.append(self.date_of_last_admission)
        elif self.current == "FIO_of_veterinary":
            self.pet_data.append(self.FIO_of_veterinary)
        elif self.current == "diagnosis":
            self.pet_data.append(self.diagnosis)

        if len(self.pet_data) == 5:
            self.table_data.append(tuple(self.pet_data))
            self.pet_data = []

        self.current = ""
