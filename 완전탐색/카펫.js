function solution(brown, yellow) {
    var answer = [];
    // 가로 
    for (let i=1; i<=yellow; i++){
        if (yellow % i ==0){
            let w = i
            let h = yellow /i // 세로 
            if ( w >= h && (2*(w+2)+2*h) == brown) {
                answer.push(w+2,h+2)
            }
        }
    }
    return answer;
}

solution(10,2) //[4,3]
solution(8,1) //[3,3]