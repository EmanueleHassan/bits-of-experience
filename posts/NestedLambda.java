import java.util.List;
import java.util.Map;
import java.util.HashMap;
import java.util.ArrayList;    

class NestedLambda {
    public static void main(String args[]) {
        Map<String, Map<String, Integer>> map = new HashMap<>();

	Map<String, Integer> map2 = new HashMap<>();

	Map<String, Integer> map3 = new HashMap<>();	

	map2.put("a",1); // add the desired value
	map2.put("b",2); // add the desired value
	map2.put("c",3); // add the desired value
	map2.put("d",4); // add the desired value


	map3.put("e",5); // add the desired value
	map3.put("f",6); // add the desired value
	map3.put("g",7); // add the desired value
	map3.put("h",8); // add the desired value	

	map.put("hello", map2);
	map.put("balloon", map3);

 	map.values().stream()
	    .forEach(d -> d.entrySet().stream().forEach(m -> System.out.println(m.getKey())));

	// note d is easily accessible in the second stream
 	map.values().stream()
	    .forEach(d -> d.entrySet().stream().forEach(m -> d.put(m.getKey(), 0 )));	

 	map.values().stream()
	    .forEach(d -> d.entrySet().stream().forEach(m -> System.out.println(m.getValue())));
    }
}