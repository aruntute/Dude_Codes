#Assignment2 Part1

x = int(input('Enter any number: '))
if x % 2 == 0:
    print(x, 'is an  even number.')
else:
    print(x, 'is an odd number.')


#Part 2
# sum of numbers between 1 and 50
x = 0
for i in range(1,51):
    x = x+i
print('The sum of numbers from 1 to 50 is: ', x)
