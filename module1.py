def translate_list(f,t,str):
    N=len(f)
    w=f.count(str)
    w2=t.count(str)
    if w or w2 ==0:
        add(f,t)
    elif w or w2!=0:
        for i in range(N):
            if f[i]== t[i] or t[i]==f[i]:
                print(f[i],"-->",t[i])
            elif f[i]!=t[i] or t[i]!=f[i]:
                print(" wrong")
      
def add(f,t):
    text2=input("напишите Слово на русском")
    with  open("TextFile1.txt",'a') as h:
           h.write("\n"+text2)
    text3=input("напишите Слово на estonian")
    with  open("TextFile2.txt",'a') as g:
                g.write("\n"+text3)
    return f and t

def loe_failist(f):
    fail=open(f,'r',encoding="utf-8-sig")
    mas=[] 
    for rida in fail:
        mas.append(rida.strip())
    fail.close()
    return mas
