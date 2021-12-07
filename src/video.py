import cv2
import moviepy.editor as mp


def convertToAudio(filePath, limit=-1):
    video = mp.VideoFileClip(filePath)

    limit = int(video.duration + 1) if limit == -1 else 30 * limit + 1

    for k in range(0, limit, 30):
        last = k + 30 if k + 30 < video.duration else video.duration
        tmp_video = video.subclip(k, last)
        tmp_video.audio.write_audiofile(f'tmp/audio/audio{k}.wav')

        tmp_video = video.subclip(k, k + 1)
        tmp_video.write_videofile(f'tmp/video/video{k}.mp4', audio=False)
        ret, image = cv2.VideoCapture(f'tmp/video/video{k}.mp4').read()
        cv2.imwrite(f'tmp/images/image{k}.png', image)
    video.close()
