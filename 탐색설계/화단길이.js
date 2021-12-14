let n  = 9
let ans = 0
for (let i = 1; i < n-1; i++) {
    for (let j = i; j <n-1; j++){
        for (let k = j; k < n-1; k++){
            if (k < i+j && i+j+k ==n ) {
                ans +=1
            }
        }
    }
}

console.log(ans)