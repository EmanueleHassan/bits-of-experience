import java.util.List;
import java.util.ArrayList;

class ParamBeh {

    private static int sum = 0;

    public static void main(String arg[]) {

	List<Integer> myList = new ArrayList<>();

	myList.add(1);
	myList.add(2);
	myList.add(3);
	myList.add(1);
	myList.add(2);
	myList.add(3);

	myList.stream()
	      .forEach(x -> {sum = mySum(x, sum);});

	System.out.println("final sum is: " + sum);
    }

    private static Integer mySum(Integer x, Integer sum){
	sum += x;

	return sum;


    }    

}		  