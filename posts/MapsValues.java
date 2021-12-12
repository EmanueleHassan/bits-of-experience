import java.util.List;
import java.util.Map;
import java.util.HashMap;
import java.util.ArrayList;    

class MapsValues {
    public static void main(String args[]) {
        Map<String, Integer> map = new HashMap<>();

	map.put("a",1); // add the desired value
	map.put("b",2); // add the desired value
	map.put("c",3); // add the desired value
	map.put("d",4); // add the desired value	


	System.out.println("My set of keys");
	map.entrySet().stream()
	    .forEach(d -> System.out.println(d.getKey()));

	System.out.println("My set of keys - Method 2");
	map.keySet().stream()
	    .forEach(System.out::println);

	System.out.println("My set of values");
	map.entrySet().stream()
	    .forEach(d -> System.out.println(d.getValue()));

	System.out.println("My set of values - Method 2");
	map.values().stream().forEach(System.out::println);
    }
}