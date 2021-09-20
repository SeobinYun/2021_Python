# List

## Ⅰ. Operations

### 1. in
- return: True or False
```
words = ["spam", "egg", "spam", sausage"]  
print("spam" in words)  
print("egg" in words)  
print("tomato" in words)
```

### 2. not 
- return : True or False
```
nums = [1, 2, 3]  
print(not 4 in nums)  
print(4 not in nums)  
print(not 3 in nums)  
print(3 not in nums)
```

---


## Ⅱ. Range

### 1. By default, it starts from 0, increments by 1 and stops before the specified number.
```
numbers = list(range(10))  
// result = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```


### 2. If it's called with two arguments, it'll produce values from the first to the second.
```
numbers= list(range(3, 8))
// result = [3, 4, 5, 6, 7]
```

### 3. If it's called with three arguments, it'll produce values from the first to the second stepping the third argument.
```
numbers = list(range(5, 20, 2))
// result = [5, 7, 9, 11, 13, 15, 17, 19]
```
- *we can also create a list of decreasing numbers, using a negative number as the third argument.*
```
list(range(20, 5, -2))
```

### 4. we can use range object in an for loop
```
for i in range(5)
```

---


## Ⅲ. Slices 

### 1. squares[a:b]
```
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]  
print(squares[2:6]) // [4, 9, 16, 25]  
print(squares[3:8]) // [9, 16, 25, 36, 49]  
print(squares[0:1]) // [0]  
```

### 2. squares[:b] or squares[a:]
- If the first number in a slice is omitted, it's taken to be the start of the list.
- If the second number is omitted, it's taken to be the end.
```
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]    
print(squares[:7]) // [0, 1, 4, 9, 16, 25, 36]  
print(squares[7:]) // [49, 64, 81]  
```

### 3. squares[::]
- a third number represents the step to include only alternate values in the slice.
```
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]  
print(squares[::2]) // [0, 4, 16, 36, 64]  
print(squares[2:8:3]) // [4, 25]  
```

### 4. Negative
```
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]  
print(squares[1:-1]) // 1, 4, 9, 16, 25, 36, 49, 64]  
```

---

# Function

## Ⅰ. List Fuction

### 1. len()

- gets the number of items in a list.
- You can also use len() on strings to return their length.

### 2. del keyword

- deletes elements from a list.
```
a = [1, 2, 3, 4, 5]  
del a[2:]  
// a = [1, 2]
```

### 3. append()

- adds an element at the end of a list.
- you can add any data types.
```
a = [1, 2, 3, 4]  
a.append([5,6])  
// a= [1, 2, 3, 4, [5, 6]]
```

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
```
a = [1, 2, 3]  
a.insert(0, 4)  
[4, 1, 2, 3]
```

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
```
a = [1, 2, 3]  
a.extend([4, 5])  
a = [1, 2, 3, 4, 5]  
b = [6, 7]  
a.extend(b)  
// a = [1, 2, 3, 4, 5, 6, 7]  
```

### 12. max(list)

- returns the maximum value.

### 13. min(list)

- returns the minimum value.

---

## Ⅱ. String Function

### 1. format()

- enables values to be embedded in it, using placeholders.
```
nums = [4, 5, 6]  
msg = "Numbers: {0} {1} {2}".format(nums[0], nums[1], nums[2])  
```

### 2. count()

- counts the number of characters.
```
a = "hobby"  
a.count('b') => 2
```

### 3. find()

- returns the first index of the string you're looking for.
- if there is no the string you're looking for, it returns -1.
```
a = "Python is the best choice"  
a.find('b')  => 14  
a.find('k')  => -1  
```

### 4. index()

- similar with find().
- However, if there is no the string you're looking for, it occurs error.

### 5. join()

- joins a list of string with another string as a seperator.
```
",".join('abcd')  
'a,b,c,d'
```

### 6. upper()

- converts lowercase letters into uppercase letters.

### 7. lower()

- converts uppercase letters into lowercase letters.

### 8. lstrip()

- deletes spaces on the left.
```
a = " hi "  
a.lstrip()  
'hi '
```

### 9. rstrip()

- deletes spaces on the right.

### 10. strip()

- deletes spaces on both sides.

### 11. replace()

- replaces one substring in a string with another
```
a = "Life is too short"  
a.replace("Life", "Your leg")  
'Your leg is too short'
```

### 12. split()

- The opposite of join, turns a string with a certain separator into a list.
- Separated strings are returned as a list.
```
a = "Life is too short"  
a.split()  <= separates with space  
['Life', 'is', 'too', 'short']  
```
```
b = "a:b:c:d"  
b.split(':')  <= seperates with ':'  
['a', 'b', 'c', 'd']
```

### 13. startswith() endswith()

- determine if there is a substring at the start and end of a string, respectively.
- return : True or False
```
print("This is a sentence.".startswith("This"))  
True
```

---


# Tuple

## Ⅰ. definition

- covered with () and can skip it.
- cannot change values.
- You have to add comma(,) if tuple has only one element.
```
t1 = ()  
t2 = (1,)  
t3 = (1, 2, 3)  
t4 = 1, 2, 3  
t5 = ('a', 'b', ('ab', 'cd'))  
```

---


# Dictionary

## Ⅰ. definition

- Associative array or Hash
- {Key1:Value1, Key2:Value2, Key3:Value3, ...}

## Ⅱ. function

### 1. add dictionary key-value pair
```
a = {1:'a'}  
a[2] = 'b'  
a = {1:'a', 2:'b'}
```

### 2. delete dictionary key-value pair
```
del a[1]  
// key가 1인 key:value 쌍 삭제
```

### 3. get value using key
```
grade = {'pey': 10, 'julliet': 99}  
grade['pey'] // 10
```

### 4. keys()
- key만을 모아서 dict keys 객체 반환
- 리스트처럼 사용가능, 하지만 리스트 관련 함수(append, insert, pop 등)는 사용 불가능
```
a = {'name':'pey','phone':'0119993323', 'birth':'1118'}  
a.keys() 
// dict_keys(['name', 'phone', 'birth'])  
```
```
for k in a.keys():  
  print(k)  
  name  
  phone  
  birth
```
- dict_keys 객체를 리스트로 변환
```
list(a.keys())  
['name', 'phone', 'birth']
```
### 5. values()
- value만을 모아서 dict_values 객체 반환
```
a.values() 
// dict_values(['pey', '0119993323', '1118'])
```

### 6. items()
- key와 value의 쌍을 튜플로 묶은 값을 모아서 dic_items 객체 반환
```
a.items() 
// dict_items([('name':'pey'), ('phone':'0119993323'), ('birth':'1118')])
```

### 7. clear()
- delete all elements in a dictionary
- empty dictionary : {}

### 8. in
- check whether the key is in a dictionary
- If the key is in a dictionary, it returns True.
- If the key isn't in a dictionary, it returns False. 
```
'name' in a 
// True
```

### 9. get()
- key에 대응되는 value() 반환
```
a.get('name') 
// 'pey'
```
- 존재하지 않은 키 사용 시 None 반환
- Key값이 없을 경우, default 값을 대신 반환하도록 지정 가능
```
a.get('foo', 'bar') 
// 'bar'
```

---


# Set

## Ⅰ. properties

- not allow duplication
- unordered
- set 자료형은 순서가 없기 떄문에 인덱싱 사용 불가
- 인덱싱 할려면 list or tuple로 변환 필요
```
s1 = set([1,2,3])  
l1 = list(s1)  
l1 // [1, 2, 3]
```
```
t1 = tuple(s1)  
t1 
// (1, 2, 3)
```

## Ⅱ

### 1. intersection

- & or intersection()
```
s1 & s2
s1.intersection(s2)
```

### 2. union

- | or union()
```
s1 | s2
s1.union(s2)  
```

### 3. difference set

- - or difference()
```
s1 - s2
s1.difference(s2)
```

## Ⅲ. function

### 1. add()

### 2. update()

- 여러 개의 값을 한꺼번에 추가
```
s1 = set([1, 2, 3])  
s1.update([4, 5, 6])
```

### 3. remove()


---


# Bool

- True or False
- type()
```
a = True  
type(a) 
// <class 'bool'>
```
- bool()
```
bool('python') 
// True
```

## True and False of data types

|data type|value|T or F|
|---|---|---|
|String|"python"|True|
||""|False|
|List|[1, 2, 3]|True|
||[]|False|
|Tuple|()|False|
|Dictionary|{}|False|
|Number|0이 아닌 숫자|True|
||0|False|
||None|False|


---


# File

## Ⅰ. open()

- 파일 객체 = open(파일 이름, 파일 열기모드)

|파일 열기 모드| |  
|---|---|  
|r|읽기 모드 - 파일을 읽기만 할 때 사용|  
|w|쓰기 모드 - 파일에 내용을 쓸 때 사용|  
|a|추가 모드 - 파일의 마지막에 새로운 내용을 추가할 때 사용  
- w로 열면 해당 파일이 이미 존재할 경우 원래 있던 내용이 모두 사라지고, 해당 파일이 존재하지 않으면 새로운 파일이 생성됨
```
f = open("ex.txt", 'w')  
f.close()
```

## Ⅱ. readline()

- 파일의 첫 번째 줄을 읽어 출력
- 더 이상 읽을 줄이 없는 경우 None을 출력
```
while True:  
  line = f.readline()  
  if not line: break  
  print(line)  
f.close()
```
- 더 이상 읽을 줄이 없는 경우 None을 출력

## Ⅲ. readlines()

- 파일의 모든 줄을 읽어서 각각의 줄을 요소로 갖는 리스트로 반환
- ["1번째 줄입니다.", "2번째 줄입니다.", ... ]

## Ⅳ. read()

- 파일의 내용 전체를 문자열로 반환
```
data = f.read()  
print(data)
// data는 파일의 전체 내용
```

## Ⅴ. close()

- 파일 객체를 닫아주는 역할

## Ⅵ. with문

- 파일을 열고 닫는 것을 자동으로 처리해주는 문법
- with 블록을 벗어나는 순간 열린 파일 객체는 자동으로 close됨
```
with open("ex.txt", "w") as f:  
 f. write("blahblabhalbhalbhl")
```

---


# Class

``` 
class FourCal:  
   def setdata(self, first, second):  
     self.first = first   
     self.second = second
    
    def add(self):
      result = self.first + self.second
      return result
```
```
a = FourCal()
a.setdata(4, 2)
// self = a
// first = 4
// second = 2
```
```
print(a.add())
// 6
```

## Ⅰ. Constructor

- 객체가 생성될 때 자동으로 호출되는 method
- method name: \_\_init\_\_
```
class FourCal:
  def __init__(self, first, second):
    self.first = first
    self.second = second
```
- 객체 생성 시 생성자의 매개변수에 해당하는 값을 전달해야 함
```
a = FourCal(4, 2)
```

## Ⅱ. Inheritance

- FourCal class를 상속하는 MoreFourCal class
```
class MoreFourCal(FourCal):
  pass
```
- FourCal class를 상속했으므로 FourCal class의 모든 기능 사용 가능


---


# Module

## Ⅰ. definition

- 함수나 변수 또는 클래스를 모아 놓은 파일
- 다른 파이썬 프로그램에서 불러와 사용할 수 있게끔 만든 파이썬 파일

## Ⅱ. 불러오기

- import 모듈 이름
```
// mod1.py를 저장한 디렉터리: C:\doit
C:\Users\pahkey>cd C:\doit
C:\doit>python  // 대화형 인터프리터 실행
>>>
>>> import mod1 
>>> print(mod1.add(3, 4))   // mod1.py 파일에 있는 add 함수를 사용하려면 모듈 이름 뒤에 .를 붙이고 함수이름 입력
```
- from 모듈 이름 import 모듈 함수
```
from mod1 import add
add(3, 4)
7
```
```
from mod1 import add, sub
```
```
from mod1 import *    // 모듈 내의 모든 함수를 불러오겠다는 의미
```

## Ⅲ. if \_\_name__=="\_\_main\_\_"

- \_\_name\_\_ 변수: 파이썬이 내부적으로 사용하는 특별한 변수

```
# mod1.py
def add(a, b):
  return a+b
  
def sub(a, b):
  return a-b
   
if __name__=="__main":
  print(add(1, 4))
  print(sub(4, 2))
```

- python mod1.py와 같이 이 파일을 실행한 경우
: \_\_name\_\_ 변수에는 \_\_main\_\_ 값이 저장되어 \_\_name\_\_ == "\_\_main\_\_"이 참이 됨
```
C:\doit>python mod1.py
5
2
```

- 대화형 인터프리터나 다른 파일에서 이 모듈을 불러서 사용할 경우
: \_\_name\_\_ 변수에는 모듈 이름 mod1이 저장되어 \_\_name\_\_== "\_\_main\_\_"이 거짓이 됨
```
>>> import mod1
>>>
```


---


# Package

```
// 1. C:\doit 디렉터리 밑에 game와 기타 서브 디렉터리 및 .py 파일 생성
C:\doit\game\__init__.py
C:\doit\game\sound\__init__.py
C:\doit\game\sound\echo.py
C:\doit\game\graphic\__init__.py
C:\doit\game\graphic\render.py

// 2. 각 디렉터리에 __init__.py 파일 생성 - 내용은 비워둠

// 3. echo.py 파일 생성
# echo.py
def echo_test():
  print("echo")
  
// 4. render.py 파일 생성
# render.py
def render_test():
  print("render")

// 5. 생성한 game 패키지를 참조할 수 있도록 명령 프롬프트 창에서 set 명령어로 PYTHONPATH 환경 변수에 C:\doit 디렉터리 추가
C:\>set PYTHONPATH=C:\doit
```
## Ⅰ. 패키지 안 함수 실행하기

### 1. echo 모듈을 import하여 실행

```
>>> import game.sound.echo
>>> game.sound.echo.echo_test()
echo
```

### 2. echo 모듈이 있는 디렉터리를 from ... import하여 실행

```
>>> from game.sound import echo
>>> echo.echo_test()
echo
```

### 3. echo 모듈의 echo_test 함수를 직접 import 하여 실행

```
>>> from game.sound.echo import echo_test
>>> echo_test
echo
```
