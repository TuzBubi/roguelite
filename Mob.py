import Animation as am
import dialogs


class Mob:
    def __init__(self, x, y):
        self.size_y = None
        self.size_x = None
        self.state = None
        self.health = None
        self.armor = None
        self.attack = None
        self.animation = None
        self.x_pos = x
        self.y_pos = y
        self.x_vel = 0
        self.y_vel = 0
        self.bot_time = 0

    def say_m(self):
        dialogs.say(self, id)

    def collision(self, obj2):
        pass
    
    def sprite_update(self,time):
        pass
    
    def update(self):
        self.x_pos += self.x_vel
        self.y_pos = min(self.y_pos + self.y_vel, 600 - self.size_y)
        if self.y_pos + self.size_y < 600:
            self.y_vel += 1  # da eto g

    def destruction(self):
        """Разрушение моба, сюда нужна будет анимация"""
        pass


if __name__ == '__main__':
    pass
else:
    print('Class Mob connected.')