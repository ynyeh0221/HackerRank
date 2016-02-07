function processData(input) {
    //Enter your code here
    input=input.split("\n");
    input[0]=input[0].split(" ");
    var coins=input[1].split(" ");
    var n=parseInt(input[0][0]);
    var T=[];
    for(i=0;i<n+1;i++)
    {
        var element=[];
        for(j=0;j<coins.length;j++)
            element.push(0);
        T.push(element);
    }
    for(j=0;j<coins.length;j++)
        T[0][j]=1;
    
    for(i=1;i<n+1;i++)
    {
        for(j=0;j<coins.length;j++)
        {
            var x=0;
            var y=0;
            if(i-coins[j] >= 0)
                x=T[i - coins[j]][j];
            if(j>=1)
                y=T[i][j-1];
            T[i][j]=x+y;
        }
    }
    console.log(T[n][coins.length-1])
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
