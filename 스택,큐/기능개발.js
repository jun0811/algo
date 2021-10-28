//https://programmers.co.kr/learn/courses/30/lessons/42586?language=javascript
function solution(progresses, speeds) {
    var answer = [];
    let length = progresses.length;
    let s = -1
    let cur = 0
    while (cur !=length) {
        s = parseInt(( 100 - progresses[cur] ) / speeds[cur]) < ( 100 -  progresses[cur] ) / speeds[cur] 
        ? parseInt(( 100 -  progresses[cur] ) / speeds[cur])+1 : parseInt(( 100 -  progresses[cur] ) / speeds[cur]) 
        let i = cur;
        for(;i<length;i++){
            progresses[i] += (speeds[i] * s)
        }
        let cnt = 0 
        let tmp = progresses.slice(cur)

        for(let i =0; i <tmp.length;i++){
            if(tmp[i]<100) break 
            cnt += 1
        }
        cur += cnt
        answer.push(cnt)
    }
    return answer;
}
console.log(solution([93,30,55],[1,30,5]));