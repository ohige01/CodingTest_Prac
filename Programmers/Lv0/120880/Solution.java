import java.util.*;

class Solution {
    public int[] solution(int[] numlist, int n) {
        Map<Integer, Integer> map = new HashMap<>();

        for (int num : numlist) {
            map.put(num, Math.abs(num - n));
        }

        List<Integer> answer = new ArrayList<>(map.keySet());

        Collections.sort(answer, (s1, s2) -> {
            if(!map.get(s1).equals(map.get(s2))){
                return map.get(s1) - map.get(s2);
            } else {
                return s2 - s1;
            }
        });

        return answer.stream()
                .mapToInt(Integer::intValue)
                .toArray();
    }
}
