import os
with open("list_files.txt") as f:
    for file in f:
        file = file.rstrip("\n")
        #print("mkdir /mys3bucket/twitter_bz2/{}".format(file[:-4]))
        #print("tar -xvf /mys3bucket/twitter_dump/{} -C /mys3bucket/twitter_bz2/{}/".format(file,file[:-4]))
        os.system("mkdir /mys3bucket/twitter_bz2/{}".format(file[:-4]))
        os.system("wget -O- 'https://archive.org/download/archiveteam-twitter-stream-2018-{}".format(file[13:15])+"/{}'".format(file)+"| aws s3 cp - s3://tone-of-the-nation/twitter_dump/{}".format(file))