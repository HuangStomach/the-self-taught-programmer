import sys
num = int(sys.argv[1])
if (num <= 10):
    print("<10")
elif (num > 10 and num <= 25):
    print("10 < num <= 25")
else:
    print(">25")