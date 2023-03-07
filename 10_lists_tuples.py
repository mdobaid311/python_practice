a = ['mohammed obaid', 22]
b = ["mohammed", "obaid", "saif"]
a.append("CSE")
print(a)
a.extend(b)
print(a)
a.insert(1, "obaid")
print(a)
a.remove("obaid")
print(a)
print(a.pop())
print(a)
print(a.pop(1))
print(a)
a.clear()
print(a)
a = ['mohammed obaid', 22]
print(a.index("mohammed obaid"))
print(a.index(22))
print(a.count("mohammed obaid"))
print(a.count(22))
print("**")
a = [25, 22]
a.sort()
print(a)
a.reverse()
print(a)
a = [25, 22]
b = a.copy()
print(b)
a = [25, 22]
b = a
print(b)
