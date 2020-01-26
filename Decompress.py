import os
with open("list_files.txt") as f:
    for file in f:
        file = file.rstrip("\n")
        os.system("mkdir /mys3bucket/twitter_bz2/{}".format(file[:-4]))
        os.system("tar -xvf /mys3bucket/twitter_dump/{} -C /mys3bucket/twitter_bz2/{}/".format(file,file[:-4]))