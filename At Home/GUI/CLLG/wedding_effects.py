"""
Wedding Effects Module
Contains classes for various visual effects like hearts, sparkles, and animations
"""

import random
import math


class Sparkle:
    """Class to represent a sparkle/star effect"""
    def __init__(self, x, y, canvas_width, canvas_height):
        self.x = x
        self.y = y
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height
        self.size = random.randint(2, 5)
        self.velocity_x = random.uniform(-1, 1)
        self.velocity_y = random.uniform(-2, 0)
        self.alpha = random.uniform(0.5, 1.0)
        self.color = random.choice(['#FFD700', '#FFF8DC', '#FFFFE0', '#F0E68C'])
        
    def update(self):
        """Update sparkle position"""
        self.x += self.velocity_x
        self.y += self.velocity_y
        
        # Reset if out of bounds
        if self.y < 0 or self.x < 0 or self.x > self.canvas_width:
            self.y = self.canvas_height
            self.x = random.randint(0, self.canvas_width)
            
    def get_position(self):
        """Return current position"""
        return (self.x, self.y, self.size)


class FloatingHeart:
    """Class to represent a floating heart"""
    def __init__(self, x, y, canvas_width, canvas_height):
        self.x = x
        self.y = y
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height
        self.size = random.randint(15, 30)
        self.velocity_y = random.uniform(-1.5, -0.5)
        self.velocity_x = random.uniform(-0.5, 0.5)
        self.angle = random.uniform(0, 360)
        self.rotation_speed = random.uniform(-5, 5)
        
    def update(self):
        """Update heart position and rotation"""
        self.x += self.velocity_x
        self.y += self.velocity_y
        self.angle += self.rotation_speed
        
        # Reset if out of bounds
        if self.y < -50:
            self.y = self.canvas_height + 50
            self.x = random.randint(0, self.canvas_width)
            
    def get_heart_points(self):
        """Calculate heart shape points"""
        points = []
        for i in range(0, 360, 10):
            t = math.radians(i)
            # Parametric heart equation
            x = 16 * math.sin(t) ** 3
            y = -(13 * math.cos(t) - 5 * math.cos(2*t) - 2 * math.cos(3*t) - math.cos(4*t))
            
            # Scale and translate
            scaled_x = self.x + (x * self.size / 20)
            scaled_y = self.y + (y * self.size / 20)
            points.extend([scaled_x, scaled_y])
            
        return points


class PulsingEffect:
    """Class to create pulsing animation effect"""
    def __init__(self, min_scale=0.9, max_scale=1.1, speed=0.05):
        self.min_scale = min_scale
        self.max_scale = max_scale
        self.speed = speed
        self.current_scale = min_scale
        self.direction = 1
        
    def update(self):
        """Update the pulse scale"""
        self.current_scale += self.speed * self.direction
        
        if self.current_scale >= self.max_scale:
            self.direction = -1
        elif self.current_scale <= self.min_scale:
            self.direction = 1
            
        return self.current_scale
