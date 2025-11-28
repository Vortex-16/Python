"""
Beautiful Wedding Wish Page for Sakshi Didi & Rajat Jiju
Marriage Date: 30th November 2025

A stunning GUI application with animations, effects, and heartfelt wishes!
Created with love ❤️
"""

import tkinter as tk
from tkinter import font
import random
import time
from datetime import datetime

# Import custom modules
import wedding_config as config
import wedding_effects as effects
import wedding_messages as messages


class WeddingWishPage:
    """Main class for the wedding wish application"""
    
    def __init__(self, root):
        self.root = root
        self.root.title(f"💑 Wedding Wishes for {config.BRIDE_NAME} & {config.GROOM_NAME} 💑")
        
        # Get screen dimensions
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        # Set window size (90% of screen)
        window_width = int(screen_width * 0.9)
        window_height = int(screen_height * 0.9)
        
        # Center the window
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")
        self.root.configure(bg=config.BACKGROUND_COLOR)
        
        # Initialize effects
        self.sparkles = []
        self.hearts = []
        self.pulse = effects.PulsingEffect()
        self.message_index = 0
        self.emoji_index = 0
        
        # Animation state
        self.animation_running = True
        
        # Setup UI
        self.setup_ui()
        
        # Initialize effects
        self.init_effects()
        
        # Start animations
        self.animate()
        self.cycle_messages()
        
    def setup_ui(self):
        """Setup the user interface"""
        
        # Main container
        main_frame = tk.Frame(self.root, bg=config.BACKGROUND_COLOR)
        main_frame.pack(expand=True, fill='both', padx=20, pady=20)
        
        # Canvas for animations
        self.canvas = tk.Canvas(
            main_frame,
            bg=config.BACKGROUND_COLOR,
            highlightthickness=0
        )
        self.canvas.pack(fill='both', expand=True)
        
        # Get canvas dimensions
        self.root.update()
        self.canvas_width = self.canvas.winfo_width()
        self.canvas_height = self.canvas.winfo_height()
        
        # Title Section
        title_y = 50
        self.canvas.create_text(
            self.canvas_width // 2,
            title_y,
            text="💖 Wedding Celebration 💖",
            font=config.TITLE_FONT,
            fill=config.PRIMARY_COLOR,
            tags="title"
        )
        
        # Names Section with decorative elements
        names_y = title_y + 80
        
        # Decorative line before names
        self.canvas.create_line(
            self.canvas_width // 2 - 200, names_y - 20,
            self.canvas_width // 2 + 200, names_y - 20,
            fill=config.SECONDARY_COLOR, width=2
        )
        
        self.canvas.create_text(
            self.canvas_width // 2,
            names_y,
            text=config.BRIDE_NAME,
            font=config.NAME_FONT,
            fill=config.PRIMARY_COLOR,
            tags="bride_name"
        )
        
        self.canvas.create_text(
            self.canvas_width // 2,
            names_y + 45,
            text="&",
            font=("Brush Script MT", 32, "bold"),
            fill=config.SECONDARY_COLOR
        )
        
        self.canvas.create_text(
            self.canvas_width // 2,
            names_y + 85,
            text=config.GROOM_NAME,
            font=config.NAME_FONT,
            fill=config.PRIMARY_COLOR,
            tags="groom_name"
        )
        
        # Decorative line after names
        self.canvas.create_line(
            self.canvas_width // 2 - 200, names_y + 110,
            self.canvas_width // 2 + 200, names_y + 110,
            fill=config.SECONDARY_COLOR, width=2
        )
        
        # Date Section
        date_y = names_y + 150
        self.canvas.create_text(
            self.canvas_width // 2,
            date_y,
            text=f"🗓️ {config.WEDDING_DATE} 🗓️",
            font=config.DATE_FONT,
            fill=config.TEXT_COLOR
        )
        
        # Rotating message
        message_y = date_y + 60
        self.rotating_message = self.canvas.create_text(
            self.canvas_width // 2,
            message_y,
            text=messages.MAIN_WISHES[0],
            font=config.SUBTITLE_FONT,
            fill=config.PRIMARY_COLOR,
            tags="rotating_msg"
        )
        
        # Personal message box
        personal_msg_y = message_y + 80
        
        # Create a decorative frame
        frame_padding = 30
        msg_lines = messages.PERSONAL_MESSAGE.strip().split('\n')
        line_height = 25
        box_height = len(msg_lines) * line_height + frame_padding * 2
        box_width = 700
        
        # Draw decorative box
        self.canvas.create_rectangle(
            self.canvas_width // 2 - box_width // 2,
            personal_msg_y,
            self.canvas_width // 2 + box_width // 2,
            personal_msg_y + box_height,
            outline=config.SECONDARY_COLOR,
            width=3,
            fill="#FFFAF0"
        )
        
        # Add personal message
        self.canvas.create_text(
            self.canvas_width // 2,
            personal_msg_y + frame_padding,
            text=messages.PERSONAL_MESSAGE.strip(),
            font=config.MESSAGE_FONT,
            fill=config.TEXT_COLOR,
            width=box_width - 60,
            justify='center',
            anchor='n'
        )
        
        # Bottom blessing with emojis
        blessing_y = personal_msg_y + box_height + 40
        self.blessing_text = self.canvas.create_text(
            self.canvas_width // 2,
            blessing_y,
            text=messages.BLESSINGS[0],
            font=("Comic Sans MS", 20, "bold"),
            fill=config.HEART_COLOR,
            tags="blessing"
        )
        
        # Celebration emojis
        emoji_y = blessing_y + 50
        self.emoji_text = self.canvas.create_text(
            self.canvas_width // 2,
            emoji_y,
            text=messages.CELEBRATION_EMOJIS,
            font=("Segoe UI Emoji", 24),
            tags="emojis"
        )
        
    def init_effects(self):
        """Initialize visual effects"""
        # Create sparkles
        for _ in range(config.SPARKLE_COUNT):
            sparkle = effects.Sparkle(
                random.randint(0, self.canvas_width),
                random.randint(0, self.canvas_height),
                self.canvas_width,
                self.canvas_height
            )
            self.sparkles.append(sparkle)
            
        # Create floating hearts
        for _ in range(config.HEART_COUNT):
            heart = effects.FloatingHeart(
                random.randint(0, self.canvas_width),
                random.randint(0, self.canvas_height),
                self.canvas_width,
                self.canvas_height
            )
            self.hearts.append(heart)
            
    def animate(self):
        """Main animation loop"""
        if not self.animation_running:
            return
            
        # Clear previous effects
        self.canvas.delete("sparkle", "heart")
        
        # Update and draw sparkles
        for sparkle in self.sparkles:
            sparkle.update()
            x, y, size = sparkle.get_position()
            self.canvas.create_oval(
                x - size, y - size,
                x + size, y + size,
                fill=sparkle.color,
                outline="",
                tags="sparkle"
            )
            
        # Update and draw hearts
        for heart in self.hearts:
            heart.update()
            points = heart.get_heart_points()
            if len(points) > 4:
                self.canvas.create_polygon(
                    points,
                    fill=config.HEART_COLOR,
                    outline=config.PRIMARY_COLOR,
                    width=1,
                    tags="heart"
                )
        
        # Apply pulsing effect to title
        scale = self.pulse.update()
        self.canvas.itemconfig("title", font=("Edwardian Script ITC", int(48 * scale), "bold"))
        
        # Schedule next animation frame
        self.root.after(config.ANIMATION_SPEED, self.animate)
        
    def cycle_messages(self):
        """Cycle through different messages"""
        if not self.animation_running:
            return
            
        # Update rotating message
        self.message_index = (self.message_index + 1) % len(messages.MAIN_WISHES)
        self.canvas.itemconfig(
            self.rotating_message,
            text=messages.MAIN_WISHES[self.message_index]
        )
        
        # Update blessing
        self.emoji_index = (self.emoji_index + 1) % len(messages.BLESSINGS)
        self.canvas.itemconfig(
            self.blessing_text,
            text=messages.BLESSINGS[self.emoji_index]
        )
        
        # Schedule next message change (every 3 seconds)
        self.root.after(3000, self.cycle_messages)
        
    def run(self):
        """Start the application"""
        self.root.mainloop()


def main():
    """Main entry point"""
    root = tk.Tk()
    app = WeddingWishPage(root)
    app.run()


if __name__ == "__main__":
    main()
