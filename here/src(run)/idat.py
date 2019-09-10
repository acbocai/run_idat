import sys,os

class IDAT:
    # ·作用：拼接出IDAT.EXE使用的的命令字符串
    # ·参数1：父级目录
    # ·参数2：二进制文件名
    # ·参数3：脚本文件名
    # ·参数4：输出文件名
    # .参数5：日志文件名
    # ·返回值：str cmd
    # ·使用前提：
    # 根目录下创建了IDA_Pro_v7.0_Portable、intput、output、script、log文件夹
    # 并且so文件存在于intput下，脚本文件存在于script文件夹下，idat完整程序在IDA_Pro_v7.0_Portable下
    # 举例：root_path libape.so getallfunc.py libape__getallfunc.json libape__getallfunc.txt
    @staticmethod
    def get(root,bin,script,result,log):
        根目录 = root
        IDA可执行文件名 = 根目录 + "\\IDA_Pro_v7.0_Portable\\idat.exe"
        二进制文件名 = 根目录 + "\\input\\"  + bin
        脚本文件名   = 根目录 + "\\script\\" + script
        结果文件名   = 根目录 + "\\output\\" + result
        日志文件名   = 根目录 + "\\log\\" + log
        p1 = IDA可执行文件名
        p2 = " -A"
        p3 = " -L" + "\"" + 日志文件名 + "\""
        p4 = " -S" + "\"" + 脚本文件名
        p5 = " " + 结果文件名 + "\""
        p6 = " " + 二进制文件名
        cmd = p1 + p2 + p3 + p4 + p5 + p6
        return cmd

    # ·作用：通过命令行传参调用get
    # ·参数1：sys.argv
    # ·返回值：str cmd
    @staticmethod
    def exe(sys_argv):
        if (6 != len(sys.argv)):
            print("6 !=sys.argv.count(),fail.")
            return ""
        else:
            root = sys.argv[1]
            bin = sys.argv[2]
            script = sys.argv[3]
            result = sys.argv[4]
            log = sys.argv[5]
            return IDAT.get(root, bin, script, result,log)

# if(__name__=="__main__"):
#     cmd = IDAT.exe(sys.argv)
#     print(cmd)