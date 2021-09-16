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

## Ⅱ. String Function

### 1. format()

- enables values to be embedded in it, using placeholders.
- > nums = [4, 5, 6]  
- msg = "Numbers: {0} {1} {2}".format(nums[0], nums[1], nums[2])  

### 2. count()

- counts the number of characters.
- > a = "hobby"  
a.count('b') => 2

### 3. find()

- returns the first index of the string you're looking for.
- if there is no the string you're looking for, it returns -1.
- > a = "Python is the best choice"  
a.find('b')  => 14  
a.find('k')  => -1  

### 4. index()

- similar with find().
- However, if there is no the string you're looking for, it occurs error.

### 5. join()

- joins a list of string with another string as a seperator.
- > ",".join('abcd')  
'a,b,c,d'

### 6. upper()

- converts lowercase letters into uppercase letters.

### 7. lower()

- converts uppercase letters into lowercase letters.

### 8. lstrip()

- deletes spaces on the left.
- > a = " hi "  
a.lstrip()  
'hi '

### 9. rstrip()

- deletes spaces on the right.

### 10. strip()

- deletes spaces on both sides.

### 11. replace()

- replaces one substring in a string with another
- > a = "Life is too short"  
a.replace("Life", "Your leg")  
'Your leg is too short'

### 12. split()

- The opposite of join, turns a string with a certain separator into a list.
- Separated strings are returned as a list.
- > a = "Life is too short"  
a.split()  <= separates with space  
['Life', 'is', 'too', 'short']  
- > b = "a:b:c:d"  
b.split(':')  <= seperates with ':'  
['a', 'b', 'c', 'd']

### 13. startswith() endswith()

- determine if there is a substring at the start and end of a string, respectively.
- return : True or False
- > print("This is a sentence.".startswith("This"))  
True


---


# Tuple

## Ⅰ. definition

- covered with () and can skip it.
- cannot change values.
- You have to add comma(,) if tuple has only one element.
- > t1 = ()  
t2 = (1,)  
t3 = (1, 2, 3)  
t4 = 1, 2, 3  
t5 = ('a', 'b', ('ab', 'cd'))  


---


# Dictionary

## Ⅰ. definition

- Associative array or Hash
- {Key1:Value1, Key2:Value2, Key3:Value3, ...}

## Ⅱ. function

1. add dictionary key-value pair
> a = {1:'a'}  
> a[2] = 'b'  
> a = {1:'a', 2:'b'}

2. delete dictionary key-value pair
> del a[1]  
> // key가 1인 key:value 쌍 삭제

3. get value using key
> grade = {'pey': 10, 'julliet': 99}  
> grade['pey'] // 10

4. keys()
- key만을 모아서 dict keys 객체 반환
- 리스트처럼 사용가능, 하지만 리스트 관련 함수(append, insert, pop 등)는 사용 불가능
- > a = {'name':'pey','phone':'0119993323', 'birth':'1118'}  
a.keys() // dict_keys(['name', 'phone', 'birth'])  
- > for k in a.keys():  
  print(k)  
  name  
  phone  
  birth
- dict_keys 객체를 리스트로 변환
- > list(a.keys())  
['name', 'phone', 'birth']

5. values()
- value만을 모아서 dict_values 객체 반환
- > a.values() // dict_values(['pey', '0119993323', '1118'])

6. items()
- key와 value의 쌍을 튜플로 묶은 값을 모아서 dic_items 객체 반환
- > a.items() // dict_items([('name':'pey'), ('phone':'0119993323'), ('birth':'1118')])

7. clear()
- delete all elements in a dictionary
- empty dictionary : {}

8. in
- check whether the key is in a dictionary
- If the key is in a dictionary, it returns True.
- If the key isn't in a dictionary, it returns False. 
- > 'name' in a // True

9. get()
- key에 대응되는 value() 반환
- > a.get('name') // 'pey'
- 존재하지 않은 키 사용 시 None 반환
- Key값이 없을 경우, default 값을 대신 반환하도록 지정 가능
- > a.get('foo', 'bar') // 'bar'

