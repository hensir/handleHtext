with open("./过滤结构体/HCNetSDK.h","r") as f:
    fo = open("struct.cpp", "w",encoding="utf-8")
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
                fo.write("\n")  
                start = False
        except IndexError:
            pass
    fo.close()