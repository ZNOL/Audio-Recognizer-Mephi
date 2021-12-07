import os
import asyncio
from src.images import *
from datetime import datetime
import speech_recognition as sr


ans = ''


async def part_recognition(mainPath, filename):
    global ans
    r = sr.Recognizer()

    with sr.AudioFile(f'{mainPath}/{filename}') as source:
        audio = r.record(source)
        try:
            result = r.recognize_google(audio, language="ru")
            ans += f'{result}\n'
        except sr.UnknownValueError:
            print('Неизвестная ошибка')
        except sr.RequestError as e:
            print(f"Ошибка: {e}")


async def recognition(mainPath):
    global ans
    ans = ''
    for filename in os.listdir(mainPath):
        new_task = asyncio.create_task(part_recognition(mainPath, filename))
        await new_task


async def old_recognition(mainPath):
    ans = ''

    r = sr.Recognizer()
    audioPath = mainPath + '/audio'

    files = sorted(list(os.listdir(audioPath)), key=lambda x: int(x.split('.')[0][5:]))
    print(files)
    for filename in files:
        idx = int(filename.split('.')[0][5:])
        print('!', idx)
        with sr.AudioFile(f'{audioPath}/{filename}') as source:
            audio = r.record(source)
            try:
                result = r.recognize_google(audio, language="ru")
                speaker = image_processing(mainPath + f'/images/image{idx}.png')
                ans += f'{speaker}: {result}\n'
            except sr.UnknownValueError:
                print('Неизвестная ошибка')
            except sr.RequestError as e:
                print(f"Ошибка: {e}")

    return ans
