names = ['Jhon', 'Bob', 'Mosh', 'Sarah']
print(names[-1])
print(names[1:3])
print(names)

matrix =[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(matrix[0][1])
for row in matrix:
    for item in row:
        print(item, end = " ")
    print()

numbers = [5,2,1,7,4]
numbers.append(20)
print(numbers)
numbers.insert(3,10)
print(numbers)
numbers.remove(2)
print(numbers)
numbers.pop()
print(numbers)
print(numbers.index(7))
print(numbers.count(10))
numbers.sort()
print(numbers)
numbers.reverse()