function processData(input) {
    //Enter your code here
    input=input.split("\n");
    for(i=1;i<=2*parseInt(input[0]);i=i+2)
    {
        var check=0;
        var a=input[i].split("").sort();
        var b=input[i+1].split("").sort();
        if(a.length<b.length)
        {
            for(j=0;j<a.length;j++)
            {
                if(a[j]!=a[j-1] && b.indexOf(a[j])!=-1)
                {
                    check=1;
                    break;
                }
            }
        }
        else
        {
            for(j=0;j<b.length;j++)
            {
                if(b[j]!=b[j-1] && a.indexOf(b[j])!=-1)
                {
                    check=1;
                    break;
                }
            }
        }

        if(check==1)
            console.log("YES");
        else
            console.log("NO");
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
