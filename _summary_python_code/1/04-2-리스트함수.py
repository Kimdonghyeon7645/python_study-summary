# -*- coding: utf-8 -*-
"""
블로그 링크 : https://bodhi-sattva.tistory.com/70
"""
"""리스트 함수:
문자열처럼 리스트도 전용 함수가 있다.
대표적인 리스트 함수는 아래와 같다.
"""

a = [1, 2, 3]
print(a)
a.append(4)
a.append([1, 2])
print(a)
''' .append() 함수:
리스트 맨 마지막에 전달받은 매개변수를 요소로 추가한다. 그때의 매개변수는 1개든, 여러개든, 리스트든 가능하다.
참고로 아래처럼, 자기(리스트) 자신을 요소로 추가할 수 있다. 그러면 이렇게 무한루프?가 만들어진다. ([...]를 참조하면..)
'''
# roop = ['무한으로즐겨요']
# roop.append(roop)
# print(roop, roop[1], roop[1][1][1][1])


b = [2, 3, 1]
b2 = ['d', 'c']
b3 = ['낟', '난', '각']
b.sort()
b2.sort()
b3.sort()
print(b, b2, b3)
''' .sort() 함수:
리스트의 요소를 정렬시키는 함수로, 숫자든, 문자든 123, abc 순으로 정렬시킨다. 
(심지어 한글도 정렬된다 크~! , 여러 자료형이 짬뽕된 리스트는 정렬 못시키는 듯 하다)
'''


c = ['가자!', '때가 왔다!', '포기 할', '생각마라!', '승리할', '우리다!', '하찮은', '적들을 봐라!']
for ch in c:
    print(ch, end=' ')
print()
c.reverse()
for ch in c:
    print(ch, end=' ')
print()
''' .reverse() 함수:
리스트의 요소를 역순으로 뒤집는 함수다. (역순 정렬이 아니다. 그러고 싶으면 .sort().reverse()를 하자)
(참고로 리스트 함수가 아닌, 파이썬 내장함수로 같은 역할을 하는 reversed() 함수도 있다.)
'''


d = [1, 2, 3]
print(d.index(2))
''' .index() 함수:
리스트의 요소 값을 전달받아, 그 위치의 인덱스를 반환하는 함수다.
(d[n] 같이 인덱스로 요소 값을 반환하는 방식과 반대다)
'''
d.insert(0, 4)
print(d)
''' .insert() 함수:
인덱스 위치와, 넣을 요소 값을 전달받아, 그 인덱스 위치로 요소 값을 삽입하는 함수다.
(인덱스가 중복되면 차례대로 밀려서 재배치된다.)
'''
d.remove(4)
print(d)
''' .remove() 함수:
요소 값을 전달받아, 그 값을 삭제하는 함수다. (중복시 왼쪽부터 짜른다)
(del d[n] 같이 인덱스로 삭제하는 방식과 반대다)
'''
print("pop된 값: ", d.pop())
print(d)
''' .pop() 함수:
맨 마지막 요소를 반환하고, 그 요소를 리스트에서 삭제한다.
(스택 자료구조에서 연산이다, remove(d[-1]) + print(d[-1]) 와 같다)
'''
d.extend([3, 4])
print(d)
''' .extend() 함수:
기존 리스트에 전달받은 리스트를 덧붙이는 함수다. ( d.extend([3, 4]) == d += [3, 4] )
(.append() 함수랑 차이점은, 인자로 리스트를 전달받을 때 
extend() 는 같은 차원으로 추가되고, append()는 아래 차원의 요소 하나로 추가된다
그리고 extend()에서 인자는 리스트만 될 수 있다.) 
'''

"""그외 함수:
.count(n)  리스트에 n이 들어간 횟수를 반환한다.
.copy()  리스트를 복사한다. ( e = d.copy()  ==  e = d )
.clear()  리스트를 비운다. ( d.clear()  ==  d = [] )
"""
