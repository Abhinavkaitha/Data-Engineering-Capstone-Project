import os


my_path = '/mys3bucket/twitter_bz2'

count = 0
all_files = []
for dirpath, dirs, files in os.walk(my_path):
  for filename in files:
    fname = os.path.join(dirpath,filename)
    if fname.endswith('.bz2'):
        new_name = fname[25:].replace("/", "_")
        count += 1
        os.system("mv " + fname + " " + "/mys3bucket/twitter_bz2_dump/" + new_name)
        if count%1000 == 0:
            print("Number of files moved:", count)
