# L1, L2 Regularization

[참고1](http://light-tree.tistory.com/125)

[참고2](https://www.youtube.com/watch?v=deEqfwlH67U&t=2s)

[수식 및 그림 출처](https://en.wikipedia.org/wiki/Norm_(mathematics))

[toc]

## Norm

* Norm이란 벡터의 크기(혹은 거리)를 측정하는 방법임.

  ### L1 Norm(Taxicab norm)
  
   ![\ left \ | x \ right \ | = \ left | x \ right |](https://wikimedia.org/api/rest_v1/media/math/render/svg/22fd51db136659c9d2fdf018cf2b906a95690067)
  
  ![d_ {1} (\ mathbf {p}, \ mathbf {q}) = \ | \ mathbf {p}-\ mathbf {q} \ | _ {1} = \ sum _ {i = 1} ^ {n} | p_ {i} -q_ {i} |,](https://wikimedia.org/api/rest_v1/media/math/render/svg/02436c34fc9562eb170e2e2cfddbb3303075b28e)![\ mathbf {p} = (p_ {1}, p_ {2}, \ dots, p_ {n}) {\ text {and}} \ mathbf {q} = (q_ {1}, q_ {2}, \ 도트, q_ {n}) \,](https://wikimedia.org/api/rest_v1/media/math/render/svg/3be69c76d8560e245117031391182ca0cd95130d)
  
  
  
  ### L2 Norm(Euclidean norm)
  
   ![{\displaystyle \left\|{\boldsymbol {x}}\right\|_{2}:={\sqrt {x_{1}^{2}+\cdots +x_{n}^{2}}}.}](https://wikimedia.org/api/rest_v1/media/math/render/svg/4d2562bd8e6df0c2625fd9c0e0c09ee9b932785d)
  
  
  
   ![{\ displaystyle {\ begin {aligned} d (\ mathbf {p}, \ mathbf {q}) = d (\ mathbf {q}, \ mathbf {p}) & = {\ sqrt {(q_ {1}- p_ {1}) ^ {2} + (q_ {2} -p_ {2}) ^ {2} + \ cdots + (q_ {n} -p_ {n}) ^ {2}}} \\ [8pt ] & = {\ sqrt {\ sum _ {i = 1} ^ {n} (q_ {i} -p_ {i}) ^ {2}}}. \ end {aligned}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/795b967db2917cdde7c2da2d1ee327eb673276c0)
  
  
  
  ### L1 Norm과 L2 Norm
  
  ![img](https://upload.wikimedia.org/wikipedia/commons/thumb/0/08/Manhattan_distance.svg/200px-Manhattan_distance.svg.png)
  
  * 검은 점에서 검은 점까지 가는 경우 빨강, 파랑, 노랑 선은 L1 Norm이 될 수 있고. 초록 선은 L2 Norm이 될 수 있음.
  * L1 Norm은 여러가지 경로를 가지며 L2 Norm과 겹칠 수도 있음. L2 Norm은 유일한 최소 경로(**unique shortest path**) 를 가짐.



## Regularization

<img src="https://user-images.githubusercontent.com/46865281/77522638-e3f12380-6ec7-11ea-826f-c50c7b339b89.png" alt="image" style="zoom:50%;" />

* 모델을 학습하다 보면 과적합 현상이 발생함. 이를 막기 위해 모델의 복잡도(weight)에 패널티를 주는 식으로 정규화를 진행함.

* **learning rate** 와 유사한 용도인 **lamda**가 쓰임. 둘은 관계가 있는데, 낮은 learning rate가 보폭을 줄여서 가중치가 미치는 영향을 줄이듯, 높은 lamda는 가중치를 0으로 유도함. 따라서 둘을 동시에 변경하면 결과 해석에 혼동이 생길 수 있음.

  

  ### L1 Regularization(lasso)

  <img src="https://miro.medium.com/max/1292/1*1zCcVuEOPi64mjkkF6Uj7w@2x.png" alt="img" style="zoom:50%;" />[^1]

  

  ### L2 Regularization(ridge)

  <img src="https://miro.medium.com/max/1256/1*FfBxNNuFoCnzq8eEzPrRcw@2x.png" alt="img" style="zoom:50%;" />[^1]

  

  ### L1과 L2

  * Regularization의 목적은 가중치(복잡도)가 미치는 영향을 줄여서 Outlier의 영향을 덜 받도록 하는 것임.

  * 일반적으로 L2 Regularization이 쓰인다. 성능이 더 좋기 때문. outliar 에 더 민감하다.

  * L1은 가중치 벡터를 듬성듬성(sparse)하게 만든다. 결국 특정 feature를 0으로 만들어 업데이트를 멈추도록 하는 특징이 있다.

    * GD(gradient descent)를 위해 각각을 미분 했을 때, L2는 가중치^2에 패널티를 주니까 대략  `lr*2*w `로 업데이트 할 것이고, l1은 `lr*k*w`로 업데이트를 할 것이다.

    * L2의 경우 매번 가중치의 x%만큼 제거하는 꼴이기 때문에 결코 0이 될 수 없다. 반면 L1은 가중치와 무관한 상수 값을 빼주기 때문에 0이 될수 있음.

      * 조금 더 구체적으로, L2 norm은 unique shortest path를 가지므로 서로 다른 두 벡터가 주어졌을 때 그 차이가 결코 0이 될 수 없다.

    * 아래 그림처럼,  L1은 미분 불가능한 점이 생길 수 있으므로 GD할 때 주의 필요.

      <img src="https://t1.daumcdn.net/cfile/tistory/99BED3425CE4B13418" alt="img" style="zoom:50%;" />[^2]

  * 이런 특징 때문에 고차원 희소 벡터를 사용할 때 불필요한 특성을 삭제하기 위해(feature selection) L1이 쓰인다.

    

[^1]: https://towardsdatascience.com/intuitions-on-l1-and-l2-regularisation-235f2db4c261
[^2]:https://www.quora.com/When-would-you-chose-L1-norm-over-L2-norm

