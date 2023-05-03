def balancedBrackets(string):
    s = []
    m = dict()
    m[")"] = "("
    m["}"] = "{"
    m["]"] = "["
    for c in string:
        if len(s)>0 and c in m and s[-1]==m[c]:
            s.pop()
        elif c in "{[()]}":
            s.append(c)
    return len(s)==0

assert balancedBrackets("([])(){}(())()()")==True

