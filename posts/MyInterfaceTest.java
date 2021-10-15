interface MyInterface
{
  
  /** Were any errors found */
  default public boolean   hasErrors()  { return false; }

}

class MyClass implements MyInterface {

}


class MyInterfaceTest
{

    public static void main(String[] args){
	MyClass myObject = new MyClass();

	System.out.println("The default boolean is " + myObject.hasErrors()); 

    }
} // end of IUploader
