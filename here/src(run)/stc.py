import os

# ·作用：抽象信息对象：输入文件、脚本文件、输出文件、日志文件
# ·参数1：输入文件名
# ·参数2：脚本文件名
class STC_ELE:
    def __init__(self, input, script):
        # 声明
        self.input = input
        self.script = script
        self.output = ""
        self.log = ""

        # ...
        a = os.path.splitext(input)[0]
        b = os.path.splitext(script)[0]
        self.output =  a + "___" + b + ".json"
        self.log =  a + "___" + b + ".txt"
        return



# ·作用：输入一个根目录，根据目录下文件情况，创建STC
# ·参数1：目录
# ·API：get(),返回list
class STC:
    def __init__(self, root):
        # 声明
        self.__root_dir__ = root                 # 根目录
        self.__input_dir__ = root + "\\input"    # 输入目录
        self.__script_dir__ = root + "\\script"  # 脚本目录
        self.__ouput_dir__ = root + "\\output"   # 输出目录
        self.__log_dir__ = root + "\\log"        # 日志目录
        self.__list__ = []                       # 一个文件对应一个INFO

        # ...
        a = self.__get_file_list__(self.__input_dir__)
        b = self.__get_file_list__(self.__script_dir__)
        for k in a:
            for j in b:
                self.__list__.append(STC_ELE(k, j))
        return

    def __get_file_list__(self, d):
        l = []
        for k in os.listdir(d):
            l.append(k)
        return l

    def get(self):
        return self.__list__


# if(__name__=="__main__"):
#     path = r"C:\Users\HAHA\AndroidStudioProjects\IDA_SUTFF1"
#     l = STC(path).get()
#     k = 0