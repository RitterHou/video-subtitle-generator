import os

from backend.main import SubtitleGenerator

root = 'E:/'

if __name__ == '__main__':
    files = list(map(lambda f: root + f, filter(lambda f: f.endswith('.mp4'), os.listdir(root))))
    for file in files:
        print(file)
        sg = SubtitleGenerator(file, language='zh-cn')
        ret = sg.run(concurrency=1)
