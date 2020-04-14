## 깊이 우선 탐색(DFS), 인접행렬, 인접 리스트

<img src="https://user-images.githubusercontent.com/46865281/72500441-d0965c00-3877-11ea-94be-d61c7db3f8db.png" alt="image" style="zoom:150%;" />

* 그래프의 노드 간 관계를 표현할 때 인접 리스트 방식과 인접 행렬 방식이 있다. 파이썬은 딕셔너리 등을 이용해 인접 리스트로 표현하기 편하다. 하지만 그래프 문제에서 인접 행렬 방식이 보편적으로 쓰이는 것 같다.

  
  
* 딕셔너리로 인접 행렬 구현 코드

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
  * 트리 구조를 재귀로 만들 때 주의할 점은 재귀가 그저 스택의 역할을 대신 수행할 뿐이라는 점이다. 자식 노드들을 이동하는 과정이 재귀 중에 꼬이지 않도록 신경써야 한다.

    

* 인접행렬 코드([백준]2606_바이러스)

  ```python
  def DFS(node, size):
      visited[node] = 1   
      stack = [node]
      while stack:
          curNode = stack.pop()
          for nextNode in range(1, size+1):
              if graph[curNode][nextNode] and not visited[nextNode]: #연결되어 있고, 방문하지 않았다면
                  visited[nextNode] = True
                  stack.append(nextNode)
                  
  ...
  
  for _ in range(k):
      i, j = map(int, input().split())
      graph[i][j] = True
      graph[j][i] = True
  
  ```

  * 무향그래프인 경우, 양방향 다 표시를 해주어야 하기 때문에 데이터를 입력받을 때 `graph[i][j]` `graph[j][i]` 둘 다 넣어줘야 한다.

    

* 인접 리스트 코드(위와 동일 문제)

  ```python
  def DFS(node, size):
      visited[node] = True
      stack = [node]
      cnt = 0
      while stack:
          curNode = stack.pop()
          for neighbor in graph[curNode]:  #연결되어 있고
              if not visited[neighbor]:   #방문하지 않았다면
                  visited[neighbor] = True
                  stack.append(neighbor)
                  cnt += 1
      return cnt
    
  ...
    
  for _ in range(k):
      i, j = map(int, input().split())
      graph[i].append(j)
      graph[j].append(i)
  ```

  