from module1 import *
rus_list=loe_failist("TextFile1.txt")
est_list=loe_failist("TextFile2.txt")
print(rus_list)
print(est_list)
word=input("введите слово-")


while 1:
    print("a-перевод с английского языка на русский и с русского на английский,\ne-добавить слово в словарь,\nr-исправить слово,\nt-проверить знание слов из словаря")
    valik=input("Ваш выбор:")
    if valik.lower()=="a":
      translate_list(rus_list,est_list,word)
    elif valik.lower()=="e":
       rus_list,est_list=add(rus_list,est_list)
    elif valik.lower()=="r":
        change(rus_list,est_list,word)
    elif valik.lower()=="t":
        break