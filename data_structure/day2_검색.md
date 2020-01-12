# 검색

* 검색: 자료에서 원하는 항목을 찾는 작업
  * 탐색키 기준

### 순차 검색

* 검색 대상이 많은 경우 비효율적
* 시간 복잡도: O(n)

1. 정렬되지 않은 자료의 경우
   * 하나하나 탐색키로 비교
2. 정렬된 경우
   * 하나하나 탐색키 비교함
   * 이때 원소의 키 값이 검색 대상의 키 값보다 클 경우, 원소가 없다는 거니까 그대로 검색 종료

### 이진 검색

* 범위를 반으로 줄여가며 검색

* 정렬되어 있어야 함

* 시간 복잡도: O(logN)

  ```python
  def binarySearch(a, key):
    start =0
    end = len(a)-1
    while start<=end:
      middle = start + (end-start)//2
      if key == a[middle]: #검색 성공
        return True
      elif key < a[middle]:
        end = middle - 1
      else:
        start = middle + 1
      return False	#검색 실패
  ```

  

  **재귀로 구현**

  ```python
  def binarySearch2(a, low, high, key):
    if low > high: #검색 실패
      return False
    else:
      middle = (low+high)//2
      if key == a[middle]: #검색 성공
        return True
      elif key < a[middle]:
        return binarySearch2(a, low, middle-1, key)
      elif a[middle] < key:
        return binarySearch2(a, middle+1, high, key)
  ```

  