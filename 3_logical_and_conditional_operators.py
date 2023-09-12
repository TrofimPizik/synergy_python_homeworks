# Задание №1
a = int(input("Введите число, и нажмите Enter "))

if ((a%2) != 0) and ((a/2)>0):
    print("положительное нечетное число")
if (a%2 == 0) and ((a/2)>0):
    print("положительное четное число")
elif (a%2 == 0) and ((a/2)<0):
    print("отрицательное четное число")
elif (a%2 != 0) and ((a/2)<0):
    print("отрицательное нечетное число")
elif (a/2 == 0):
    print("нулевое число")


# Задание №2
slovo = input('Введите слово с гласными буквами: ')
eg=slovo.count('e') # считает количество гласных e
ag=slovo.count('a') # считает количество гласных a
ig=slovo.count('i') # считает количество гласных i
ug=slovo.count('u') # считает количество гласных u
og=slovo.count('o') # считает количество гласных o
schetglas=eg+ag+ig+ug+og # суммирует гласные

print("всего гласных",schetglas) #выводит количество гласных
print("всего согласных",len(slovo)-schetglas)  # считает сколько букв в слове и минусует от общего количества букв гласные, выводит количество согласных

if (eg==0):
    print ("гласной e в слове False")
else:
    print("e=",eg)

if (ug==0):
    print ("гласной u в слове False")
else:
    print("u=",ug)

if (og==0):
    print ("гласной o в слове False")
else:
    print("o=",og)

if (ag==0):
    print ("гласной a в слове False")
else:
    print("a=",ag)

if (ig==0):
    print ("гласной i в слове False")
else:
    print("i=",ig)


#Задание №3
summa=int(input("Минимальная сумма инвестиций - "))
maikl=int(input("Cколько долларов у Майкла - "))
ivan=int(input("Сколько долларов у Ивана - "))

if (maikl>=summa) and (ivan>=summa):
    print(2)
elif (maikl>=summa) and (ivan<=summa):
    print("Mike")
elif (maikl<=summa) and (ivan>=summa):
    print("Ivan")
elif (maikl<=summa) and (ivan<=summa) and ((maikl+ivan)>=summa):
    print(1)
elif (maikl<=summa) and (ivan<=summa) and ((maikl+ivan)<=summa):
    print(0)