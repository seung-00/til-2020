# Iterator

[주로 참고한 글](https://shoark7.github.io/programming/python/iterable-iterator-generator-in-python#4a)

```python
a= {"a":1, "d":2, "c":3}
sorted(a)
# ['a', 'c', 'd']

print(help(sorted))
# sorted(iterable, /, *, key=None, reverse=False)
#    Return a new list containing all items from the iterable in ascending order.
```

* sorted(), sum()과 같은 내장 함수들의 파라미터로 iterable 쓰인다.



### iterable

> An object capable of returning its members one at a time. Examples of iterables include all sequence types (such as [`list`](https://docs.python.org/3/library/stdtypes.html#list), [`str`](https://docs.python.org/3/library/stdtypes.html#str), and [`tuple`](https://docs.python.org/3/library/stdtypes.html#tuple)) and some non-sequence types like [`dict`](https://docs.python.org/3/library/stdtypes.html#dict), [file objects](https://docs.python.org/3/glossary.html#term-file-object), and objects of any classes you define with an [`__iter__()`](https://docs.python.org/3/reference/datamodel.html#object.__iter__) method or with a [`__getitem__()`](https://docs.python.org/3/reference/datamodel.html#object.__getitem__) method that implements [Sequence](https://docs.python.org/3/glossary.html#term-sequence) semantics. Iterables can be used in a [`for`](https://docs.python.org/3/reference/compound_stmts.html#for) loop and in many other places where a sequence is needed ([`zip()`](https://docs.python.org/3/library/functions.html#zip), [`map()`](https://docs.python.org/3/library/functions.html#map), …). 

 * iterable은 말 그대로 반복 가능한 객체다

    * for loop가 가능한 객체
    * iterator로 변환 가능한 객체

 * sequence는 iterable을 상속한 추상클래스다. sequence에는 list, tuple 등이 있다 ([참고](https://seung00.tistory.com/41)).

* 요구사항

  *  **`__iter__` **메소드에서 Iterator를 반환할 수 있어야 한다.

  

### iterator

> iterator
>
> An object representing a stream of data. Repeated calls to the iterator’s [`__next__()`](https://docs.python.org/3/library/stdtypes.html#iterator.__next__) method (or passing it to the built-in function [`next()`](https://docs.python.org/3/library/functions.html#next)) return successive items in the stream. When no more data are available a [`StopIteration`](https://docs.python.org/3/library/exceptions.html#StopIteration) exception is raised instead. At this point, the iterator object is exhausted and any further calls to its `__next__()` method just raise [`StopIteration`](https://docs.python.org/3/library/exceptions.html#StopIteration) again.

*  next 메소드로 값을 차례대로 접근할 수 있는 객체
  * iterable 객체의 **`__iter__`** 으로 변환되어 반환된다.아니면 내장 함수 **`iter`**를 쓸 수도 있다.

```python
a = [1, 2, 3]
type(a)
# <class 'list'>

# 내장함수 iter()를 사용해 iterator 객체를 만들 수 있다.
a_iter = iter(a)
type(a_iter)
# <class 'list_iterator'>

# iterable 객체는 매직메소드 __iter__ 를 가지고 있다. 이 메소드로 iterator를 만들수 있다.
b = {1, 2, 3}
dir(b)
# ['__and__', ... '__iter__', ...]
b_iter = b.__iter__()
type(b_iter)
# <class 'set_iterator'>

# next()로 꺼낼 수 있다
next(a_iter)
# 1
next(a_iter)
# 2
```

* 각  Iterator는 상태를 갖으며 서로 영향을 주지 않는다.

  * 각  Iterator의 상태란 순회하고 있는 위치다. 

  ```python
  l = [1, 2, 3]
  assert iter(l) != iter(l)
  ```

* 요구사항
  *  **`__iter__` **메소드는 자기 자신을 반환
  * **`__next__`**의 인자로 iterator를 줬을 때 다음 값을 반환하고 
  * Iterator가 반환할 값이 없는 경우 StopIteration 예외를 일으킴



### customizing

* iterator를 직접 구현해보자. 핵심은 **`__iter__`**와 **`__next__`** 다.

  ```python
  class Iterable3:
  	def __init__(self, size):
  		self.size = size	# 컨테이너 크기
  	def __iter__(self):
  		return Iterator3(self.size)	# 현재 인스턴스 반환시켜줌
  
  class Iterator3:
    def __init__(self, size):
      self.cur = 0	# 현재 위치
      self.size = size	# 컨테이너 크기
    def __iter__(self):
      return self
    def __next__(self):
      if self.cur<self.size:
        self.cur += 1
        return self.cur*3
      else:
        raise StopIteration
  
  it = Iterable3(5)
  for i in it:
    print(i)
  #3
  #6
  #9
  #12
  #15
  ```

  