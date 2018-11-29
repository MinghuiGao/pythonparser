
f = open("C:/Users/Administrator/Desktop/GraphForm.txt",'r',encoding='UTF-8')
line = f.readline()

#for eachline in f:
#    if 'public' in eachline:
#        eachline.strip()
#        print(eachline)
i = 0
unitsList = []
while line :
    if 'public' in line or 'private' in line or 'void' in line or 'protected' in line:
        if '(' in line:
            line = line.strip()
            print(i,"->"+line)
            # 获取到了字符串方法名 操作word文档，生成表格
            unit = Unit()
            unit.methodName = line[0:line.find(')')+1]
            unit.desc = ""
            #截取（）中的内容
            print("---------------",line.find('('))
            inputArgs = line[line.find('(')+1:line.find(')')]
            #print(inputArgs)
            t = inputArgs.split(',')
            unit.inputValue = t
            inputStr  = ""
            for arg in t:
                inputStr += arg.lstrip()+":\n"
            #print("====="+inputStr)
            if line.find("/") >= 0:
                unit.desc = line[line.find("/")+2:len(line)]
                #print("desc => " + unit.desc)
            unitsList.append(unit)

    line = f.readline()
    i = i+1
f.close()

# 将获取出的注释内容写到word中去
if unitsList != None:
    print("========================\n",len(unitsList))
    rowCount = len(unitsList) * 4

    doc = docx.Document()
    doc.add_heading(u'写入测试',0)

    # 遍历文件列表，依次增加表格
    # 没个文件，创建一个表格，表头上注明类名和描述
    table = doc.add_table(rows = rowCount+2,cols = 3)
    hcells0 = table.rows[0].cells
    hcells0[1].merge(hcells0[2])
    hcells0[0].text = "文件名"
    hcells0[1].text = "要获取的文件名"
    hcells1 = table.rows[1].cells
    hcells1[1].merge(hcells1[2])
    hcells[0].text = "描述"
    hcells[1].text = "要获取的文件描述"


    for i in range(len(unitsList)):
        cells0 = table.rows[(0 + i*4)+2].cells
        
        # TODO 添加方法序号（拼接字符串和整数）2.合并单元格。

        cells0[1].text = "名称："
        cells0[2].text = unitsList[i].methodName
        cells1 = table.rows[(1+i*4)+2].cells
        cells1[1].text = "功能："
        cells1[2].text = unitsList[i].desc
        cells2 = table.rows[(2+i*4)+1].cells
        cells2[1].text = "输入："
        input = ""
        for arg1 in unitsList[i].inputValue:
            input += arg1.lstrip()+" \n"
            print(i,"---"+ input)
        cells2[2].text = input
        cells3 = table.rows[(3+i*4)+2].cells
        cells3[1].text = "输出："
        cells3[2].text = unitsList[i].outputValue
        cells0[0].merge(cells3[0])
        cells0[0].text = "方法{0}".format(i)
        
    doc.save(u'test.docx')







    

#def writeUnitList2WordDocument():

