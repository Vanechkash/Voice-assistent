import pyttsx3
engine = pyttsx3.init()
engine.say("система ассистирования активирована")
engine.runAndWait()

import speech_recognition as sr
for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))

r = sr.Recognizer()
with sr.Microphone(device_index=1) as source:
    print('скажи что-нибудь...')
    audio = r.listen(source)

query = r.recognize_google(audio, language="ru-RU")
print('Вы сказали: ' + query.lower())