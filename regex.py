import re
loadedText=open("regex_sum_1546835.txt")
sumOfAllNumbers=0
for line in loadedText:
    numbers= re.findall('[0-9]+',line)
    for number in numbers:
        sumOfAllNumbers=sumOfAllNumbers+int(number)
print(sumOfAllNumbers)