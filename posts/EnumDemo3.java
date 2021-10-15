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

    int getPrice() { return price; }
}
class EnumDemo3 {
    public static void main(String args[])
    {
  	Apple ap;
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