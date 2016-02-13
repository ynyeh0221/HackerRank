function processData(input) {
    //Enter your code here
    var n=parseInt(input);
    function primeFactorization(num)
    {
        var root = Math.sqrt(num),
        result = arguments[1] || [],
        x = 2;  
        if(num % x)
        {
            x = 3;
            while((num % x) && ((x = x + 2) < root)){}
        }
        x = (x <= root) ? x : num;
        result.push(x.toString());
        return (x === num) ? result : primeFactorization(num/x, result);
    }
    var primes=primeFactorization(n);
    var nstr=n.toString();
    var sum1=0;
    var sum2=0;
    for(i=0;i<nstr.length;i++)
        sum1+=parseInt(nstr[i]);
    for(i=0;i<primes.length;i++)
    {
        for(j=0;j<primes[i].length;j++)
            sum2+=parseInt(primes[i][j]);
    }
    if(sum1==sum2)
        console.log(1);
    else
        console.log(0);
} 

process.stdin.resume();
process.stdin.setEncoding("ascii");
_input = "";
process.stdin.on("data", function (input) {
    _input += input;
});

process.stdin.on("end", function () {
   processData(_input);
});
