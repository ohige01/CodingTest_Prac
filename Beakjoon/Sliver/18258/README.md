<h2><a href="https://www.acmicpc.net/problem/18258">🚀18258번 문제</a></h2>

![image](https://github.com/user-attachments/assets/f0972865-f274-4da6-957e-e95d93d46f0b)
<h2>🛠️로직설명</h2>
<h2>📝오답노트</h2>

![image](https://github.com/user-attachments/assets/bf6c01b3-5000-4903-a92a-deeadea3e720)
<details>
  <summary><b> 1번 시도</b></summary>
    <pre>
      <code >
  ...중략...   
  # 입력
  for i in range(int(input())):
      #for문에서 input 쓰면 시간초과 뜸
      menu = list(map(str, sys.stdin.readline().split()))
      #push
      if(menu[0] == "push"):
          list_s.insert(0, int(menu[1]))
  ...중략...
      </code>
    </pre>
  해당 코드처럼 <code>insert()</code> 넣으면, 시간 초과가 뜬다.<br><br>
  끝자리에 요소를 추가하는 <code>append()</code>와 달리, <code>insert()</code>는 특정 위치에 요소를 삽입하기 때문에 위치를 탐색하는 연산이 필요하다.<br>
  위 문제는 O(n^2)의 시간복잡도를 가지면 시간 초과가 뜨기 때문에 해당 매서드를 사용하면 안된다.<br> 
  
  <h3>✨참고자료</h3>
  1. <a href="https://ooyoung.tistory.com/117">append(), extend(), insert() 함수 비교</a><br>
</details>
<details>
  <summary><b> 2번 시도</b></summary>
    <pre>
      <code >
  ...중략...   
  #push
    if(menu[0] == "push"):
        list_s.append(int(menu[1]))      
  #pop
  elif(menu[0] == "pop"):
      if len(list_s) > 0 :
          print(list_s.pop(0))
      else:
          print(-1)
  #size
  elif(menu[0] == "size"):
      print(len(list_s))
  ...중략...
      </code>
    </pre>
  해당 코드처럼 <code>pop()</code>이 아니라 <code>pop(0)</code> 넣으면, 시간 초과가 뜬다.<br><br>
  두 매서드가 시간복잡도의 차이가 발생하는 이유는 <code>pop(0)</code>은 앞의 값을 제거하기 위해 전체를 복사하기 때문이다.<br>
  앞서 말했던 이유처럼 시간복잡도가 O(n)인 매서드는 시간 초과가 뜬다<br><br>
  따라서, 해당 문제에서는 매서드를 새롭게 정의하지 않는 이상 dequeue 패키지를 사용해 시간복잡도가 O(1)인 매서드를 이용해야 한다.<br>

  <h3>✨참고자료</h3>
  1. <a href="https://hyun-am-coding.tistory.com/entry/Python-list-%EC%97%B0%EC%82%B0%EC%97%90-%EB%94%B0%EB%A5%B8-%EC%8B%9C%EA%B0%84-%EB%B3%B5%EC%9E%A1%EB%8F%84">Python list 연산에 따른 시간 복잡도</a><br>
</details>
<br><br>
