# coding=UTF-8
import sys
import idc
import idaapi
import idautils

def save_json(path,content):
    with open(path, 'w+') as f:
        json.dump(fp=f, obj=content)
        return

def get_all_func():
    num = 0
    content = []
    for func in idautils.Functions():
        seg_perm = idc.get_segm_attr(func,SEGATTR_PERM)         # 段属性
        if(5 !=seg_perm):
            continue
        seg_name = idc.get_segm_name(func)                      # 段名
        if(".plt" == seg_name):
            continue
        
        func_name = idc.get_func_name(func)                     # 函数名
        func_flags = hex(idc.get_func_attr(func,FUNCATTR_FLAGS))# 函数信息
        func_head = hex(idc.get_func_attr(func,FUNCATTR_START)) # 函数头
        func_end = hex(idc.get_func_attr(func,FUNCATTR_END))    # 函数尾

        l = []
        l.append(num)
        l.append(seg_name)
        l.append(seg_perm)
        l.append(func_name)
        l.append(func_flags)
        l.append(func_head)
        l.append(func_end)
        content.append(l)
        
        num += 1
        #print(l)
    return content
        
# 程序入口
idaapi.autoWait()

path = idc.ARGV[1]
content = get_all_func()
save_json(path,content)
print("haha")

idc.Exit(0)