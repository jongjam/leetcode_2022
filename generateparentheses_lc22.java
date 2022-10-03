public class generateparentheses_lc22 {
    class Solution {
        public List<String> generateParenthesis(int n) {
            List<String> list = new ArrayList<>(); //
            recur (list, "", 0, 0, n);
            return list;
        }
        
        //So I know that n gives me the criteria for the amount of open and closed parentheses I need
        // What I don't know : How should I MAKE the permutations
        // What really is the correct base case?
        // Is the tree really just going left and right? 
        private void recur(List<String> list, String cur, int open, int close, int count) {
            if (cur.length() == count * 2) { //making sure we have the correct length here
                list.add(cur);
                return;
            } 
            
            if (open < count) recur(list, cur + "(", open + 1, close, count); //branching right
            if (close < open) recur(list, cur + ")", open, close + 1, count);
        } 
    }
}
