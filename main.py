import cv2
from src.video import *
from src.writer import *


async def main():
    name = '/run/media/znol/Seagate Bas/ProjectMephi/files/Теляковский.mp4'  # название файла лекции

    convertTime = datetime.now()
    convertToAudio(name, limit=1)  # разбиение на аудио дорожки
    print('Длительность конвертации:', datetime.now() - convertTime)

    robot = asyncio.create_task(writer('tmp'))  # распознавание текста
    await robot


if __name__ == '__main__':
    if not os.path.exists('tmp'):
        os.mkdir('tmp')
        os.mkdir('tmp/audio')
        os.mkdir('tmp/images')
        os.mkdir('tmp/video')

    startTime = datetime.now()
    asyncio.run(main())

    print('Длительность всей работы:', datetime.now() - startTime)
