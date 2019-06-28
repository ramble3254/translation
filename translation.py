from googletrans import Translator
from gtts import gTTS
import playsound 
import tempfile
import sys
def ts(text, translator_language):
	translator = Translator()
	translator_text = translator.translate(text, dest=translator_language).text
	print(translator_text)
	return translator_text

def speak(voice, voice_language):
    with tempfile.NamedTemporaryFile(delete=True) as fp:
        tts = gTTS(text=voice, lang=voice_language)
        tts.save('{}.mp3'.format(fp.name))
        playsound.playsound('{}.mp3'.format(fp.name))

def choose_language(translator_language):	
	if translator_language == '1':
		translator_language = 'zh-TW'
	elif translator_language == '2':
		translator_language = 'en'
	else:
		print('請輸入正確的選項')
		main()
	return translator_language

def choose_voice(voice_language):
	if voice_language == '1':
		voice_language = 'zh-TW'
	elif voice_language == '2':
		voice_language = 'en'
	return voice_language

def main():
	print('英翻中請輸入: 1', '中翻英輸入: 2', '離開請輸入: q')
	translator = input('請輸入: ')
	if translator == 'q':
		exit()
	else:
		translator_language = choose_language(translator)
		voice_language = choose_voice(translator)
		while True:
			text = input('請輸入要翻譯的字: ')
			if text == 'q':
				exit()
			else:
				voice = ts(text, translator_language)
				speak(voice, voice_language)

def exit():
	print('**離開**')
	sys.exit()
	
main()

