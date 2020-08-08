# 예시를 통한 ROGUE 성능 지표의 이해

### ROGUE 가 요약 모델의 성능을 평가하는 방법

ROGUE 는 Recall - Oriented Understudy for Gisting Evaluation의 준말로 텍스트 요약 모델의 성능 평가 지표다. ROGUE는 모델이 생성한 요약본 혹은 번역본을 사람이 미리 만들어 놓은 참조본과 대조해 성능 점수를 계산한다.

예컨대

**시스템 요약**

> the cat found under the bed

**참조 요약**

>  the cat was under the bed

개별 단어에만 집중해 성능을 평가한다면 두 요약 간 겹치는 단어는 총 6개다. 그러나 이 6은 성능 지표로 바로 사용하기에 적합하지 않다. 우리는 이 6이라는 숫자를 이용해 Recall 과 Precision을 계산해야 한다.



### ROGUE에서 Precision과 Recall의 의미

Recall은 참조 요약본을 구성하는 단어 중 몇 개의 단어가 시스템 요약본의 단어들과 겹치는지 보는 점수다.
$$
Recall = \frac{Number\ of \ overlapped \ words} {Total\ words\ in\ reference\ summary}
$$
unigram을 하나의 단어로 계산하면 앞선 예제의 Recall 점수는 6/6으로 1이다.



Recall 점수에 따르면 언뜻 보기에 좋은 모델로 보인다. 그러나 만약, 모델이 생성한 시스템 요약본이 엄청 긴 문장일 경우 요약문이 참조 요약문과 크게 관련 없을 지라도 참조 요약분의 단어 대부분을 포함할 가능성이 커진다. 



이 문제를 해결하기 위해 Precision을 계산한다. Precision은 Recall과 반대로 모델이 생성한 시스템 요약본 중 참조 요약본과 겹치는 단어들이 얼마나 많이 존재하는지 보고자 한다.
$$
Precision = \frac{Number\ of \ overlapped \ words} {Total\ words\ in\ system\ summary}
$$


위 예시에서 Precision은 0.86이다.



다음과 같은 시스템 요약문을 생각해보자.

**시스템 요약2**

> the tiny little cat was found under the big funny bed



이때 Precision은 0.55이다. 위 요약의 경우 모델이 생성한 시스템 요약 내에 불필요한 단어가 너무 많이 존재하기 때문에 좋은 점수를 받지 못했다. 즉 간결한 요약문을 생성해내야 한다면 Precision이 좋은 성능 지표로 사용될 수 있다.



### ROGUE-N

ROGUE-1은 시스템 요약본과 참조 요약본 간 겹치는 unigram의 수를 본다 ROGUE-2 는 시스템 요약본과 참조 요약본 간 겹치는 수를 보는 지표다.

**시스템 요약(bigrams)**

> the cat, cat was, was found, found under, under the, the bed

**참조 요약(bigrams)**

> the cat, cat was, was under, under the, the bed



ROGUE-2의 Recall은 0.8, Precision은 0.67이다.	