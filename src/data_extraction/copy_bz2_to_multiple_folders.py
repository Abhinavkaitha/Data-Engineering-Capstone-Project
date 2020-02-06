import os

def copy_bz2_to_one_folder(my_path):
    count = 0
    folder = 1
    os.system('mkdir /mys3bucket/new_twitter/1')
    for dirpath, dirs, files in os.walk(my_path):
      for filename in files:
        fname = os.path.join(dirpath,filename)
        if fname.endswith('.bz2'):
            new_name = fname[25:].replace("/", "_")
            count += 1
            print(count)
            os.system("mv " + fname + " " + "/mys3bucket/new_twitter/"+ str(folder) + "/"+new_name)
            if count % 500 == 0:
                folder += 1
                print("******** "+folder+" ********")
                os.system('mkdir /mys3bucket/new_twitter/' + str(folder))

if __name__ == '__main__':
    copy_bz2_to_one_folder(my_path = '/mys3bucket/twitter_bz2')