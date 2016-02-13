function processData(input) {
    //Enter your code here
    input=input.split("\n");
    var num1=parseInt(input[0]);
    var num2=parseInt(input[1]);
    var result=[];
    for(j=num1;j<=num2;j++)
    {
        var square=Math.pow(j,2).toString();
        var r=parseInt(square.substring(square.length-j.toString().length, square.length));
        var l=parseInt(square.substring(0, square.length-j.toString().length));
        if(isNaN(l)) l=0;
        if(l+r==j)
            result.push(j);
    }
    if(result.length==0)
        console.log("INVALID RANGE");
    else
        console.log(result.join(" "));
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
