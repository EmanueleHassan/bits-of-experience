import java.util.regex.Pattern;

class Regex {
    public static void main(String args[]) {

	Pattern pattern = Pattern.compile("^(?!USD_A.*?(PRPYMNT)).*$");

	System.out.println(pattern.matcher("USD_ALABAMAPRPYMNT").matches());
    }
}