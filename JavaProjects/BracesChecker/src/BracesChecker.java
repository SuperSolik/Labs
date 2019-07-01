import utilites.Stack;

public class BracesChecker {
    static Stack<Character> stack = new Stack<>();

    public static boolean isCorrect(char[] test){
        for (Character c : test) {
            if (c == '{' || c == '(' || c == '[') {
                stack.push(c);
            } else if(c != '}' && c != ')' && c != ']'){
                continue;
            } else {
                if(stack.isEmpty()){
                    System.out.println("Missing " + oppositeBracket(c));
                    return false;
                }
                if(oppositeBracket(c) != stack.top()){
                    System.out.println("Missing " + oppositeBracket(stack.top()));
                    return false;
                }
                stack.pop();
            }
        }
        if(!stack.isEmpty()){
            System.out.println("Missing " + oppositeBracket(stack.top()));
            return false;
        }
        return true;
    }

    private static Character oppositeBracket(Character bracket){
        if (bracket == '(') return ')';
        else if (bracket == ')') return '(';
        else if (bracket == '}') return '{';
        else if (bracket == '{') return '}';
        else if (bracket == '[') return ']';
        else return '[';
    }
}
