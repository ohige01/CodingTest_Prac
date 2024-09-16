<h2><a href="https://www.acmicpc.net/problem/2504">🚀2504번 문제</a></h2>

![image](https://github.com/user-attachments/assets/4bfb3fde-7e76-48a0-9e54-819f00e2a63a)

<h2>🛠️로직설명</h2>
<h3>곱하기를 하는 경우</h3>
여는 괄호 이후 닫는 괄호를 만난 경우 -> '(' 나 '['를 만났을 때 연산자와 연산될 값을 스택에 넣고, ')' 나 ']'를 만났을 때 연산을 실행한 뒤의 결과값을 스택에 넣는다.
<h3>더하기를 하는 경우</h3>
닫는 괄호 이후 여는 괄호를 만난 경우 -> '(', '[' 이전의 값이 ')',']'라면 덧셈 연산을 스택에 삽입, 추후 닫는 괄호를 만났을 때, 덧셈이 스택에서 <code>pop()</code>된다면, 해당 연산을 실행 
<h3>테스트 케이스 연산 순서</h3>
<details>
  <summary><b>(()[[]])()</b></summary>
  <b>stack</b>: *2, *2, pop, +, *3, *3, pop, pop, pop(+), pop, +, *2, pop <br>
  <b>expect_cal</b> =  (2*1) * ((2*1) + (3*1) * (3*1)) + (2*1) 
</details>
<details>
  <summary><b>([][])()</b></summary>
  <b>stack</b>: *2, *3, pop, +, *3, pop, pop(+), pop, +, *2, pop <br>
  <b>expect_cal</b> =  (2*1) * ((3*1) + (3*1)) + (2*1)
</details>
<details>
  <summary><b>([][][])</b></summary>
  <b>stack</b>: *2, *3, pop, +, *3, pop, +, *3, pop, pop(+), pop(+), pop <br>
  <b>expect_cal</b> =  (2*1) * ((3*1) + (3*1) + (3*1))
</details>
<h2>📝오답노트</h2>

![image](https://github.com/user-attachments/assets/be8337d4-7c43-4afb-a65c-ce5e297617f2)
<details>
  <summary><b>여러 시도들</b></summary>
    <pre>
      <code >
...중략...  
  elif(op == '+'):           
      stack_num.append(stack_num.pop() + stack_num.pop())
      # +연산할 시 뒤에 있는 연산도 함께 실행
      op = stack_op.pop()
      # 다수의 +가 있을시 모두 처리
      while(op == "+"):
          stack_num.append(stack_num.pop() + stack_num.pop())
          op = stack_op.pop()
      if(op == "*2"):
          stack_num.append(stack_num.pop() * 2) 
      elif(op == "*3"):
          stack_num.append(stack_num.pop() * 3)  
...중략...
      </code>
    </pre>
  문제에 예시가 충분하지 않아 많은 시도를 했는데, 주요 실패요인은 덧셈의 연산이다.<br><br>
  +이후에 연산이 무엇이냐에 따라 얼마나 <code>pop()</code>을 진행할 것인지 설계해야 했다.<br>
  +를 연산한다면 뒤에 연산도 같이 실행해줘야 이후에 연산시에 엉뚱한 연산을 하지 않는다.<br>
  또한, +뒤에 +가 나오면 해당 연산도 모두 실행해야 하기 때문에 연속적으로 나오는 +연산을 처리해줘야 한다.<br>
  마지막으로, 깊이가 제일 얕은 괄호들은 +연산을 처리하기 힘들기 때문에 <code>sum()</code>함수를 통해 처리한다.<br>
</details>
<br><br>
