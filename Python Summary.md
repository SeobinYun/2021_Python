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


---


# Exception Handling

## Ⅰ. try, except

```
try:
  ...
except [발생 오류[as 오류 메시지 변수]]:
  ...
```
- try 블록 수행 중 오류가 발생하면 except 블록 수행
- []: 괄호 안의 내용을 생략할 수 있다는 관례 표기 기법

### 1. try, except만 쓰는 방법

```
try:
  ...
except:
  ...
```

- 오류 종류에 상관없이 오류가 발생하면 except 블록 수행

### 2. 발생 오류만 포함하는 방법

```
try:
  ...
except 발생 오류:
  ...
```

- 오류가 발생했을 때 except문에 미리 정해 놓은 오류 이름과 일치할 때만 except 블록 수행

### 3. 발생 오류와 오류 메시지 변수를 포함한 except문

```
try: 
  ...
except 발생 오류 as 오류 메시지 변수:
  ...
```

```
try:
  4/0
except ZeroDivisionError as e:
  print(e)
```

```
결괏값: division by zero
```

```
try:
  a = [1, 2]
  print(a[3])
  4/0
except (ZeroDivisionError, IndexError) as e:
  print(e)
```



- 오류가 발생했을 때 except문에 미리 정해 놓은 오류 이름과 일치할 때만 except 블록을 수행, 오류 메시지의 내용까지 알고 싶을 때 사용

## Ⅱ. try ... finally

- finally절은 예외 발생 여부에 상관없이 항상 수행됨

```
f = open('ex.txt', 'w')
try: 
  # 무언가를 수행한다.
finally:
  f.close()
```

## Ⅲ. 오류 회피

```
try: 
  f = open("없는 파일", 'r')
except FileNotFoundError:
  pass
```

- 특정 오류가 발생할 경우 그냥 통과

## Ⅳ. 오류 일부러 발생

- raise 명령어 사용

> ex) Bird 클래스를 상속받는 자식 클래스가 반드시 fly라는 함수를 구현하도록 하고 싶은 경우
> fly 함수를 구현하지 않은 상태로 fly 함수 호출 시 NotImplementedError 오류 발생

```
class Bird:
  def fly(self):
    raise NotImplementedError
    
class Eagle(Bird):
  pass
  
eagle = Eagle()
eagle.fly()
// NotImplementedError 발생
```

## Ⅴ. 예외 만들기 

- 파이썬 내장 클래스인 Exception 클래스를 상속하여 생성 가능

> ex) 별명을 출력해주는 함수에서 MyError 사용
```
class MyError(Exception):
  pass

def say_nick(nick):
  if nick == '바보':
    raise MyError()
  print(nick)
  
say_nick("바보")
// MyError 발생 
```

> ex) 예외처리 기법을 사용하여 MyError 발생 예외 처리
```
try:
  say_nick("천사")
  say_nick("바보")
except MyError:
  print("허용되지 않는 별명입니다.")
  
// 천사
// 허용되지 않은 별명입니다.
```

> ex) MyError에서 \_\_str\_\_ 메서드 구현하여 오류 메시지 사용

```
class MyError(Exception):
  def __str__(self):
    return "허용되지 않는 별명입니다."
    
try:
  say_nick("천사")
  say_nick("바보")
except MyError as e:
  print(e)
  
// 천사
// 허용되지 않는 별명입니다.
```


---


# Built-in Function


- import 등 기타 설정없이 바로 사용 가능


### 1. all(x)


- 반복 가능한 자료형 x가 모두 참이면 True, 하나라도 거짓이면 False

```
>>> all([1, 2, 3])
True
>>> all([1, 2, 3, 0])
False
```


### 2. abs(x)


- x의 절댓값을 돌려주는 함수


### 3. any(x)


- x가 모두 거짓이면 False, 하나라도 참이면 True

```
>>> any([1, 2, 3, 0])
True
>>> any([0, ""])
False
```


### 4. chr(x)


- ASCII 코드를 입력받아 코드에 해당하는 문자 반환

```
>>> chr(97)
'a'
>>> chr(48)
'0'
```


### 5. dir(x) 


- 객체가 자체적으로 가지고 있는 변수나 함수 반환

```
>>> dir([1, 2, 3])
['append', 'count', 'extend', 'index', ...]
>>> dir({'1':'a'})
['clear', 'copy', 'get', 'has_key', 'items', ...]
```


### 6. dirmod(a, b)


- a를 b로 나눈 몫과 나며지를 튜플 형태로 반환

```
>>> divmod(7, 3)
(2, 1)
```


### 7. enumerate(x)


- 순서가 있는 자료형(리스트, 튜플, 문자열)을 입력으로 받아 인덱스 값을 포함하는 enumerate 객체 반환

```
for i, name in enumerate(['body', 'foo', 'bar']):
  print(i, name)
  
0 body
1 foo
2 bar
```


### 8. eval(expression)


- 실행 가능한 문자열을 입력으로 받아 문자열을 실행한 결괏값 반환
- 문자열로 파이썬 함수나 클래스를 동적으로 실행할 때 사용

```
>>> eval('1+2')
3
>>> eval("'hi'+'a'")
'hia'
>>> eval('divmod(4, 3)')
(1, 1)
```


### 9. filter(f, iterable)


- iterable 자료형의 요소가 함수 f에 입력되었을 때 반환 값이 참인 것만 묶어서 반환

```
def positive(x):
  return x>0
  
print(list(filter(positive, [1, -3, 2, 0, -5, 6])))
```
```
>>> list(filter(lambda x: x>0, [1, -3, 2, 0, -5, 6]))
// [1, 2, 6]
```


### 10. hex(x)


- 정수 값을 입력받아 16진수로 변환

```
>>> hex(234)
'0xea'
```


### 11. id(object)


- 객체의 고유 주소 값 반환

```
>>> a = 3
>>> id(3)
135072304
>>> id(a)
135072304
>>> b = a
>>> id(b)
135072304
```


### 12. input([prompt])


- 사용자 입력을 받는 함수
- 문자열 인자 생략 가능
- 매개변수로 문자열을 주면 프롬프트를 띄움

```
>>> a = input()
_
>>> b = input("Enter: ")
Enter: _
```


### 13. int(x)


- 문자열 형태의 숫자나 소수점이 있는 숫자 등을 정수 형태로 변환

```
>>> int('3')
3
>>> int(3.4)
3
```

- int(x, radix): radix 진수 문자열을 10진수로 변환

```
>>> int('1A', 16)
26
```


### 14. isinstance(object, class)


- object: 인스턴스 / class: 클래스 이름
- 인스턴스가 클래스의 인스턴스인지 판단하여 참이면 True, 거짓이면 False

```
>>> class Person: pass
...
>>> a = Person()
>>> isinstance(a, Person)
True
>>> b = 3
>>> isinstance(b, Person)
False
```


### 15. len(x)


- 입력값의 길이(요소의 전체 개수) 반환


### 16. list(iterable)


- iterable 자료형을 리스트로 변환

```
>>> list("python")
['p', 'y', 't', 'h', 'o', 'n']
>>> list((1, 2, 3))
[1, 2, 3]
```


### 17. map(f, iterable)


- iterable 자료형의 각 요소를 함수 f가 수행한 결과를 묶어서 반환

```
>>> def two_times(x): return x*2
...
>>> list(map(two_times, [1, 2, 3, 4]))
[2, 4, 6, 8]
```
```
>>> list(map(lambda a: a*2, [1, 2, 3, 4]))
[2, 4, 6, 8]
```


### 18. max(iterable)


- iterable 자료형의 최댓값 반환


### 19. min(iterable)


- iterable 자료형의 최솟값 반환


### 20. oct(x) 


- 정수 형태의 숫자를 8진수 문자열로 변환

```
>>> oct(34)
'0o42'
```


### 21. ord(c)


- 문자의 아스키 코드 값 반환

```
>>> ord('a')
97
```


### 22. pow(x, y)


- x의 y 제곱한 결괏값 반환

```
>>> pow(2, 4)
16
```


### 23. round(number[, ndigits])


- 숫자를 입력받아 반올림
- ndigits는 반올림하여 표시하고 싶은 소수점의 자릿수

```
>>> round(4.6)
5
>>> round(5.678, 2)
5.68
```


### 24. sorted(iterable)


- 입력값을 정렬한 후 그 결과를 리스트로 반환

```
>>> sorted([3, 1, 2])
[1, 2, 3]
>>> sorted(['a', 'c', 'b'])
['a', 'b', 'c']
>>> sorted("zero")
['e', 'o', 'r', 'z']
```


### 25. str(object)


- 객체를 문자열 형태로 변환

```
>>> str('hi'.upper())
'HI'
```


### 26. sum(iterable)


- 리스트나 튜플의 모든 요소의 합 반환


### 27. tuple(iterable)


- iterable 자료형을 튜플 형태로 변환

```
tuple("abc")
('a', 'b', 'c')
```


### 28. type(object)


- 입력값의 자료형 반환

```
>>> type("abc")
<class 'str'>
>>> type([])
<class 'list'>
>>> type(open("test", 'w'))
<class '_io.TextIOWrapper'>
```


### 29. zip(\*iterable)


- 동일한 개수로 이루어진 자료형을 묶어주는 역할

```
>>> list(zip([1, 2, 3], [4, 5, 6]))
[(1, 4), (2, 5), (3, 6)]
>>> list(zip("abc", "def"))
[('a', 'd'), ('b', 'e'), ('c', 'f')]
```


---


# Library


## Ⅰ. sys


- 파이썬 인터프리터가 제공하는 변수와 함수를 직접 제어할 수 있게 해주는 모듈


### 1. sys.argv - 명령 행에서 인수 전달하기


```
C:\User\home>python test.py abc pey guidp
```

- 명령 프롬프트 창에서 .py 뒤에 또 다른 값을 함께 넣어주면 sys.argv 리스트에 그 값이 추가됨.

```
# argv_test.py
import sys
print(sys.argv)
```
```
# 명령 프롬프트 창에서 argv_test.py 실행
C:/doit/Mymod>python argv_tset.py you need python
['argv_tset.py', 'you', 'need', 'python']
```

- python 명령어 뒤의 입력 값이 공백을 기준으로 나뉘어 sys.argv 리스트의 요소가 됨.


### 2. sys.exit - 강제로 스크립트 종료


```
>>> sys.exit()
```

- 프로그램 파일 안에서 사용하면 프로그램을 중단시킴.
- ctrl+z나 ctrl+d를 눌러서 대화형 인터프리터를 종료하는 것과 같은 기능.


### 3. sys.path - 자신이 만든 모듈 불러와 사용하기


- 파이썬 모듈들이 저장되어 있는 위치를 나타냄.
- 이 위치에 있는 파이썬 모듈은 경로에 상관없이 어디에서나 불러올 수 있음.

[image](https://user-images.githubusercontent.com/54767707/136689705-ea702049-6d2e-4bdb-b5aa-8a4e45d64247.png)

- 경로 이름을 추가하면, 해당 경로에 있는 파이썬 모듈을 불러와서 사용 가능.

```
import sys
sys.path.append("C:\doit\Mymod")
```


## Ⅱ. pickle


- 객체의 형태를 그대로 유지하면서 파일에 저장하고 불러올 수 있게 하는 모듈


### 1. pickle.dump


- 딕셔너리 객체를 그대로 파일에 저장

```
>>> import pickle
>>> f = open{"test.txt", 'wb'}
>>> data = {1: 'python', 2: 'you need'}
>>> pickle.dump(data, f)
>>> f.close()
```


### 2. pickle.load


- pickle.dump로 저장한 파일을 원래 딕셔너리 객체 상태로 불러오기

```
>>> import pickle
>>> f = open("test.txt", 'rb')
>>> data = pickle.load(f)
>>> print(data)
{1: 'python', 2: 'you need'}
```


---


## Ⅲ. OS


- OS 모듈은 환경 변수나 디렉터리, 파일 등의 OS 자원을 제어할 수 있게 해주는 모듈


### 1. os.environ


- 현재 시스템의 환경 변수에 대한 정보를 딕셔너리 객체로 반환

```
>>> import os
>>> os.environ
environ({'PROGRAMFILES': 'C:\\Program Files', 'APPDATA':... 생략...})
```
```
>>> os.environ['PATH']
'C:\\ProgramData\\Oracle\\Java\\javapath; ... 생략...'
```


### 2. os.chdir


- 디렉터리 위치 변경

```
>>> os.chdir("C:\WINDOWS")
```


### 3. os.getcwd


- 현재 디렉터리 위치 반환

```
>>> os.getcwd()
'C:\WINDOWS' // 현재 디렉터리 위치
```


### 4. os.system


- 시스템 자체의 프로그램이나 기타 명령어를 파이썬에서 호출할 수 있음.

```
# 현재 디렉터리에서 시스템 명령어 dir 실행
>>> os.system("dir")
```


### 5. os.popen


- 시스템 명령어를 실행한 결과값을 읽기 모드 형태의 파일 객체로 반환

```
>>> f = os.popen("dir")
```


### 6. os.mkdir(directory)


- 디렉터리 생성


### 7. os.rmdir(directory)


- 디렉터리 삭제
- 단 디렉터리가 비어 있어야 삭제 가능


### 8. os.unlink(filename)

- 파일을 지움.


### 9. os.rename(src, dst)


- src라는 이름의 파일을 dst라는 이름으로 바꿈.


## Ⅳ. shutil

- 파일을 복사해주는 파이썬 모듈
- src라는 이름의 파일을 dst로 복사
- dst가 디렉터리 이름이면 src라는 파일 이름으로 dst 디렉터리에 복사
- 동일한 파일 이름이 있을 경우에는 덮어 씀

```
>>> import shutil
>>> shutil.copy("src.txt", "dst.txt")
```


## Ⅴ. glob

- 특정 디렉터리에 있는 파일들을 리스트로 반환
- \*, ? 등 메타 문자를 써서 원하는 파일만 읽어들일 수 있음

```
# C:\doit 디렉터리에 있는 파일 중 이름이 mark로 시작하는 파일 모두 찾기

>>> import glob
>>> glob.glob("c:\doit\mark*")
['c:\doit\marks1.py', ...]
```


## Ⅵ. tempfile


- 파일을 임시로 만들어서 사용


### 1. tempfile.mkstemp


- 중복되지 않은 임시 파일의 이름을 무작위로 생성하여 반환


```
>>> import tempfile
>>> filename = tempfile.mkstemp()
>>> filename
'C:\WINDOWS\TEMP\~~275151-0'
```


### 2. tempfile.TemporaryFile


- 임시 저장 공간으로 사용할 파일 객체 반환
- 기본적으로 wb 모드
- f.close()가 호출되면 파일 객체는 자동으로 사라짐

```
>>> import tempfile
>>> f = tempfile.TemporaryFile()
>>> f.close()  // 생성한 임시 파일이 자동으로 삭제됨
```


## Ⅶ. time


### 1. time.time


- UTC를 사용하여 현재 시간을 실수 형태로 반환

```
# 1970년 1월 1일 0시 0분 0초를 기준으로 지난 시간을 초 단위로 반환
>>> import time
>>> time.time()
988458015.73417199
```


### 2. time.localtime


- time.time()이 돌려준 실수 값을 사용하여 연도, 월, 일, 시, 분, 초, ...의 형태로 반환

```
>>> time.localtime(time.time())
time.struct_time(tm_year=2013, tm_mon=5, tm_mday=21,...
```


### 3. time.asctime


- time.localtime에서 반환된 튜플 값을 인수로 받아서 날짜와 시간을 알아보기 쉬운 형태로 반환

```
>>> time.asctime(time.localtime(time.time()))
'Sat Apr 28 20:50:20 2001'
```


### 4. time.ctime


- 현재 시간 반환

```
>>> time.ctime()
'현재 시간'
```


### 5. time.strftime


- 시간에 관계된 것을 세밀하게 표현하는 여러 가지 포맷 코드 제공

```
time.strftime('출력할 형식 포맷 코드', time.localtime(time.time()))
```
```
>>> import time
>>> time.strftime('%x', time.localtime(time.time()))
'05/01/0'
>>> time.strftime('%c', time.localtime(time.time()))
'05/01/01 17:22:21'
```


### 6. time.sleep


- 주로 루프 안에서 많이 사용
- 일정한 시간 간격을 두고 루프를 실행할 수 있음
- 인수는 실수 형태 ex) 1이면 1초, 0.5면 0.5초

```
# 1초 간격으로 0부터 9까지의 숫자 출력

import time
for i in range(10):
  print(i)
  time.sleep(1)
```


## Ⅷ. calendar


### 1. calendar.calendar(연도)


- 그해의 전체 달력 출력

```
>>> import calendar
>>> print(calendar.calendar(2014))
```


### 2. calendar.prcla(연도)


- calendar.calendar과 같은 결과


### 3. calendar.weekday(연도, 월, 일)


- weekday(연도, 월, 일) 함수는 그 날짜에 해당하는 요일 정보 반환
- 월~일은 0~6이라는 값으로 반환

```
>>> calendar.weekday(2015, 12, 31)
3
```


### 4. calendar.monthrange(연도, 월)


- 입력받은 달의 1일이 무슨 요일인지와 그 달이 며칠까지 있는지 튜플 형태로 반환

```
>>> calendar.monthrange(2015, 12)
(1, 31)
```


## Ⅸ. random


- 난수를 발생시키는 모듈


### 1. random.random


```
# 0.0에서 1.0 사이의 실수 중 난수 생성

>>> import random
>>> random.random()
```


### 2. random.randint

```
# 1에서 10 사이의 정수 중 난수 생성

>>> random.randint(1, 10)
6
```


### 3. random.shuffle


- 리스트 항목 무작위로 섞는 함수

```
>>> import random
>>> data = [1, 2, 3, 4, 5]
>>> random.shuffle(data)
>>> data
[5, 1, 3, 4, 2]
```


## Ⅹ. webbrowser

- 자신의 시스템에서 사용하는 기본 웹 브라우저를 자동으로 실행하는 모듈

```
# 웹 브라우저를 자동으로 실행하고 해당 URL인 google.com으로 이동

>>> import webbrowser
>>> webbrowser.open("http://google.com")
```


