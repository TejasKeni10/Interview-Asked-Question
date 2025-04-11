def Occur(stringg):
    occur={}
    for i in stringg:
        if i in occur:
            occur[i] +=1
        else:
            occur[i] = 1
    print(occur)

stringg = "hello"
Occur(stringg)