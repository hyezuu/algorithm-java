import java.util.*;

class Solution {
    public int[] solution(int[] arr) {

		List<Integer> list = new ArrayList<>();

		for (int i = 0; i < arr.length; i++) {
			for (int j = 0; j < arr[i]; j++) {
				list.add(arr[i]);
			}
		}

		int[] resultArray = new int[list.size()];
		for (int i = 0; i < list.size(); i++) {
			resultArray[i] = list.get(i);
		}
        
        return resultArray;
    }
}
