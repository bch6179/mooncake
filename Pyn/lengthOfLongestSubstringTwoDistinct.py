Idea is simple. Maintain left to right window. If third char encountered, remove the char which has the lowest position value and update left pointer to the lowest position + 1.
This solution can be easily extend to k distinct chars.

class Solution(object):
def lengthOfLongestSubstringTwoDistinct(self, s):
    """
    :type s: str
    :rtype: int
    """
    distinct = {}  # char: pos
    maxlen = 0
    left = 0
    
    for right, char in enumerate(s):
        if len(distinct) == 2 and char not in distinct:
            left = min(distinct.values()) + 1
            self.remove_lowest_char(distinct)
        distinct[char] = right
        maxlen = max(maxlen, right - left + 1)
    return maxlen

def remove_lowest_char(self, distinct):
    lowest_pos = min(distinct.values())
    for k, pos in distinct.items():
        if pos == lowest_pos:
            char = k
    distinct.pop(char)

I wonder if it costs O(n) for the remove_lowest_char function. If so, then the total time complexity should be O(n^2)

I would like to use distinct.pop(s[left - 1]) instead.

9 months ago reply quote 
0
H HORNER 
Reputation:  0
How about del distinct[s[min(distinct.values())]]

K kevinhsu 
Reputation:  274
The main idea is to maintain a sliding window with 2 unique characters. The key is to store the last occurrence of each character as the value in the hashmap. This way, whenever the size of the hashmap exceeds 2, we can traverse through the map to find the character with the left most index, and remove 1 character from our map. Since the range of characters is constrained, we should be able to find the left most index in constant time.

public class Solution {
    public int lengthOfLongestSubstringTwoDistinct(String s) {
        if(s.length() < 1) return 0;
        HashMap<Character,Integer> index = new HashMap<Character,Integer>();
        int lo = 0;
        int hi = 0;
        int maxLength = 0;
        while(hi < s.length()) {
            if(index.size() <= 2) {
                char c = s.charAt(hi);
                index.put(c, hi);
                hi++;
            }
            if(index.size() > 2) {
                int leftMost = s.length();
                for(int i : index.values()) {
                    leftMost = Math.min(leftMost,i);
                }
                char c = s.charAt(leftMost);
                index.remove(c);
                lo = leftMost+1;
            }
            maxLength = Math.max(maxLength, hi-lo);
        }
        return maxLength;
    }
}