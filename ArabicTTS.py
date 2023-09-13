# from gtts import gTTS
import os
from tts import gTTS
text1 = "مرحبا بالعالم"
text="ما عملش حاجة تستحق الذكر"
tts = gTTS(text=text, lang='ar',slow=False)

tts.save("out.mp3")

os.system("mpg123 out.mp3")