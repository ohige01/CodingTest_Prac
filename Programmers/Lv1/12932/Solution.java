import java.util.*;

class Solution {
    public int[] solution(long n) {
        List<Integer> answer = new ArrayList<>();

        String y = String.valueOf(n);
        for(int i = y.length() - 1; i >= 0; i--){
            answer.add(Character.getNumericValue(y.charAt(i)));
        }

        return answer.stream()
                .mapToInt(Integer::intValue)
                .toArray();
    }
}