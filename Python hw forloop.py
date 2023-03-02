numbers = open('numbers.txt', 'r')
runs = 1
for line in numbers:
    amount = float(line)
    print(f'{amount:.2f}')
    while runs == 1:
        y = amount
        runs += 1
    y += y
    print (y)
print (int(y) / 3)



            
        
