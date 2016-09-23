function processData(input) {
    input = input.split('\n').slice(1);
    for (let i = 0; i < input.length; i++)
    {
        let stack = [];
        input[i] = input[i].split(':');
        input[i][0] = input[i][0].trim() + '.';
        input[i][1] = input[i][1].trim();
        let s = input[i][1];
        let temp = 0;
        for (let j = 0; j < s.length; j++)
        {
            if (isNumeric(s[j]))
            {
                temp = 10 * temp + parseInt(s[j], 10);
            }
            else if (s[j] == '(');
            else if (s[j] == ')')
            {
                stack.push(temp);
                temp = 0;
            }
        }
        input[i].push(stack.reduce(function(a, b) {return a + b;}, 0));
        input[i].push(i);
    }
    input.sort(function(a,b) {
        if (a[2] === b[2])
            return a[3] > b[3] ? 1 : -1;
        else
            return a[2] > b[2] ? 1 : -1;
    });
    for (let i = 0; i < input.length; i++)
        console.log(input[i][0]);
} 
    
function isNumeric(n) {
  return !isNaN(parseFloat(n)) && isFinite(n);
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
