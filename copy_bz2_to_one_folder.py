import os


my_path = '/mys3bucket/twitter_bz2'

# Create a for loop to create a list of all bz2 files and collect each filepath

all_files = []
for dirpath, dirs, files in os.walk(my_path):
  for filename in files:
    fname = os.path.join(dirpath,filename)
    if fname.endswith('.bz2'):
        all_files.append(fname)

print("Total Number of bz2 files: ", len(all_files))

for i in all_files:
    new_name = i[25:].replace("/", "_")
    os.system("mv "+ i + " "+"/mys3bucket/twitter_bz2_dump/"+new_name)
