from abc import ABC, abstractmethod
class Scene:
    def __init__(self, screen):
        self.screen = screen
    
    @abstractmethod    
    def handle_events(self, events):
        raise NotImplementedError
    
    @abstractmethod
    def update(self):
        raise NotImplementedError
    
    @abstractmethod
    def render(self):
        raise NotImplementedError