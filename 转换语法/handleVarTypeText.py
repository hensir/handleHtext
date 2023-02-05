# typedef struct _NET_DVR_AUDIODECInfo                     /* 信息 */
# {
#     int            nchans;                         /* 声道数 */
#     int            sample_rate;                  /* 采样率 */
#     int            aacdec_profile;               /* 编码用的框架 */
#     int            reserved[16];                 /* 保留 */
# } NET_DVR_AUDIODEC_INFO;
with open("./ori/struct.cpp","r") as f:
    

    fo = open("pybind.py","w",encoding="utf-8")
    start = False
    for line in f.readlines():
        word = line.split(" ")
        if word[0] == "typedef" and word[1] == "struct":        # 
            start = True
        if start == True:
            # print(line)
            fo.writelines(line)
        try:
            if word[0][0] == "}":
                start = False
        except IndexError:
            pass
    fo.close()


# 不要变量类型
# 要，结构体末尾第一个名字，结构体属性  就可以开始拼接了

structName = 123
structattr = 456

headText = f"pybind11::class_<{structName}>(m, \"{structName}\")"
midText1 = "    .def(pybind11::init())"
midText2 = f"    .def_readwrite(\"{structattr}\", &{structName}::{structattr})"
