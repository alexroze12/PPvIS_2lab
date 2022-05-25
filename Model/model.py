# The model implements the observer pattern. This means that the class must
# support adding, removing, and alerting observers. In this case, the model is
# completely independent of controllers and views. It is important that all
# registered observers implement a specific method that will be called by the
# model when they are notified (in this case, it is the `model_is_changed`
# method). For this, observers must be descendants of an abstract class,
# inheriting which, the `model_is_changed` method must be overridden.
import datetime


class MenuScreenModel:

    def __init__(self, table_of_data):
        self._observers = []
        self.table_of_data = table_of_data

    def notify_observers(self):
        """
        The method that will be called on the observer when the model changes.
        """

        for observer in self._observers:
            observer.model_is_changed()

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def add_information(self, data):
        try:
            pets_name = str(data[0])
            datetime.datetime.strptime(data[1], '%Y-%m-%d')
            datetime.datetime.strptime(data[2], '%Y-%m-%d')
            fio = str(data[3])
            diagnosis = str(data[4])
            self.table_of_data.row_data.insert(len(self.table_of_data.row_data),
                                               [data[0], data[1], data[2], data[3], data[4]])
        except ValueError:
            print("Input data is invalid!")

    def search_information(self, table_data, data):
        try:
            pets_name = str(data[0])
            datetime.datetime.strptime(data[1], '%Y-%m-%d')
            for information in self.table_of_data.row_data:
                if data[0] == information[0] and data[1] == information[1]:
                    table_data.row_data.append(information)
        except ValueError:
            print("Error! Pets name and date of births are incorrect!")
        try:
            datetime.datetime.strptime(data[2], '%Y-%m-%d')
            fio = str(data[3])
            diagnosis = str(data[4])
            for information in self.table_of_data.row_data:
                if data[2] == information[2] and data[3] == information[3]:
                    table_data.row_data.append(information)
        except ValueError:
            print("Error! FIO and date of last visit are incorrect!")
        try:
            diagnosis = str(data[4])
            for information in self.table_of_data.row_data:
                if data[4] == information[4]:
                    table_data.row_data.append(information)
        except ValueError:
            print("Error!Diagnosis is incorrect!")

    def delete_information(self, table_data, data):
        start_counter = len(self.table_of_data.row_data)
        try:
            pets_name = str(data[0])
            datetime.datetime.strptime(data[1], '%Y-%m-%d')
            for information in self.table_of_data.row_data:
                if data[0] == information[0] and data[1] == information[1]:
                    continue
                table_data.row_data.append(information)
        except ValueError:
            print("Error! Pets name and date of births are incorrect!")
        try:
            datetime.datetime.strptime(data[2], '%Y-%m-%d')
            fio = str(data[3])
            diagnosis = str(data[4])
            for information in self.table_of_data.row_data:
                if data[2] == information[2] and data[3] == information[3]:
                    continue
                table_data.row_data.append(information)
        except ValueError:
            print("Error! FIO and date of last visit are incorrect!")
        try:
            diagnosis = str(data[4])
            for information in self.table_of_data.row_data:
                if data[4] == information[4]:
                    continue
                table_data.row_data.append(information)
        except ValueError:
            print("Error!Diagnosis is incorrect!")
        finish_counter = len(table_data.row_data)
        delete_counter = start_counter - finish_counter
        if delete_counter == 0:
            return 0
        else:
            return delete_counter
