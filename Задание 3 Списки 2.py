f = open('СФ2.txt', 'r')
a = []
for el in f:
    a.append(el)
b = [a.count(x) for x in a]
for i in a:
    if a.count(i) == max(b):
        print(i)
        break
