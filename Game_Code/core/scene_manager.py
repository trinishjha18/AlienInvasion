from Game_Code.scenes.gameplay_scene import GameplayScene
from Game_Code.scenes.menu_scene import MenuScene
from Game_Code.core.scene import *

class SceneManager:
    def __init__(self, starting_scene):
        self.current_scene = starting_scene

        self.scene_stack = []

    def push(self, scene):
        self.scene_stack.append(scene)

    def pop(self):
        if self.scene_stack:
            self.scene_stack.pop()

    def replace(self, new_scene):
        self.pop()
        self.push(new_scene)

    def load_scene(self, name):
        if name.lower() == "menu":
            self.replace(MenuScene(self.current_scene, self))

        elif name.lower() == "gameplay":
            self.replace(GameplayScene(self.current_scene, self))

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
        # for scene in self.scene_stack:
        #     scene.render()
        if self.scene_stack:
            self.scene_stack[-1].render()