function processData(input) {
    //Enter your code here
    input=input.split("\n");
    input[1]=input[1].split(" ");
    var num1=[];
    var num2=[];
    for(i=0;i<input[1].length;i++)
    {
        num1.push(parseInt(input[1][i]));
        num2.push(parseInt(input[1][i]));
    }
    num2.sort(function(a,b){return a-b;});
    var diff=[];
    for(i=0;i<num1.length;i++)
        diff.push(num1[i]-num2[i]);
    var check=[];
    for(i=0;i<diff.length;i++)
    {
        if(diff[i]!=0)
            check.push([i,diff[i]]);
    }
    var yes=0;
    for(i=0;i<Math.floor(check.length/2);i++)
    {
        if(check[i][1]==(-1)*check[check.length-1-i][1])
            yes=1;
    }
    if(yes==1)
    {
        console.log("yes");
        if(check.length==2)
            console.log("swap "+(check[0][0]+1)+" "+(check[check.length-1][0]+1));
        else
            console.log("reverse "+(check[0][0]+1)+" "+(check[check.length-1][0]+1));
    }
    else
        console.log("no");
        
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
