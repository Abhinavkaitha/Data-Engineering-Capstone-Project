import os

def download(file):
    with open(file) as f:
        for file in f:
            file = file.rstrip("\n")
            os.system("wget -O- 'https://archive.org/download/archiveteam-twitter-stream-2018-{}".format(file[13:15])+"/{}'".format(file)+"| aws s3 cp - s3://tone-of-the-nation/twitter_dump/{}".format(file))

if __name__ == '__main__':
    download(file = 'list_files.txt')