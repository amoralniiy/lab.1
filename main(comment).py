import csv
janrs=[]
janrs1=''#переменная для 4 задания
flag =0 #3 зад.
NumOfZapiz = -1
count =0
count1 =0
search = input("Искать: ")
f = open('result.txt', "w") #создает файл для записи
with open('books.csv', "r") as csvfile:
    table = csv.reader(csvfile, delimiter = ";") #разделение
    for row in list(table):
        fl1 = False  #Доп. задание
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
        NumOfZapiz +=1  #Первое задание
        lower_case = row[3].lower()#3 задние
        # print(lower_case)
        index = lower_case.find(search.lower()) #3 задание
        if len(row[1])>30: #2 задание
            count +=1
        if index != -1 and float(row[7].replace(',','.'))>200: #Проверка цены на условие >200 (3 задание)
            f.write(row[1]+'\n')
            print(row[1])
            flag = 1
        if 1<=count1<=21: #4 задание
            f.write(row[4] + '. ' + row[1] + '-' + row[6][:4] + '\n')
        count1+=1
    if flag == 0:
        f.write("Такого тут нет!!!" + '\n')
    f.write(str(NumOfZapiz)+ '\n')
    f.write(str(count))
    f.write(janrs1)
f.close()