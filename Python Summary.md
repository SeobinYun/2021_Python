# List

## Ⅰ. Operations

### 1. in
- return: True or False
- > words = ["spam", "egg", "spam", sausage"]  
print("spam" in words)  
print("egg" in words)  
print("tomato" in words)

### 2. not 
- return : True or False
- > nums = [1, 2, 3]  
print(not 4 in nums)  
print(4 not in nums)  
print(not 3 in nums)  
print(3 not in nums)


---


## Ⅱ. Range

### 1. By default, it starts from 0, increments by 1 and stops before the specified number.
- > numbers = list(range(10))  
- result = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]



### 2. If it's called with two arguments, it'll produce values from the first to the second.
- > numbers= list(range(3, 8))
- result = [3, 4, 5, 6, 7]


### 3. If it's called with three arguments, it'll produce values from the first to the second stepping the third argument.
- > numbers = list(range(5, 20, 2))
- result = [5, 7, 9, 11, 13, 15, 17, 19]
- *we can also create a list of decreasing numbers, using a negative number as the third argument.*
- > list(range(20, 5, -2))


### 4. we can use range object in an for loop
- > for i in range(5)


---


## Ⅲ. Slices 

### 1. squares[a:b]
- > squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]  
print(squares[2:6]) // [4, 9, 16, 25]  
print(squares[3:8]) // [9, 16, 25, 36, 49]  
print(squares[0:1]) // [0]  

### 2. squares[:b] or squares[a:]
- If the first number in a slice is omitted, it's taken to be the start of the list.
- If the second number is omitted, it's taken to be the end.
- > squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]    
print(squares[:7]) // [0, 1, 4, 9, 16, 25, 36]  
print(squares[7:]) // [49, 64, 81]  

### 3. squares[::]
- a third number represents the step to include only alternate values in the slice.
- > squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]  
print(squares[::2]) // [0, 4, 16, 36, 64]  
print(squares[2:8:3]) // [4, 25]  

### 4. Negative
- > squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]  
print(squares[1:-1]) // 1, 4, 9, 16, 25, 36, 49, 64]  
