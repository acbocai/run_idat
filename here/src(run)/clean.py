import os,sys

def getfilelist_s(d,s):
    l1 = []
    l2 = []
    for parent, dirnames, filenames in os.walk(d, followlinks=True):
        for filename in filenames:
            file_path = os.path.join(parent, filename)
            t = os.path.splitext(file_path)
            if( t[1]== s):
                l1.append(file_path)
            else:
                l2.append(file_path)
    return l1,l2


def getfilelist_s(d,sl):
    l1 = []
    l2 = []
    for parent, dirnames, filenames in os.walk(d, followlinks=True):
        for filename in filenames:
            file_path = os.path.join(parent, filename)
            t = os.path.splitext(file_path)

            if(t[1] in sl):
                l1.append(file_path)
            else:
                l2.append(file_path)
    return l1,l2


def getfilelist(d):
    #l1 = []
    l2 = []
    for parent, dirnames, filenames in os.walk(d, followlinks=True):
        for filename in filenames:
            file_path = os.path.join(parent, filename)
            #l1.append(filename)
            l2.append(file_path)
    return l2


def deldir(d):
    if (not os.path.exists(d)):
        return False
    else:
        for k in getfilelist(d):
            os.remove(k)
        # os.removedirs(d)
        return True


def clean_outputlog(root):
    二进制目录 = root + "\\input\\"
    结果目录 = root + "\\output\\"
    日志目录 = root + "\\log\\"
    deldir(结果目录)
    deldir(日志目录)
    l1,l2 = getfilelist_s(二进制目录,[".so",".exe",".dll"])
    for k in l2:
        os.remove(k)
    k = 0

# if(__name__=="__main__"):
#     root = os.path.dirname(os.path.realpath(sys.argv[0]))
#     #root = r"C:\Users\HAHA\AndroidStudioProjects\IDA_SUTFF122222"
#     clean_outputlog(root)