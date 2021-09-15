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


---

# Function

## Ⅰ. List Fuction

### 1. len()

- gets the number of items in a list.
- You can also use len() on strings to return their length.

### 2. del keyword

- deletes elements from a list.
- > a = [1, 2, 3, 4, 5]  
del a[2:]  
*a = [1, 2]*

### 3. append()

- adds an element at the end of a list.
- you can add any data types.
- > a = [1, 2, 3, 4]  
a.append([5,6])  
*a= [1, 2, 3, 4, [5, 6]]*

### 4. sort()

- arranges the elements of a list in order.

### 5. reverse()

- turns out the elements of a list in reverse order.
- not sorting the elements in reverse order, just reversing.

### 6. index()

- index(x) => returns the index with x.
- if there is no value, error will occur.

### 7. insert()

- insert(a, b) => inserts b into a-th position.
- > a = [1, 2, 3]  
a.insert(0, 4)  
[4, 1, 2, 3]

### 8. remove()

- remove(x) => deletes the first x from a list.
- if there are multiple values, it deletes only the first one.

### 9. pop()

- pop() => returns the last element of a list and delete it.
- pop(x) => returns the x-th element one of a list and delete it.

### 10. count()

- returns the number of the elements in a list.
- count(x) => returns the number of the x elements in a list.

### 11. extend()

- adds a list into a list.
- extend(x) => x position is only list.
- > a = [1, 2, 3]  
a.extend([4, 5])  
*a = [1, 2, 3, 4, 5]*  
b = [6, 7]  
a.extend(b)  
*a = [1, 2, 3, 4, 5, 6, 7]*  

### 12. max(list)

- returns the maximum value.

### 13. min(list)

- returns the minimum value.

---

