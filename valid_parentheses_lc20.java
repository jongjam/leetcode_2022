class valid_parentheses_lc20 {
public boolean isValid(String s) {
        Stack<Character> st = new Stack();
        
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '{' || s.charAt(i) == '(' || s.charAt(i) == '[') {
                st.push(s.charAt(i));
            } //so whenever I find an opening paren, I push it on top of the stack.
            //now I know I want a stack, because the order starts from right next to each to outwards
            else {
                if (st.isEmpty() || ) {
                    return false; 
                }
                char cur = s.charAt(i);
                char t = st.pop();
                if (cur == '}' ) {
                    if (t != '{' ) {
                        return false;
                    }
                } else if (cur == ']') {
                    if (t != '[') {
                        return false;
                    }
                } else if (cur == ')') {
                    if (t != '('){
                        return false;
                    }
                }
            }
        }
        return st.isEmpty(); 
    }
}