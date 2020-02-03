import os


def copy_bz2_to_one_folder(my_path):
    count = 0
    folder = 1
    list_files = os.listdir(my_path)
    os.system('mkdir /mys3bucket/new_twitter/1')
    for fname in list_files:
        os.system("mv /mys3bucket/twitter_bz2_dump/" + fname + " " + "/mys3bucket/new_twitter/" + str(folder)+'/')
        count += 1
        print(count)
        if count%500 == 0:
            folder += 1
            os.system('mkdir /Users/ark/Desktop/test/'+str(folder))
if __name__ == '__main__':
    copy_bz2_to_one_folder(my_path = '/mys3bucket/twitter_bz2_dump')
