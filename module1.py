def translate_list(f,t,str):
    N=len(f)
    w=f.count(str)
    w2=t.count(str)
    if w==0 and w2 ==0:
       valikyes=input("No such  word , would you like to add it. please enter yes or no: ")
       if valikyes.lower()=="yes":
               add(f,t)
       elif valikyes.lower()=="no":
             quit() 
    elif w!=0 and w2!=0:
        for i in range(N):
            if str== t[i] or str==f[i]:
                print(f[i]," meaning-->",t[i])
    elif str!=t[i] or str!=f[i]:
       print(" wrong word")
      
def add(f,t):
    text2=input("напишите Слово на русском")
    with  open("TextFile1.txt",'a') as h:
           h.write("\n"+text2)
    text3=input(" write this word on estonian")
    with  open("TextFile2.txt",'a') as g:
                g.write("\n"+text3)
    return f and t

def change(f,t,str):
     w3=f.count(str)
     w4=t.count(str)
     if w3 >=1 or w4>=1:
        g = open("TextFile1.txt","r+")
        d = g.readlines()
        g.seek(0)
        c = open("TextFile2.txt","r+")
        h = c.readlines()
        c.seek(0)
        n=0
        for i in d :
            if i.rstrip('\n')!= str :
                g.write(i)
                g.truncate() 
            elif i.rstrip('\n')== str:
               n=d.index(i)
        g.close()
        print(n)
        for b in h:
            if h.index(b)!=n:
                c.write(b)
                c.truncate()        
        c.close()
        print("words were deleted")
        add(f,t)
     else:   
        p=input("no such word, would you like to add it yes/no:")
        if p.lower()=="yes":
              add(f,t)
        elif p.lower()=="no":
             quit() 
            


def loe_failist(f):
    fail=open(f,'r',encoding="utf-8-sig")
    mas=[] 
    for rida in fail:
        mas.append(rida.strip())
    fail.close()
    return mas
