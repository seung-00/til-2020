## 깊이 우선 탐색(DFS)

![image](https://user-images.githubusercontent.com/46865281/72500441-d0965c00-3877-11ea-94be-d61c7db3f8db.png)

* 코드

  ```python
  def DFS(graph, root):
      visited = []
      stack = []
      stack.append(root)
  
      while stack:
          node = stack.pop()
          visited.append(node)
          childNode = list((graph[node]) - set(visited))   #자식 노드 중 아직 안 간 곳
          stack.extend(childNode)
  #graph = {1:{4, 3}, 2:{3, 5}, 3:{}, 4:{6}, 5:{}, 6:{}}
  ```

  

* 재귀로 구현

  ```python
  def DFS(graph, node, visited):
      if node not in visited:
          print(node)
          visited.append(node)
      for neighbour in graph[node]:
          DFS(graph, neighbour, visited)
  ```

  다른 코드

  ```python
  def DFS(graph, node, visited):
      visited.append(node)
      print(node)
      childNode = list((graph[node]) - set(visited))   #자식 노드 중 아직 안 간 곳
      while childNode:
          DFS(graph, childNode.pop(), visited)
  ```

  * 딕셔너리가 경로 저장하기 좋다, set을 쓰면 방문한 노드를 제외하기 좋다.
  * 트리 구조를 재귀로 만들 때 주의할 점은 **재귀가 그저 스택의 역할을 대신 수행할 뿐이라는 점이다.** 자식 노드들을 이동하는 과정이 재귀 중에 꼬이지 않도록 신경써야 한다.
    * 예컨대, 종료 조건 속에 return을 놓고, return func()을 할 경우 dfs를 돌다가 반복문이 끝날 것이다.

