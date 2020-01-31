import os

def decompress(file):
    with open(file) as f:
        for file in f:
            file = file.rstrip("\n")
            os.system("mkdir /mys3bucket/twitter_bz2/{}".format(file[:-4]))
            os.system("tar -xvf /mys3bucket/twitter_dump/{} -C /mys3bucket/twitter_bz2/{}/".format(file,file[:-4]))

if __name__ == '__main__':
    decompress(file = "list_files.txt")