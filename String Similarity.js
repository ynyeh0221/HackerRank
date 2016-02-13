//time-out

function processData(input) {
    //Enter your code here
    input=input.split("\n");
    for(i=1;i<=parseInt(input[0]);i++)
    {
        var s=input[i].split("");
        var s2=input[i].split("");
        var first=s[0];
        s2[0]=0;
        var ind=s2.indexOf(first);
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
            ind=s2.indexOf(first);
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
