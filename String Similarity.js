//time-out

function processData(input) {
    //Enter your code here
    input=input.split("\n");
    for(i=1;i<=parseInt(input[0]);i++)
    {
        var s=input[i].split("");
        var s2=input[i].split("");
        s2[0]=0;
        var ind=s2.indexOf(s[0]);
        var sum=0;
        while(ind!=-1)
        {
            for(j=ind;j<s.length;j++)
            {
                if(s[j]==s[j-ind])
                    sum++;
                else
                    break;
            }
            s2[ind]=0;
            ind=s2.indexOf(s[0]);
        }
        console.log(sum+s.length);
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
