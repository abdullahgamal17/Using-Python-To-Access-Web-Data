import re
string_nums = list()
f = open("regex_sum_1357653.txt","r")
text = f.readlines()
for i in text:
    x = re.findall("[0-9]+",i)
    string_nums.extend(x)
sum = 0
for i in string_nums:
    sum += int(i)

print(sum)