import java.util.List;
import java.util.ArrayList;

class PassFunction {
    public static void main(String arg[]) {
	List<Integer> myList = new ArrayList();

	myList.add(1);
	myList.add(2);
	myList.add(3);
	myList.add(1);
	myList.add(2);
	myList.add(3);

	myList.stream()
	    .forEach(System.out::println);
    }
}		  