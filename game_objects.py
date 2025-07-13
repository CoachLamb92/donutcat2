from random import randint
from math import radians, cos, sin
import json

class Window:
    def __init__(self, width, height, colour):
        self._width = width
        self._height = height
        self._colour = colour

    def get_width(self):
        return self._width
    
    def get_height(self):
        return self._height
    
    def get_colour(self):
        return self._colour

class Border:
    def __init__(self, window, thickness, colour):
        self._x_co = window.get_width()//10
        self._y_co = window.get_height()//10
        self._width = (4*window.get_width())//5
        self._height = (4*window.get_height())//5
        self._thickness = thickness
        self._colour = colour

    def get_x_co(self):
        return self._x_co
    
    def get_y_co(self):
        return self._y_co
    
    def get_width(self):
        return self._width
    
    def get_height(self):
        return self._height
    
    def get_thickness(self):
        return self._thickness
    
    def get_colour(self):
        return self._colour
    
    def get_rect(self):
        return (self._x_co, self._y_co, self._width, self._height)

class Player:
    def __init__(self, window):
        self._radius = 7
        self._colour = (255, 255, 255)
        self._velocity = 0.3
        self._x = window.get_width()//2
        self._y = window.get_height()//2    

    def get_radius(self):
        return self._radius
    
    def get_colour(self):
        return self._colour
    
    def get_velocity(self):
        return self._velocity
    
    def get_x(self):
        return self._x
    
    def get_y(self):
        return self._y
    
    def get_position(self):
        return (self._x, self._y)
    
    def token_collection(self, position):
        # (x-xc)**2 + (y-yc)**2 = r**2
        x_diff = (position[0]-self._x)
        y_diff = (position[1]-self._y)
        if (x_diff**2 + y_diff**2) <= self._radius**2:
            return True
        else:
            return False

    
    def update_x(self, direction):
        if direction == "left":
            self._x -= self._velocity
        if direction == "right":
            self._x += self._velocity

    def update_y(self, direction):
        if direction == "up":
            self._y -= self._velocity
        if direction == "down":
            self._y += self._velocity

class Enemy:
    def __init__(self, window, border):
        self._radius = 7
        self._border_x = border.get_x_co()
        self._border_y = border.get_y_co()
        self._border_thickness = border.get_thickness()
        self._arena_width = border.get_width()
        self._arean_height = border.get_height()
        self._x_a = randint(window.get_width()//10 + self._border_thickness, (9*window.get_width())//20 - (self._border_thickness + self._radius))
        self._x_b = randint((11*window.get_width())//20, (9*window.get_width())//10 - (self._border_thickness + self._radius))
        self._y_a = randint(window.get_height()//10 + self._border_thickness, (9*window.get_height())//20 - (self._border_thickness + self._radius))
        self._y_b = randint((11*window.get_height())//20, (9*window.get_height())//10 - (self._border_thickness + self._radius))
        self._x = randint(self._x_a, self._x_b)
        self._y = randint(self._y_a, self._y_b)
        self._colour = (255, 0 ,0)
        self._base_velocity = 0.1
        self._current_velocity = 0.3
        self._movement_angle = radians(randint(0, 3599)/10)
        self._x_velocity = self._current_velocity * cos(self._movement_angle)
        self._y_velocity = self._current_velocity * sin(self._movement_angle)
        self._hitbox = [(self._x + self._radius * cos(angle), self._y + self._radius * sin(angle)) for angle in [radians(x) for x in range(0, 360, 20)]]

    def get_radius(self):
        return self._radius
    
    def get_x(self):
        return self._x
    
    def get_y(self):
        return self._y
    
    def get_position(self):
        return (self._x, self._y)
    
    def get_colour(self):
        return self._colour
    
    def get_base_velocity(self):
        return self._base_velocity
    
    def get_x_velocity(self):
        return self._x_velocity
    
    def get_y_velocity(self):
        return self._y_velocity
    
    def increase_velocity(self):
        self._current_velocity += self._base_velocity
        self._x_velocity = self._current_velocity * cos(self._movement_angle)
        self._y_velocity = self._current_velocity * sin(self._movement_angle)

    def reset_velocity(self):
        self._current_velocity = 0.3
        self._x_velocity = self._current_velocity * cos(self._movement_angle)
        self._y_velocity = self._current_velocity * sin(self._movement_angle)

    def set_movement_angle(self, direction):
        if direction == "up":
            self._movement_angle = radians(randint(1801, 3599)/10)
            self._x_velocity = self._current_velocity * cos(self._movement_angle)
            self._y_velocity = self._current_velocity * sin(self._movement_angle)
        elif direction == "down":
            self._movement_angle = radians(randint(1, 1799)/10)
            self._x_velocity = self._current_velocity * cos(self._movement_angle)
            self._y_velocity = self._current_velocity * sin(self._movement_angle)
        elif direction == "left":
            self._movement_angle = radians(randint(901, 2699)/10)
            self._x_velocity = self._current_velocity * cos(self._movement_angle)
            self._y_velocity = self._current_velocity * sin(self._movement_angle)
        elif direction == "right":
            self._movement_angle = radians(randint(2701, 4499)/10)
            self._x_velocity = self._current_velocity * cos(self._movement_angle)
            self._y_velocity = self._current_velocity * sin(self._movement_angle)

    def movement(self):
        if (self._x - self._radius + 1) <= (self._border_x + self._border_thickness - 1):
            self.set_movement_angle("right")
        if (self._x + self._radius - 1) >= (self._border_x + self._arena_width - self._border_thickness):
            self.set_movement_angle("left")
        if (self._y - self._radius + 1) <= (self._border_y + self._border_thickness - 1):
            self.set_movement_angle("down")
        if (self._y + self._radius - 1) >= (self._border_y + self._arean_height - self._border_thickness):
            self.set_movement_angle("up")
        self._x += self._x_velocity
        self._y += self._y_velocity

    def increase_radius(self):
        self._radius += 7

class Token:
    def __init__(self, border):
        self._thickness = 10
        self._colour = (0, 0, 255)
        self._left_arena_edge = border.get_x_co()
        self._top_arena_edge = border.get_y_co()
        self._arena_width = border.get_width()
        self._arena_height = border.get_height()
        self._border_thickness = border.get_thickness()
        self._x = randint(self._left_arena_edge + self._border_thickness, self._left_arena_edge + self._arena_width - self._border_thickness - self._thickness + 2)
        self._y = randint(self._top_arena_edge + self._border_thickness, self._top_arena_edge + self._arena_height - self._border_thickness - self._thickness + 2)
        self._left_edge = [(self._x, self._y + i) for i in range(self._thickness)]
        self._right_edge = [(self._x + self._thickness - 1, self._y + i) for i in range(self._thickness)]
        self._top_edge = [(self._x + i, self._y) for i in range(1, self._thickness)]
        self._bottom_edge = [(self._x + i, self._y + self._thickness - 1) for i in range(1, self._thickness)]
        self._border_coords = self._left_edge + self._right_edge + self._top_edge + self._bottom_edge

    def get_thickness(self):
        return self._thickness

    def get_x(self):
        return self._x
    
    def get_y(self):
        return self._y
    
    def get_position(self):
        return (self._x, self._y)
    
    def get_colour(self):
        return (self._colour)
    
    def get_token(self):
        return (self._x, self._y, self._thickness, self._thickness)
    
    def get_border_coords(self):
        return self._border_coords
    
    def generate_border_coords(self):
        self._left_edge = [(self._x, self._y + i) for i in range(self._thickness)]
        self._right_edge = [(self._x + self._thickness - 1, self._y + i) for i in range(self._thickness)]
        self._top_edge = [(self._x + i, self._y) for i in range(1, self._thickness)]
        self._bottom_edge = [(self._x + i, self._y + self._thickness - 1) for i in range(1, self._thickness)]
        self._border_coords = self._left_edge + self._right_edge + self._top_edge + self._bottom_edge
    
    def generate_token(self):
        self._x = randint(self._left_arena_edge + self._border_thickness, self._left_arena_edge + self._arena_width - self._border_thickness - self._thickness + 2)
        self._y = randint(self._top_arena_edge + self._border_thickness, self._top_arena_edge + self._arena_height - self._border_thickness - self._thickness + 2)
        self.generate_border_coords()

class Highscore_Table:
    def __init__(self):
        self._table = self.load_highscores()
    
    def get_highscores(self):
        return self._table
    
    def update_table(self, new_entry):
        self._table.append(new_entry)
        self._table = sorted(self._table, key=lambda x: x["Score"], reverse=True)[:10]

    def load_highscores(self):
        with open("highscores.json", "r") as file:
            content = json.load(file)
        return [x for x in content["Scores"]]
    
    def save_highscores(self):
        with open("highscores.json", "w") as file:
            data = {"Scores": self._table}
            json.dump(data, file, indent=4)





