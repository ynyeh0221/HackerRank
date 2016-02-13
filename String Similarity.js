//time-out

function processData(input) {
    //Enter your code here
    input=input.split("\n");
    for(k=1;k<=parseInt(input[0]);k++)
    {
        var str=input[k];
        var len=input[k].length;
        var count=0;
        var total=0;
        for(i=1;i<len;i++)
        {
            count=0;
            for(j=i;j<len;j++)
            {
                if(str.charAt(j-i)==str.charAt(j))
                    count++;
                else
                    break;
            }
            total=total+count;
        }
        console.log(total+len);
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
