// A simple example of the switch.
class SampleSwitchWithEmptyCase {
    public static void main(String args[]) {
	for(int i=0; i<6; i++)
	    switch(i) {
	    case 0:
		System.out.println("i is zero.");
		break;
	    case 1:
	    case 2:
		System.out.println("i is two.");
		break;
	    case 3:
		System.out.println("i is three.");
 		break;
	    default: // see default. no matching condition redirects here.
		System.out.println("i is greater than 3.");
	    }
    }
}