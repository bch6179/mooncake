1.   equality of counter  of letters are constant time comparason,only [256]finate number, subclass of dictionary, hash the count of each letters, each letter is the key, count number as the value 
2.   cut the time O(26) to O(1)
  while (right < s.length()) {
        //move right everytime, if the character exists in p's hash, decrease the count
        //current hash value >= 1 means the character is existing in p
        if (hash[s.charAt(right++)]-- >= 1) count--; 
        
        //when the count is down to 0, means we found the right anagram
        //then add window's left to result list
        //the number of letters count be more or less to match the count number;otherwise either not exist or < 1; smart
        if (count == 0) list.add(left);