from abc import ABC, abstractmethod

class Scene(ABC):
    def __init__(self, screen):
        self.screem = screen

    @abstractmethod
    def handle_events(self, events):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def render(self):
        pass