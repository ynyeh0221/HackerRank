//time-out

function processData(input) {
    //Enter your code here
    input=input.split("\n")
    for(i=1;i<=parseInt(input[0]);i++)
    {
        input[i]=input[i].split(" ");
        var a=parseInt(input[i][0]);
        var b=parseInt(input[i][1]);
        var sum=0;
        for(j=a;j<=b;j++)
        {
            var binary=(j>>>0).toString(2);
            //console.log(a,b,binary);
            for(k=0;k<binary.length;k++)
            {
                if(binary.charAt(k)=='1')
                    sum++;
            }
        }
        console.log(sum);
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
