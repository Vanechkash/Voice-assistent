import os
import time
import speech_recognition as sr
from fuzzywuzzy import fuzz
import pyttsx3
import datetime


opts = {
    "alias": ('глэдис'),
    "tbr": ('скажи', 'расскажи', 'сколько', 'покажи', 'включи', 'пожалуйста'),
    "cmds": {
        "ctime": ('текущее время', 'сейчас времени', 'времени', 'время', 'сейчас время', 'сейчас часов', 'который час'),
        "music": ('включи музыку', 'поставь музыку', 'музыка', 'музыкальная пауза', 'поставь что-нибудь'),
        "joke": ('расскажи анекдот', 'шутка', 'пошути', 'юморни', 'шуткани', 'расскажи прикол', 'ты знаешь анкдот', 'ты знаешь шутки', 'рассмеши меня', 'повесели меня'),
        "musicoff": ('выключи музыку', 'останови музыку', 'отключи музыку')
    }
}

# функции
def speak(what):
    print(what)
    speak_engine.say(what)
    speak_engine.runAndWait()
    speak_engine.stop()

def callback(recognizer, audio):
    try:
        voice = recognizer.recognize_google(audio, language="ru-RU").lower()
        print("[log] Распознано: " + voice)

        if voice.startswith(opts["alias"]):
            # обращаются к Ассистенту
            cmd = voice

            for x in opts['alias']:
                cmd = cmd.replace(x, "").strip()

            for x in opts['tbr']:
                cmd = cmd.replace(x, "").strip()

            # распознаем и выполняем команду
            cmd = recognize_cmd(cmd)
            execute_cmd(cmd['cmd'])

    except sr.UnknownValueError:
        print("[log] Голос не распознан!")

def recognize_cmd(cmd):
    RC = {'cmd': '', 'percent': 0}
    for c, v in opts['cmds'].items():

        for x in v:
            vrt = fuzz.ratio(cmd, x)
            if vrt > RC['percent']:
                RC['cmd'] = c
                RC['percent'] = vrt

    return RC

def execute_cmd(cmd):
    if cmd == 'ctime':
        # сказать текущее время
        now = datetime.datetime.now()
        speak("Сейчас " + str(now.hour) + ":" + str(now.minute))

    elif cmd == 'music':
        # воспроизвести музыку
        player.play()

    elif cmd == 'musicoff':
        # отключить музыку
        player.stop()

    elif cmd == 'stupid1':
        # рассказать анекдот
        speak("Я серьёзная девушка")

    else:
        print('Команда не распознана, повторите!')

# запуск

r = sr.Recognizer()
m = sr.Microphone(device_index=1)

with m as source:
    r.adjust_for_ambient_noise(source)

speak_engine = pyttsx3.init()

speak("Здравствуйте, меня зовут Глэдис")

stop_listening = r.listen_in_background(m, callback)
while True: time.sleep(0.1) # infinity loop
