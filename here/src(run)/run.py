import sys,os,subprocess

from clean import clean_outputlog
from idat import IDAT
from stc import STC

# xxx root_path libape.so getallfunc.py libape__getallfunc.json
# 父目录、输入文件名、IDAPY脚本名、输出文件名
# root create_idat_params.exe

if(__name__=="__main__"):
    # 根目录
    root = os.path.dirname(os.path.realpath(sys.argv[0]))
    #root = r"C:\Users\HAHA\AndroidStudioProjects\IDA_SUTFF122222"

    # 删除旧文件
    clean_outputlog(root)

    # 创建STC
    l = STC(root).get()

    # 遍历STC，调用IDAT
    cmd_list = []
    for k in l:
        bin    = k.input
        script = k.script
        result = k.output
        log    = k.log
        cmd = IDAT.get(root,bin,script,result,log)
        cmd_list.append(cmd)

    # 执行cmd
    for k in cmd_list:
        ret = subprocess.getoutput(k)

    # ...
    k = 0
    pass