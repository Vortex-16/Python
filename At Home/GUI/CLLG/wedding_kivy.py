"""
Wedding Wish Page - Kivy Version (For Android APK)
Beautiful mobile-friendly version for Sakshi Didi & Rajat Jiju's Wedding
Date: 30th November 2025
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.graphics import Color, Ellipse, Line, Rectangle
from kivy.core.window import Window
import random

# Import wedding modules
import wedding_config as config
import wedding_messages as messages


class WeddingWishApp(App):
    """Main Kivy application for wedding wishes"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.message_index = 0
        self.blessing_index = 0
        
    def build(self):
        """Build the UI"""
        # Set window background color
        Window.clearcolor = (1, 0.94, 0.96, 1)  # Lavender Blush
        
        # Main layout
        main_layout = FloatLayout()
        
        # Add animated background
        self.add_animated_background(main_layout)
        
        # Content layout
        content_layout = BoxLayout(
            orientation='vertical',
            padding=20,
            spacing=15,
            size_hint=(0.9, 0.9),
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        
        # Title
        title = Label(
            text='💖 Wedding Celebration 💖',
            font_size='40sp',
            bold=True,
            color=(1, 0.08, 0.58, 1),  # Deep Pink
            size_hint=(1, 0.1)
        )
        content_layout.add_widget(title)
        
        # Start pulsing animation for title
        self.pulse_animation(title)
        
        # Names section
        bride_name = Label(
            text=config.BRIDE_NAME,
            font_size='32sp',
            bold=True,
            italic=True,
            color=(1, 0.08, 0.58, 1),
            size_hint=(1, 0.08)
        )
        content_layout.add_widget(bride_name)
        
        ampersand = Label(
            text='&',
            font_size='28sp',
            bold=True,
            color=(1, 0.84, 0, 1),  # Gold
            size_hint=(1, 0.05)
        )
        content_layout.add_widget(ampersand)
        
        groom_name = Label(
            text=config.GROOM_NAME,
            font_size='32sp',
            bold=True,
            italic=True,
            color=(1, 0.08, 0.58, 1),
            size_hint=(1, 0.08)
        )
        content_layout.add_widget(groom_name)
        
        # Date
        date_label = Label(
            text=f'🗓️ {config.WEDDING_DATE} 🗓️',
            font_size='24sp',
            color=(0.55, 0, 0.55, 1),  # Dark Magenta
            size_hint=(1, 0.07)
        )
        content_layout.add_widget(date_label)
        
        # Rotating message
        self.rotating_message = Label(
            text=messages.MAIN_WISHES[0],
            font_size='20sp',
            italic=True,
            color=(1, 0.08, 0.58, 1),
            size_hint=(1, 0.08)
        )
        content_layout.add_widget(self.rotating_message)
        
        # Personal message in scrollview
        scroll_view = ScrollView(
            size_hint=(1, 0.35),
            do_scroll_x=False
        )
        
        personal_msg = Label(
            text=messages.PERSONAL_MESSAGE.strip(),
            font_size='16sp',
            color=(0.55, 0, 0.55, 1),
            halign='center',
            valign='top',
            size_hint_y=None,
            markup=True
        )
        personal_msg.bind(texture_size=personal_msg.setter('size'))
        scroll_view.add_widget(personal_msg)
        content_layout.add_widget(scroll_view)
        
        # Blessing
        self.blessing_label = Label(
            text=messages.BLESSINGS[0],
            font_size='22sp',
            bold=True,
            color=(1, 0.41, 0.71, 1),  # Hot Pink
            size_hint=(1, 0.08)
        )
        content_layout.add_widget(self.blessing_label)
        
        # Emojis
        emoji_label = Label(
            text=messages.CELEBRATION_EMOJIS,
            font_size='28sp',
            size_hint=(1, 0.08)
        )
        content_layout.add_widget(emoji_label)
        
        main_layout.add_widget(content_layout)
        
        # Schedule message rotation
        Clock.schedule_interval(self.rotate_messages, 3)
        
        return main_layout
    
    def add_animated_background(self, layout):
        """Add animated sparkles to background"""
        # This will be drawn on the canvas
        with layout.canvas.before:
            Color(1, 0.94, 0.96, 1)
            Rectangle(pos=(0, 0), size=Window.size)
            
            # Add some decorative circles
            for _ in range(20):
                x = random.randint(0, int(Window.width))
                y = random.randint(0, int(Window.height))
                size = random.randint(3, 10)
                Color(1, 0.84, 0, random.uniform(0.2, 0.5))  # Gold with alpha
                Ellipse(pos=(x, y), size=(size, size))
    
    def pulse_animation(self, widget):
        """Create pulsing animation"""
        anim = Animation(font_size='45sp', duration=1) + Animation(font_size='40sp', duration=1)
        anim.repeat = True
        anim.start(widget)
    
    def rotate_messages(self, dt):
        """Rotate through messages"""
        self.message_index = (self.message_index + 1) % len(messages.MAIN_WISHES)
        self.rotating_message.text = messages.MAIN_WISHES[self.message_index]
        
        self.blessing_index = (self.blessing_index + 1) % len(messages.BLESSINGS)
        self.blessing_label.text = messages.BLESSINGS[self.blessing_index]


if __name__ == '__main__':
    WeddingWishApp().run()
