<h2><a href="https://www.acmicpc.net/problem/12904">🚀12904번 문제</a></h2>

![image](https://github.com/user-attachments/assets/bff2f286-b9a5-47ff-879f-6ff76b4a4be6)

<h2>🛠️로직설명</h2>
첫번째로 주어지는 입력값에서 주어진 두개의 동작으로 마지막 문자열을 만들어야 한다.<br>

<h2>📝오답노트</h2>

![image](https://github.com/user-attachments/assets/c9836ac2-bf48-463a-b92b-7006751e559c)
<details>
  <summary><b>첫번째,두번째 시도</b></summary>
  <br>  
  위 두 풀이는 첫 입력에서 마지막 문자열로 가는 방식으로 풀었다<br>
  하지만 첫 문자열로 결과를 만드는데 한가지의 방법만 있는게 아니어서, 역순으로 결과를 초기 상태로 돌리는 것이 고려해야 할 가짓수가 현저히 적다.<br><br>
  따라서, 뒤에 문자열이 'A'라면 마지막 문자를 삭제하고 'B'라면 삭제 연산을 한 뒤 문자열을 뒤집으며, 처음 문자열로 돌아가는지 확인한다.<br>
</details>
<br><br>
