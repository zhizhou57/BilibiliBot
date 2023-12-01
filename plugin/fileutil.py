import os
import sys


class FileUtil:
    # 全局储存目录
    storage_path = os.path.join(os.getcwd(), "data")
    system_name = sys.platform

    def __init__(self):
        pass

    def write(self, file_path, file_name, msg):
        # 去除首位空格
        path = os.path.join(self.storage_path, str(file_path))
        isExists = os.path.exists(path)
        if isExists:
            with open(os.path.join(path,file_name), "w+", encoding="utf-8") as file:
                file.write(msg)
        else:
            # 创建多文件夹 创建自定义目录则 -> mkdir
            os.makedirs(path)
            with open(os.path.join(path,file_name), "w+", encoding="utf-8") as file:
                file.write(msg)


    def read(self, file_path, file_name):
        path = os.path.join(self.storage_path, str(file_path))
        # 判断文件夹是否存在
        isExists = os.path.exists(path)
        if isExists:
            # 判断文件是否存在
            if os.path.exists(os.path.join(path, file_name)):
                with open(os.path.join(path, file_name), "r", encoding="utf-8") as file:
                    msg = file.read()
                    print(msg)
                    if msg == "":
                        return 'null'
                    else:
                        return msg
            else:
                return 'null'
        else:
            return 'null'
