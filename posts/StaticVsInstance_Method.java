import java.util.List;
import java.util.ArrayList;

class StaticVsInstance_Method {

    public static void chainHello (String x){

	System.out.println("hello " + x);

    }
    
    public static void main (String args[]){

	List<String> myList = new ArrayList();

	myList.add("romeo");
	myList.add("gatto colosseo");	


	myList.stream()
	      .forEach(x -> System.out.println(x.substring(2)));

	myList.stream()
	      .forEach(x -> System.out.println(String.format("Hello %s", x)));

    }

}