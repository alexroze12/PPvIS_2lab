# The model implements the observer pattern. This means that the class must
# support adding, removing, and alerting observers. In this case, the model is
# completely independent of controllers and views. It is important that all
# registered observers implement a specific method that will be called by the
# model when they are notified (in this case, it is the `model_is_changed`
# method). For this, observers must be descendants of an abstract class,
# inheriting which, the `model_is_changed` method must be overridden.

from ppvis2.Utility.SAX_reader import SaxReader


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

    def read_information_from_file(self):
        handler = SaxReader()
        handler.parser.setContentHandler(handler)
        handler.parser.parse("1_file.xml")
        for x in handler.table_data:
            self.add_new_information(x)

    def add_new_information(self, col):
        self.table_of_data.row_data.append(len(self.table_of_data.row_data), (col[0], col[1], col[2], col[3], col[4]))
