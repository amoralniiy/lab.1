import csv
janrs=[]
janrs1=''
flag =0
NumOfZapiz = -1
count =0
count1 =0
search = input("Искать: ")
f = open('result.txt', "w")
with open('books.csv', "r") as csvfile:
    table = csv.reader(csvfile, delimiter = ";")
    for row in list(table):
        fl1 = False
        janre = ''
        for i in row[12]:
            if i == '#':
                if janre != '' and janre not in janrs and fl1 == True:
                    janrs.append(janre)
                    janrs1 += janre + '\n'
                janre = ''
                fl1 = True
            else:
                janre += i
        if janre != '' and janre not in janrs and fl1 == True:
            janrs.append(janre)
            janrs1 += janre + '\n'
            janre = ''
        NumOfZapiz +=1
        lower_case = row[3].lower()
        # print(lower_case)
        index = lower_case.find(search.lower())
        if len(row[1])>30:
            count +=1
        if index != -1 and float(row[7].replace(',','.'))>200: #Проверка цены на условие >200
            f.write(row[1]+'\n')
            print(row[1])
            flag = 1
        if 1<=count1<=21:
            f.write(row[4] + '. ' + row[1] + '-' + row[6][:4] + '\n')
        count1+=1
    if flag == 0:
        f.write("Такого тут нет!!!" + '\n')
    f.write(str(NumOfZapiz)+ '\n')
    f.write(str(count))
    f.write(janrs1)
f.close()