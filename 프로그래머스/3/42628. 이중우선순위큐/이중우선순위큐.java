import java.util.*;
class Solution {
    public int[] solution(String[] operations) {
        DoublePriorityQueue dpq = new DoublePriorityQueue();
        for (String oper : operations){
            String[] arr = oper.split(" ");
            if (arr[0].equals("I")){
                dpq.insert( Integer.parseInt(arr[1]) );
            } else if(arr[0].equals("D")){
                if (arr[1].equals("-1")){
                    dpq.deleteMin();
                } else{
                    dpq.deleteMax();
                }
            }
        }        
        
        return dpq.answer();
    }
}

class DoublePriorityQueue{
    PriorityQueue<Integer> maxHeap;
    PriorityQueue<Integer> minHeap;
    Map<Integer,Integer> maxElem;
    Map<Integer,Integer> minElem;
    
    DoublePriorityQueue(){
        this.maxHeap = new PriorityQueue<>(Collections.reverseOrder());
        this.minHeap = new PriorityQueue<>();
        this.maxElem = new HashMap<>();
        this.minElem = new HashMap<>();
    }
    
    void insert(int data){
        maxHeap.offer(data);
        minHeap.offer(data);
    }
    
    // minElem.push(data,minElem.getOrDefault(data,0)+1);
    void deleteMin(){
        while (minHeap.size()>0){
            int key = minHeap.poll();
            if (!maxElem.containsKey(key) || maxElem.get(key)==0){
                minElem.put(key,minElem.getOrDefault(key,0)+1);
                break;
            }
            maxElem.put(key, maxElem.get(key)-1);
        }
        
    }
    
    void deleteMax(){
        while (maxHeap.size()>0){
            int key = maxHeap.poll();
            if (!minElem.containsKey(key) || minElem.get(key)==0){
                maxElem.put(key,maxElem.getOrDefault(key,0)+1);
                break;
            }
            minElem.put(key, minElem.get(key)-1);
        }    
    
    }
    
    int[] answer(){
        
        int[] ans = new int[2];
        int maxKey = 0;
        int minKey = 0;
        while (maxHeap.size()>0){
            int key = maxHeap.poll();
            if (!minElem.containsKey(key) || minElem.get(key)==0){
                maxKey = key; 
                break;
            }
            minElem.put(key, minElem.get(key)-1);
        }
        
        while (minHeap.size()>0){
            int key = minHeap.poll();
            if (!maxElem.containsKey(key) || maxElem.get(key)==0){
                minKey = key; 
                break;
            }
            maxElem.put(key, maxElem.get(key)-1);
        }
        
        ans[0] = maxKey;
        ans[1] = minKey;
        
        return ans;
    }
}