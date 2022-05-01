class MySumTest {

    // public interface
    @FunctionalInterface
    public static interface ICallback {
	public void sum(Integer i);

	default public void world(){
	    System.out.println("hello world");
	};

    };

    private static void myGenericMethod(ICallback callback, Integer i, Integer y){

	//consider checking if runnable != null to avoid NPE
	if (y % 2 == 0){
	    callback.sum(i);
	}
	else{
	    callback.world();
		}

	
	
    }      
    
    public static void main(String arg[]) {

	Integer i = 0;

	while (i < 5) {
	    myGenericMethod((x) -> {
		    System.out.println(x * x); // implements the functional interface
		}, 2, i);

	    i++;
	    
	}
    }
}
