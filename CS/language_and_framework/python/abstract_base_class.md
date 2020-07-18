# ABC(Abstract Base Class)

## 추상클래스란?

* 추상 클래스는 파이썬 뿐만 아니라 OOP 를 지원하는 많은 언어들에 존재하는 개념이다. 예를 들어 C++에서는 하나 이상의 순수 가상함수를 포함하는 클래스를 추상 클래스라고 부르며 자바는 abstract라는 키워드로 추상 클래스를 선언한다.

* 먼저 OOP를 상기해보자. OOP 에는 1. 추상화 2. 캡슐화 3. 상속 4.다형성 네 가지 특성이 있다.

  1. 공통의 속성, 기능을 묶어 추상화하는 것

  2. 변수와 함수를 하나로 묶어 은닉화하는 것
  3. 상위 클래스의 특징을 하위 클래스가 물려받아 재사용 하는 것
  4. 부모 클래스로부터 물려받은 기능을 오버라이딩하는 것

* python, c++, java 모두 추상 클래스는 그 자체로 객체화가 불가능하며 자식 클래스에서 오버라이딩해서 객체화해야 한다는 공통점이 있다.
  * 즉, 추상 클래스는 그 자체로 객체화하기에 너무 추상적이어서 자식 클래스에서 구체적으로 객체화 하도록 강제한 것이라 생각할 수 있다.



## 파이썬의 추상클래스

* 파이썬은 **`collections.abc`**이라는 모듈에서 list와 같은 내장 컨테이너들의 추상 클래스를 제공한다

  * [출처](https://docs.python.org/ko/3.9/library/collections.abc.html#collections.abc.Container)

    | ABC                                                          | 상속                                                         | 추상 메소드                           | 믹스인 메소드                                                |
    | :----------------------------------------------------------- | :----------------------------------------------------------- | :------------------------------------ | :----------------------------------------------------------- |
    | [`Container`](https://docs.python.org/ko/3.9/library/collections.abc.html#collections.abc.Container) |                                                              | `__contains__`                        |                                                              |
    | [`Hashable`](https://docs.python.org/ko/3.9/library/collections.abc.html#collections.abc.Hashable) |                                                              | `__hash__`                            |                                                              |
    | [`Iterable`](https://docs.python.org/ko/3.9/library/collections.abc.html#collections.abc.Iterable) |                                                              | `__iter__`                            |                                                              |
    | [`Iterator`](https://docs.python.org/ko/3.9/library/collections.abc.html#collections.abc.Iterator) | [`Iterable`](https://docs.python.org/ko/3.9/library/collections.abc.html#collections.abc.Iterable) | `__next__`                            | `__iter__`                                                   |
    | [`Reversible`](https://docs.python.org/ko/3.9/library/collections.abc.html#collections.abc.Reversible) | [`Iterable`](https://docs.python.org/ko/3.9/library/collections.abc.html#collections.abc.Iterable) | `__reversed__`                        |                                                              |
    | [`Generator`](https://docs.python.org/ko/3.9/library/collections.abc.html#collections.abc.Generator) | [`Iterator`](https://docs.python.org/ko/3.9/library/collections.abc.html#collections.abc.Iterator) | `send`, `throw`                       | `close`, `__iter__`, `__next__`                              |
    | [`Sized`](https://docs.python.org/ko/3.9/library/collections.abc.html#collections.abc.Sized) |                                                              | `__len__`                             |                                                              |
    | [`Callable`](https://docs.python.org/ko/3.9/library/collections.abc.html#collections.abc.Callable) |                                                              | `__call__`                            |                                                              |
    | [`Collection`](https://docs.python.org/ko/3.9/library/collections.abc.html#collections.abc.Collection) | [`Sized`](https://docs.python.org/ko/3.9/library/collections.abc.html#collections.abc.Sized), [`Iterable`](https://docs.python.org/ko/3.9/library/collections.abc.html#collections.abc.Iterable), [`Container`](https://docs.python.org/ko/3.9/library/collections.abc.html#collections.abc.Container) | `__contains__`, `__iter__`, `__len__` |                                                              |
    | [`Sequence`](https://docs.python.org/ko/3.9/library/collections.abc.html#collections.abc.Sequence) | [`Reversible`](https://docs.python.org/ko/3.9/library/collections.abc.html#collections.abc.Reversible), [`Collection`](https://docs.python.org/ko/3.9/library/collections.abc.html#collections.abc.Collection) | `__getitem__`, `__len__`              | `__contains__`, `__iter__`, `__reversed__`, `index` 및 `count` |
    | [`Set`](https://docs.python.org/ko/3.9/library/collections.abc.html#collections.abc.Set) | [`Collection`](https://docs.python.org/ko/3.9/library/collections.abc.html#collections.abc.Collection) | `__contains__`, `__iter__`, `__len__` | `__le__`, `__lt__`, `__eq__`, `__ne__`, `__gt__`, `__ge__`, `__and__`, `__or__`, `__sub__`, `__xor__` 및 `isdisjoint` |

  * 위 표에서처럼 각 추상 클래스는 자식 클래스 컨테이너가 구현해야 하는 메소드들을 선언해주고 있다.

  * 각각의 내장 컨테이너들은 필요한 추상 클래스들을 상속 받는다.

    ```python
    issubclass(list,collections.Sequence)
    # True
    issubclass(set,collections.Sequence)
    # False
    issubclass(set,collections.iterable)
    # True
    ```

    