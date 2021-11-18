import random
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
    elif w!=0 or w2!=0:
        for il in range(len(f)):
            if str== t[il] or str==f[il]:
                print(f[il]," meaning-->",t[il])
      
def add(f,t):
    text2=input("write this on english:-")
    with  open("TextFile1.txt",'a') as h:
           h.write("\n"+text2)
    text3=input("write this word on estonian:-")
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
            
def check (f,t):
   correct=0
   wrong=0 
   procent=0
   for k in range (5):
    s=input(" choice eng/est:-")
    if s.lower()=="eng":
         x=random.choice(f)
         print(x)
         n2=0
         y_answer=input("Write your translation:-")
         for ine in f:
             if f.index(ine)==f.index(x):
                  n2=f.index(x)
         for  g in t:
            if t.index(g)==n2:
                 if t[n2]==y_answer:
                    print("correct")
                    print(t[n2])
                    correct+=1
                 else:
                    print("wrong")
                    print(y_answer,"-supposed to be-",t[n2])
                    wrong+=1
    elif s.lower()=="est":
         n3=0
         x1=random.choice(t)
         print(x1)
         y_answer1=input("Write your translation:-")
         for ined in t:
             if t.index(ined)==t.index(x1):
                  n3=t.index(x1)
         for  g1 in f:
            if f.index(g1)==n3:
                if f[n3]==y_answer1:
                    print("correct")
                    print(f[n3])
                    correct+=1
                else:
                    print("wrong")
                    print(y_answer1,"-supposed to be-",f[n3])
                    wrong+=1
   procent1=0
   procent=correct/5*100
   procent1=wrong/5*100
   if procent>0:
       print("correct answered",procent,"%")
       print("wrong answered",procent,"%")
   else:
       print("correct answered",0,"%")
       print("wrong answered",procent1,"%")

    



def loe_failist(f):
    fail=open(f,'r',encoding="utf-8-sig")
    mas=[] 
    for rida in fail:
        mas.append(rida.strip())
    fail.close()
    return mas
