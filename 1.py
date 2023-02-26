def strip_comments(strng, markers):
    a = strng.split("\n")
    l=[]
    for i in a:
        a1=''
        for j in i:
            if j in markers:
                break
            else:
                a1+=j
        l.append(a1.rstrip())
    return "\n".join(l)

print(strip_comments("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]))
