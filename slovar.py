from module1 import *
eng_list=loe_failist("TextFile1.txt")
est_list=loe_failist("TextFile2.txt")
print(eng_list)
print(est_list)


while 1:
    print("a-translate fom estonian to english and vice versa,\ne-add to dictonary,\nr-change words pair,\nt-check your knowledge,\nc- pronounce words")
    valik=input("Your choice:")
    if valik.lower()=="a":
      word=input("Your word-")
      translate_list(eng_list,est_list,word)
    elif valik.lower()=="e":
       add(eng_list,est_list)
       est_list=loe_failist("TextFile2.txt")
       eng_list=loe_failist("TextFile1.txt")
    elif valik.lower()=="r":
        word=input("Your word-")
        change(eng_list,est_list,word)
    elif valik.lower()=="t":
        check(eng_list,est_list)
    elif valik.lower()=="c":
        input1=input(" choice eng/est:-")
        sonad="" 
        if input1.lower()=="eng":
                for sona in eng_list:
                    sonad=sonad+""+sona
                heli(sonad,'en')
        if input1.lower()=="est":
                for sona in est_list:
                    sonad=sonad+""+sona
                heli(sonad,'fi')