import java.util.*;
class Solution {
    public boolean solution(String[] phone_book) {
        Set<String> prefix = new HashSet<>();
        Set<Integer> sizeList = new HashSet<>();
        Arrays.sort(phone_book, (o1,o2)->o1.length()-o2.length());
        
        for (String num : phone_book){
            if (prefix.contains(num)){
                return false;
            } else{
                
                
                for (int size : sizeList){
                   if (prefix.contains(num.substring(0,size))) return false;
                }
                
                
                prefix.add(num);
                sizeList.add(num.length());
            }
        }
        return true;
    }
}