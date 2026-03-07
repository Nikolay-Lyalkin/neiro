from abc import ABC, abstractmethod


class FigureService(ABC):

    @abstractmethod
    def create(self, *args, **kwargs):
        pass

    @abstractmethod
    def delete(self, *args, **kwargs):
        pass

    @abstractmethod
    def show_figures(self):
        pass

    @abstractmethod
    def save_to_json(self, *args, **kwargs):
        pass

    @abstractmethod
    def load_from_json(self, *args, **kwargs):
        pass
