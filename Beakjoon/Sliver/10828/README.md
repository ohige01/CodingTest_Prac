<h2><a href="https://www.acmicpc.net/problem/10828">🚀10828번 문제</a></h2>

![image](https://github.com/user-attachments/assets/3cf0d206-de54-4ed0-8282-676534fa5cb9)
<h2>🛠️로직설명</h2>

<h2>📝오답노트</h2>

![image](https://github.com/user-attachments/assets/fb1edad5-e0d3-4ced-be23-a28beb778322)
<details>
  <summary><b> 1,2번 시도</b></summary>
    <pre>
      <code >
  # 스택 선언
  list_s = []
  # 입력
  for i in range(int(input())):
      menu = list(map(str, input().split(" ")))
      #push
      if(menu[0] == "push"):
          list_s.append(int(menu[1]))

  ...중략...
      </code>
    </pre>
  해당 방식으로 for문안에 <code>input()</code> 넣으면, 시간 초과가 뜬다.<br><br>
  그 이유는 input의 처리 방식이 입력되는 글자들을 하나씩 버퍼에 저장하는 형식으로 넣기 떄문이다.<br>
  또한, input은 개행문자를 처리하여 반환하기 때문에 이 동작을 수행하는데 시간을 소요하게 된다.<br><br>
  따라서, for문으로 입력값을 받아야 한다면, <code>input()</code>으로 받기 보단 <code>sys.stdin.readline()</code>으로 받는 것이 시간면에서 효율적이다.<br>

  <h3>✨참고자료</h3>
  1. <a href="https://malwareanalysis.tistory.com/156">input()과 sys.stdin.readline() 속도비교</a><br>
  2. <a href="https://malwareanalysis.tistory.com/156">[Python] Input vs. sys.stdin.readline 차이점?</a><br>
</details>
<br><br>
