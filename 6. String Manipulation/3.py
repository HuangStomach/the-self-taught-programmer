str = "aldous Huxley was born in 1894"
ss = str.split(" ")
ss[0] = ss[0].capitalize()
str = " ".join(ss)

print(str)