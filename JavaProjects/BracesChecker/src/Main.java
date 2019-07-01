import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        System.out.println("Input string with braces: ");
        String test = input.nextLine();
        if(BracesChecker.isCorrect(test.toCharArray())){
            System.out.println("Braces are correct");
        }
    }
}