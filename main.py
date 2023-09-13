# import pyttsx3

# # Initialize the text-to-speech engine
# engine = pyttsx3.init()

# # Set the language to Arabic
# engine.setProperty('voice', 'ar')

# # Get the text to be read
# text = "مرحبا بالعالم"

# # Say the text
# engine.say(text)
# # engine.save_to_file(text, "try.mp3")

# # Wait for the text to be spoken
# engine.runAndWait()

import pyttsx3

engine = pyttsx3.init()

for voice in engine.getProperty('voices'):
    print(voice)