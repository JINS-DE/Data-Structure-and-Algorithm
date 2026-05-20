import java.util.*;
class Solution {
    public int solution(int[][] jobs) {
        Arrays.sort(jobs,(o1,o2)->o1[0]-o2[0]);
        Queue<Job> q = new LinkedList<>();
        for (int i = 0; i < jobs.length; i++){
            Job j = new Job(jobs[i][1], jobs[i][0], i);
            q.offer(j);
        }
        
        PriorityQueue<Job> watingQ = new PriorityQueue<>();
        int lastTime=0;
        int total = 0;
        while (!q.isEmpty() || !watingQ.isEmpty()){
            // 1. 작업 중이 아닐 때
            if (watingQ.isEmpty() && !q.isEmpty() && q.peek().req > lastTime){
                lastTime = q.peek().req;
            }
            // 2. 작업 중일 때
            while(!q.isEmpty() && q.peek().req <= lastTime){
                watingQ.offer(q.poll());
            }
            Job job = watingQ.poll();
            lastTime += job.using;
            total += lastTime - job.req;

        }
        return total/jobs.length;
    }
}
class Job implements Comparable<Job>{
    int using;
    int req;
    int idx;
    Job (int u, int r, int i){
        this.using = u;
        this.req = r;
        this.idx = i;
    }
    @Override
    public int compareTo(Job other){
        if (this.using == other.using){
            if (this.req == other.req){
                return this.idx-other.idx;
            }
            return this.req - other.req;
        }
        return this.using - other.using;
    }
    
}