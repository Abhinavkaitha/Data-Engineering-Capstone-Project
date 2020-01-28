import os
import glob

# checking your current working directory
#print(os.getcwd())

# Get your current folder and subfolder event data
my_path = os.getcwd() + '/Downloads/twitter_bz2'

# Create a for loop to create a list of files and collect each filepath

all_files = []
for dirpath, dirs, files in os.walk(my_path):
  for filename in files:
    fname = os.path.join(dirpath,filename)
    if fname.endswith('.bz2'):
        all_files.append(fname)

print("Total Number of bz2 files: ", len(all_files))

for i in all_files:
    new_name = i[33:].replace("/", "_")
    os.system("mv "+ i + " "+"/Users/ark/Downloads/twitter_parquet/"+new_name)