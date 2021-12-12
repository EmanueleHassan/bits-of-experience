// Use an enum constructor, instance variable, and method.
enum Apple {
    Jonathan(10), GoldenDel(9), RedDel(12), Winesap(15), Cortland(8);

    private int price; // price of each apple

    // Constructor
    Apple(int p) { price = p; } // so note that here you are
				// specifying the form of the
				// constructor of apple. the above
				// constants would then refer to such
				// a constructor

    int getPrice() { return price; } // so note how you can define
				     // methods that you can use on
				     // enum objects. In fact enum is
				     // a special type of
				     // class. I.e. also enum are
				     // obejcts such that everything
				     // falls back into the frist
				     // class citizens of the app.
}
class EnumDemo4 {


    @FunctionalInterface
    interface myInterface {
	boolean run(String Name);
    }
    
    public static void main(String args[])
    {
	Apple ap;

	myInterface r = (String Name) -> {
	    for (Apple a : Apple.values()) {
		if (a.name().equals(Name)) {
		    return true;
		}
	    }
	    return false;
	};

	if (r.run("Jonathan")){
	    // Display price of Winesap.
	    System.out.println("Winesap costs " +
			       Apple.Winesap.getPrice() +
			       " cents.\n");
	    // Display all apples and prices.
	    System.out.println("All apple prices:");
	    for(Apple a : Apple.values())
		System.out.println(a + " costs " + a.getPrice() +
				   " cents.");
	}
	else if(r.run("Alberto")) {

	    System.out.println("Note this is not printed");
	    
	    // Display price of Winesap.
	    System.out.println("Winesap costs " +
			       Apple.Winesap.getPrice() +
			       " cents.\n");
	    // Display all apples and prices.
	    System.out.println("All apple prices:");
	    for(Apple a : Apple.values())
		System.out.println(a + " costs " + a.getPrice() +
				   " cents.");	    
	}
    }
}
