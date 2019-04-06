import csv

csv.register_dialect('myDialect',
delimiter = ',',
skipinitialspace=True)

counter = 0

with open('train.csv', 'r') as readFile:
    reader = csv.reader(readFile, dialect='myDialect')
    lines = list(reader)
    print(lines[1])
    finallist =[]
    for cell in lines[1]:
        avg = 0
        print(cell)
        numbers = cell.split('-')
        num1 = numbers[0]
        print(num1)
        num2 = numbers[1]
        print(num2)
        avg = (float(num1)+float(num2))/2
        print(avg)
        finallist.append(str(avg))
    print(finallist)
    lines[1] = finallist

with open('train.csv', 'w') as writeFile:
    writer = csv.writer(writeFile)
    writer.writerows(lines)

readFile.close()
writeFile.close()

"""for row in reader:
         if counter<4:
            print(row[0])
            list1 = row[0].split('-')
            num1 = list1[0]
            num2 = list1[1]
            avg = (int(num1)+int(num2)/2)

        counter+=1 """
