from googletrans import Translator
from gtts import gTTS
import playsound 
import tempfile
def ts(text):
	translator = Translator()
	translator_text = translator.translate(text, dest='zh-TW').text
	print(translator_text)
	return text

def speak(english):
    with tempfile.NamedTemporaryFile(delete=True) as fp:
        tts = gTTS(text=english, lang='en')
        tts.save('{}.mp3'.format(fp.name))
        playsound.playsound('{}.mp3'.format(fp.name))
def main():
	while True:
		text = input('請輸入要翻譯的字: ')
		if text == 'q':
			print('離開')
			break
		else:
			english = ts(text)
			speak(english)
main()

