function solution(numbers) {
    var answer = [];
    let length = numbers.length
    numbers = numbers.split('')

    search(numbers, '')

    function search(arr, cur) {
        if (parseInt(cur) >0){
            if (isPrimary(parseInt(cur))){
                if (!answer.includes(parseInt(cur))){
                    answer.push(parseInt(cur))
                }   
            }
        }

        if (arr.length>0){
            for (let i in arr){
                let tmp = [...arr]
                let n = tmp.splice(i,1)
                search(tmp, cur+ n)
            }
        }
    }

    function isPrimary(n) {
        if (n <= 1) return false
        if (n==2) return true
        for(let i=2; i<Math.sqrt(n); i++){
            if(n%i == 0){
                return false
            }
        } 

        return true
    }



    return answer.length;
}

solution("17") // 7 17 71
solution("011") // 11 101
