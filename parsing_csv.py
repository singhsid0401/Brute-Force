import csv

csv.register_dialect('myDialect',
delimiter = ',',
skipinitialspace=True)

counter = 0

with open('train.csv', 'r') as readFile:
    reader = csv.reader(readFile, dialect='myDialect')
    lines = list(reader)
    #print(lines[1])
    finallist =[]
    for line in lines:
        for cell in line:
            avg = 0
            #print(cell)
            numbers = cell.split('-')
            print(numbers)
            num1 = numbers[0]
            print(num1)
            num2 = numbers[1]
            print(num2)
            avg = (float(num1)+float(num2))/2
            print(avg)
            finallist.append(str(avg))
        #print(finallist)
        line = finallist

with open('trains.csv', 'w') as writeFile:
    writer = csv.writer(writeFile)
    writer.writerows(lines)

readFile.close()
writeFile.close()

