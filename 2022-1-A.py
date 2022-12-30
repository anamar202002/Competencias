def letras(i:str, p:str):
    
    if len(p)<len(i): return "IMPOSSIBLE"
    c=i
    ini=0
    inp=0
    while ini<len(i) and inp<len(p):
        if i[ini] == p[inp]:
            ini+=1
            inp+=1
        else:
            inp+=1
    if ini!=len(i):
        return "IMPOSSIBLE"
    else:
        return len(p)-len(i)


    """ if len(p)<len(i): return "IMPOSSIBLE"
    else:
        for j in i:
            for k in p:
                if j==k:
                    c=c.replace(j, '',1)
                    p=p.replace(j, '',1)
                    break
                    
    
    if len(c)==0: return len(p)
    else: return "IMPOSSIBLE" """


if __name__ == '__main__':    
    t = int(input().strip())
    
    for j in range(t):
        i = str(input().strip())
        p = str(input().strip())
        print(("Case #"+str(j+1)+":"), letras(i,p))
