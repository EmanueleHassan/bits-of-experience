import java.util.List;
import java.util.Map;
import java.util.HashMap;
import java.util.ArrayList;    

class MapsBasics {
    public static void main(String args[]) {
        Map<String, List<Integer>> map = new HashMap<>();

	List<Integer> myList = new ArrayList<>();

	myList.add(1); // add the desired value
	    
	map.put("hello", myList);

	if (map.containsKey("hello")) {
		List<Integer> myTest = map.get("hello");

		myTest.add(2);

		map.put("hello", myTest);
	}


	List<Integer> myTest = map.get("hello");

	myTest.stream().forEach(System.out::println);

    }
}