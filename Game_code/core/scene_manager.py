from Game_code.scenes.gameplay_scene import GameplayScene
from Game_code.scenes.menu_scene import MenuScene


class SceneManager:
    def __init__(self, screen):
        self.screen = screen
        # self.current_scene = None
        self.scene_stack = []
    
    def push(self, scene):
        self.scene_stack.append(scene)
        
    def pop(self):
        if self.scene_stack:
            self.scene_stack.pop()
            
    def replace(self, scene):
        self.pop()
        self.push(scene)
    
    def load_scene(self, name):
        if name == "menu":
            self.replace(MenuScene(self.screen, self))
        
        elif name == "gameplay":
            self.replace(GameplayScene(self.screen, self))
        
    # def change_scene(self, new_scene):
    #     self.current_scene = new_scene
        
    def handle_events(self, events):
        # self.current_scene.handle_events(events)
        if self.scene_stack:
            self.scene_stack[-1].handle_events(events)
        
    def update(self):
        # self.current_scene.update()
        if self.scene_stack:
            self.scene_stack[-1].update()
        
    def render(self):
        # self.current_scene.render()
        for scene in self.scene_stack:
            scene.render()