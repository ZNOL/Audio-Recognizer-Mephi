from src.speech import *


async def writer(filePath):
    recognizerTime = datetime.now()
    ans = await old_recognition(filePath)
    print('Время распознования:', datetime.now() - recognizerTime)

    with open('ans.txt', 'w', encoding='utf-8') as file:
        file.write(ans)
