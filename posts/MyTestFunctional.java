class MyTestFunctional {

    // public interface
    @FunctionalInterface
    public static interface ICallback {
	public void hello();

	default public void world(){
	    System.out.println("hello world");
	};

    };

    private static void myGenericMethod(ICallback callback, Integer i){
	//consider checking if runnable != null to avoid NPE

	if (i % 2 == 0) 
	    callback.hello();
	else
	    callback.world();
	
    }      
    
    public static void main(String arg[]) {

	Integer i = 0;

	while (i < 5){
	    
	    myGenericMethod(() -> {
		    //do something fancy
		    System.out.println("baubab"); // implements the functional interface
		}, i);

	    i++;
	} 
    }
}
