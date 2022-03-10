import java.util.Optional;

class myClass {

    public static void main(String args[]) {

	Optional<String> opt = Optional.empty();

	opt.ifPresentOrElse(
			    value -> System.out.println("Found: " + value),
			    () -> System.out.println("Not found")
			    );


	opt =  Optional.of("baeldung");;

	opt.ifPresentOrElse(
			    value -> System.out.println("Found: " + value),
			    () -> System.out.println("Not found")
			    );

	String name = null;
	opt = Optional.ofNullable(name);
	opt.ifPresentOrElse(
			    value -> System.out.println("Found: " + value),
			    () -> System.out.println("Not found")
			    );
	
    }
}