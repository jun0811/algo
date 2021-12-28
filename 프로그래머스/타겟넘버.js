function solution(numbers, target) {
    var answer = 0;
    const len = numbers.length
    function dfs(v, value){
        const cur = numbers[v]
        if (v == len){
            if (value == target) answer ++
            return
        }
        
        dfs(v+1, value+cur)
        dfs(v+1, value-cur)
        
    }
    dfs(0, 0)
    
    return answer;
}