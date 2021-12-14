/**
 * 아래와 같이 5와 사칙연산만으로 12를 표현할 수 있습니다.

12 = 5 + 5 + (5 / 5) + (5 / 5)
12 = 55 / 5 + 5 / 5
12 = (55 + 5) / 5

5를 사용한 횟수는 각각 6,5,4 입니다. 그리고 이중 가장 작은 경우는 4입니다.
이처럼 숫자 N과 number가 주어질 때, N과 사칙연산만 사용해서 표현 할 수 있는 방법 중 N 사용횟수의 최솟값을 
return 하도록 solution 함수를 작성하세요.
 */
function solution(N, number) {
    var answer = 0;
    const set = Array(9).fill().map(()=>new Set())

    for(let i=1; i<9; i++){
        set[i].add(Number(N.toString().repeat(i)))
        
        for(let j =1; j<i; j++){
            for(const arg1 of set[j]){
                for(const arg2 of set[i-j]){
                    set[i].add(arg1 + arg2)
                    set[i].add(arg1 * arg2)
                    set[i].add(arg1 - arg2)
                    set[i].add(arg1 / arg2)
                }
            }
        }
        if (set[i].has(number)) {
        console.log(set[i])    
        return i}
    }

    return -1;
}

let a =solution(5,12) //4 
solution(2,11) //3
console.log(a)