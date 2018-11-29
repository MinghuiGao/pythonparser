import os


path1 = "C:/Users/Administrator/Desktop/ctc"

filelist = []
def gci(filepath):
    files = os.listdir(filepath)
    for fi in files:
        fi_d = os.path.join(filepath,fi)
        if os.path.isdir(fi_d):
            gci(fi_d)
        else:
            newfilepath = os.path.join(filepath,fi_d)
            # C:/Users/Administrator/Desktop/ctc\ZMSystem\ValidateAdminForm.resx
            if newfilepath.rfind('.cs') >= 0 or newfilepath.find('.txt') >=0:
                newfilepath = newfilepath.replace("\\","/")
                print(newfilepath + '\n')
                # 重命名文件名 .cs -> .txt
                txtNewFilePath = newfilepath.replace(".cs",".txt")
                os.rename(newfilepath,txtNewFilePath)
                filelist.append(txtNewFilePath)
    print("--->",len(filelist))
    return filelist

list = gci(path1)

print(list.count)


