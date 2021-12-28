function solution(n, computers) {
    var answer = 0;
    const line =[]
    const visited = []
    for (let i=0; i<n;i++){
        line.push([])
        visited.push(0)
    }
    for (let i=0; i<n;i++){
        for (let j=0; j<n;j++){
            if (i != j && computers[i][j] ==1){
                line[i].push(j)
            }
        }
    }
    function connect(v){
        visited[v] = 1
        line[v].forEach((computer) => {
            if(!visited[computer]) connect(computer) 
        })
    }
    for (let k=0; k<n; k++){
        if(!visited[k]) {
            connect(k) 
            answer++;
        }
    }
    return answer;
}