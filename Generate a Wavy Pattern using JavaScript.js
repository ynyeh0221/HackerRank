function processData(input) {
    //Enter your code here
    var element="";
    for(i=0;i<14;i++)
    {
        if(i%2==0)
            element+='\u2571';
        else
            element+='\u2572';
    }
    for(j=0;j<14;j++)
        console.log(element);
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
