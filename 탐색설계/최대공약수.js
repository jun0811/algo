let a = 12;
let b = 16;

if (a < b ){
    let tmp;
    tmp = a
    a = b 
    b = tmp
}

while (true) { 
    let n = a%b
    if (n===0) {
        console.log(b);
        break;
    }
    else {
        a = b;
        b = n;
    }
}

