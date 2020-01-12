# 정렬

![image](https://user-images.githubusercontent.com/46865281/72217547-d851ba00-3572-11ea-94b8-a9d9a5b91a8f.png)





### 셀렉션 알고리즘

* k 번째로 큰, 혹은 작은 원소를 찾는 방법

* 최댓값, 최솟값 혹은 중간값을 찾는 알고리즘으로도 쓰임

* k번째로 작은 원소를 찾는 알고리즘

  * k가 비교적 작을 때 유용, O(kn)

  ```python
  def select(lst, k):
    for i in range(0, k):
      minIdx = i
      for j in range(i+1. len(lst)):
        if lst[minIdx] > lst[j]:
          minIdx = j
      lst[i], lst[minIdx] = lst[minIdx], lst[i]
      return lst[k-1]
  ```

### 선택 정렬

* 셀렉션 알고리즘을 이용한 정렬 방법

* 가장 작은 값의 원소부터 차례대로 위치를 교환

  * 시간 복잡도: O(n^2)

  ```python
  def selectionSort(arr):
    for i in range(0, len(arr)-1):
      minIdx = i
      for j in range(i+1, len(arr)):
        if arr[minIdx]>arr[j]:
          min = j
       arr[i], arr[min] = arr[min], arr[i]
  ```