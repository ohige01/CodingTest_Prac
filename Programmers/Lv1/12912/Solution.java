class Solution {
    public long solution(int a, int b) {
        long answer = a;
        while(a != b){
            if(a > b)
                a--;
            else if(a < b)
                a++;
            answer += a;
        }
        return answer;
    }
}