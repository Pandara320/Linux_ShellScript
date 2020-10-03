import os

# Jake Pan
# script to split other files and take java files then rename them


class JavaRename:
    def __init__(self):
        self.path = 'C:\\general\\script\\renameFiles\\leetcode-master-testing\\easy\\'
        print("目标路径:" + str(self.path))

    def rename(self):
        file_list = os.listdir(self.path)
        print("目录文件列表:" + str(file_list))
        n = 0
        for item in file_list:
            if '.java' in item:
                first_three_digit = item[0:3]
                no_digit_name = item[3:]
                # os.rename(src, dst)
                # src = path + filename 旧文件路径+名字
                # dst = path + new_filename
                old_name = self.path + os.sep + file_list[n]
                new_name = self.path + os.sep + '0' + first_three_digit + '-' + no_digit_name
                os.rename(old_name, new_name)
                n = n+1
                print("This is old_name:   "+str(old_name))
                print("This is new_name:   "+str(new_name))
                print('''''')


if __name__ == '__main__':
    newName_java = JavaRename()
    newName_java.rename()


