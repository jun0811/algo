function solution(numbers, target) {
    var answer = 0;
    // const visited = new Array(numbers.length).fill(false)
    // console.log(visited)
    
    dfs(0,0)
    function dfs(i,total){
        if(i==numbers.length){
            console.log(total)
            if (total == target){
                answer+=1
            }
            return
        }
        dfs(i+1,total+numbers[i])
        dfs(i+1,total-numbers[i])
    }
    console.log(answer)
    return answer;
}

solution([1,1,1,1,1],3)