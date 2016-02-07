function processData(input) {
    //Enter your code here
    input=input.split("\n");
    for(i=1;i<=2*parseInt(input[0]);i=i+2)
    {
        input[i]=input[i].split(" ");
        var values=input[i+1].split(" ");
        var K=parseInt(input[i][1]);
        var T=[];
        for(j=0;j<K+1;j++)
            T.push(0);
        for(b=1;b<=K;b++)
        {
            for(j=0;j<values.length;j++)
            {
                if(b>=values[j])
                    T[b]=Math.max(T[b], parseInt(values[j])+T[b-parseInt(values[j])]);
            }
        }
        console.log(T[K]);
    }
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
