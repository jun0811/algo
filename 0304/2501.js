const fs = require('fs');
const stdin = (process.platform === 'linux'
  ? fs.readFileSync('/dev/stdin').toString()
  : `6 3
  `
).split('\n');
const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();
 
let [n,k] = input().split(" ");
let arr = []
console.log(n,k)
for(let i=1; i<=n; i++){
	if (parseInt(n%i,10)==0) arr.push(i) 
}
if (arr.length<k){
	console.log(0)
}else{
  console.log(arr[k-1])
}