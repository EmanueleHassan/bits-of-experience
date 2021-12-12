import java.util.function.Predicate;
import java.util.List;
import java.util.Arrays;

class CleanCodeFunctional {

    public static void main(String arg[]) {

	final Predicate<String> checkIfStartsWith(final String letter) {
	    return name -> name.startsWith(letter);
	};
    
	final List<String> friends =
	    Arrays.asList("Brian", "Nate", "Neal", "Raju", "Sara", "Scott");
	final List<String> editors =
	    Arrays.asList("Brian", "Jackie", "John", "Mike");
	final List<String> comrades =
	    Arrays.asList("Kate", "Ken", "Nick", "Paula", "Zach");

	final long countFriendsStartN =
	    friends.stream()
	    .filter(checkIfStartsWith("N")).count();

	final long countFriendsStartB =
	    friends.stream()
	    .filter(checkIfStartsWith("B")).count();

	System.out.println(String.format("Number starting with N: %d", countFriendsStartN));
	System.out.println(String.format("Number starting with B: %d", countFriendsStartB));	
    }
}