def find_nulls(number):
    count = 0
    number = str(number)[::-1]
    for i in range(len(number)):
        if number[i] == '0':
            count += 1
        else:
            return count


f = open("СФ1.txt", 'r')
a = []
for el in f:
    a.append(int(el))
max_el = find_nulls((max(a)))
max_el = str(max_el)
result = open('result.txt', 'w')
result.write(max_el)
f.close()
result.close()