import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set the text to be spoken
text = "Hello! Welcome to the world of Python programming."

# Speak the text
engine.say(text)

# Wait for the speech to finish
engine.runAndWait()