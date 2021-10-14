f = open("test.txt", "w+")
f.write("999\n")
for i in range(1000):
    f.write(str(i) + "\n")