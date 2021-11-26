import java.util.List;
import java.util.ArrayList;

class MyTest {

    private static int sum = 0;
    
    public static void main(String arg[]) {


	List<Integer> myList = new ArrayList<>();

	myList.add(1);
	myList.add(2);
	myList.add(3);
	myList.add(1);
	myList.add(2);
	myList.add(3);

	java.util.function.Function<Integer,Integer> MySum = (i) -> {
	    sum += i;
	    return sum;
	};

	myList.stream()
	      .forEach(x -> {sum = MySum.apply((Integer) x);}); // note the nice forEach function.

	System.out.println("final sum is: " + sum);




	// Other example of a different interface
	// java.util.function.BiConsumer<Integer, Integer> times = (i, num) -> {
	//     i *= num;
	//     System.out.println(i);
	// };
	// for (int i = 1; i < 3; i++) {
	//     times.accept(i, 2); //multiply i by 2 and print i
	//     times.accept(i, i); //square i and then print the result
	// }
    }
}