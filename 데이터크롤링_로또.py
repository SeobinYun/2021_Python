from bs4 import BeautifulSoup # HTML을 다루는 라이브러리
import requests # 요청하다. 엔터키 역할

'''
url = requests.get("https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EB%A1%9C%EB%98%90").text
html = BeautifulSoup(url)

current_number = int(html.find('a', attrs={'class':'_lotto-btn-current'}).find('em').text[:-1])
current_number
'''

total = []

for n in range(1, current_number + 1):
  url = requests.get("https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EB%A1%9C%EB%98%90+{}%ED%9A%8C".format(n)).text
  html = BeautifulSoup(url)

  numbers = html.find('div', attrs={'class':'num_box'}).find_all('span')
  del numbers[6]

  box = []

  for i in numbers:
    box.append(int(i.text))

  total.append(box)

  print('{}회 로또 데이터 저장완료 : {}'.format(n, box))
