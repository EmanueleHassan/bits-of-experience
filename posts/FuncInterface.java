import java.util.List;
import java.util.ArrayList;

class FuncInterface {

    public static interface ICallback {
	public String greeting(String hello);

	default public String greeting2() {return "My wooow Greeting";}; 

    };

    protected static void myGreeting(String message) {
	System.out.println(message + "ciaoMamma");
    };

    public static void testCallback(ICallback test) {

	List<String> myList = new ArrayList();

	myList.add("Mulan");
	myList.add("BiancaNeve");	
	myList.add("Aladdin");

	myList.stream()
	    .forEach(rs -> test.greeting(rs));
	}
    
    public static void main(String arg[]) {
	String message;

	testCallback((message) -> myGreeting(message));
    }
}
