public class Solution {
    /**
     * @param s : A string
     * @return : A string
     */
    void reverse(char[] src, int start, int end) {
        while (start >= 0 && end <= src.length -1 && start < end) {
            char temp = src[start];
            src[start] = src[end];
            src[end] = temp;
            start++;
            end--;
        }
    }
    public String reverseWords(String s) {
        // write your code
        if (s == null || s.length() <= 1) return s;

        //char[] src = s.toCharArray();
        // int wEnd = src.length - 1;
        // int wStart = 0;
        // reverse(src, 0, wEnd);
        // for (int i = 0; i < src.length; i++) {
        //     if (src[i] != ' ') {
        //         wStart = i;
        //         while (i < src.length && src[i] != ' ') {
        //             i++;
        //         }
        //         i--;
        //          reverse(src, wStart, i);

        //     }

        // }

        // return String.valueOf(src);
        StringBuilder sb = new StringBuilder();
        int wEnd = 0;
        for (int i =  s.length() - 1; i >=0 ; i--) {
            if (s.charAt(i) != ' ') {
                if (sb.length() != 0) {
                    sb.append(' ');
                }
                wEnd = i;
                while(i >= 0 && s.charAt(i) != ' ') {
                    i--;
                }
                sb.append(s.substring(i+1, wEnd+1));

            }

        }
        return sb.toString();

    }
}