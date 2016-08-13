function processData(input) {
    //Enter your code here
    if (input == 1)
    {
        console.log(1);
        return;
    }
    let lucky = 1;
    for (let i = 2; i <= 2 * input; i++)
    {
        let temp = i.toString();
        if (temp.indexOf('4') == -1 && temp.indexOf('13') == -1)
            lucky += 1;
        if (lucky == input)
        {
            console.log(i);
            return;
        }            
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
