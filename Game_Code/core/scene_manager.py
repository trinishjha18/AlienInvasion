from Game_Code.core.scene import *

class SceneManager:
    def __init__(self, starting_scene):
        self.current_scene = starting_scene

    def change_scene(self, new_scene):
        self.current_scene = new_scene
        
    def handle_events(self, events):
        self.current_scene.handle_events(events)
        
    def update(self):
        self.current_scene.update()
        
    def render(self):
        self.current_scene.render()