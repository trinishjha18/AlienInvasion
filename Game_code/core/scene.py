class Scene:
    def __init__(self, screen):
        self.screen = screen
        
    def handle_events(self, events):
        raise NotImplementedError
    
    def update(self):
        raise NotImplementedError
    
    def render(self):
        raise NotImplementedError