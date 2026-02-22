class LevelSystem:
    def __init__(self):
        self.level = 1

    def next_level(self):
        self.level += 1

    def reset(self):
        self.level = 1