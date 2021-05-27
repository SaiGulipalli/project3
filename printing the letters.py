def mostfrequent(word):
    l = list(word)
    d = {}
    

    for e in l:
        if e in d:
            d[e] += 1
        else:
            d[e] = 1
    
    
    dl = set(d.values())
    for i in range(len(dl)):
       
        max_ = max(dl)
        for k, v in d.items():
            if v == max_:
                print(k, '=', v)
        dl.remove(max_)

word = str(input('Please enter a string :'))
mostfrequent(word)

'''
output
Please enter a string :mississippi
i = 4
s = 4
p = 2
m = 1

'''
