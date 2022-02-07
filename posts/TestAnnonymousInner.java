class Person{
    void eat(){};

    void helloWorld (){
	System.out.println ("hello world");
    };
}

class TestAnnonymousInner{
    public static void main(String args[]){
	Person p=new Person(){

		@Override
		void eat(){System.out.println("nice fruits");}
	    };

	p.eat();
	p.helloWorld ();
    }
}