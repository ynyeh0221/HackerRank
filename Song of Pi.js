function processData(input) {
    //Enter your code here
    var pi="31415926535897932384626433833";
    input=input.split("\n");
    for(i=1;i<=parseInt(input[0]);i++)
    {
        var s=input[i].split(" ");
        var check=0;
        for(j=0;j<s.length;j++)
        {
            if(s[j].length!=parseInt(pi[j]))
            {
                 check=1;
                 break;
            }
        }
        if(check==0)
            console.log("Its a pi song.");
        else
            console.log("Its not a pi song.");
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
