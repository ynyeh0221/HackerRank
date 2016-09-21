function processData(input) {
    //Enter your code here
    input = JSON.parse(input);
    let start1 = input.p1.start;
    let start2 = input.p2.start;
    let path1 = input.p1.path;
    let path2 = input.p2.path;
    for (let i = 0; i < Math.min(path1.length, path2.length); i++)
    {
        if (path1[i] == 'R')
            start1[0] += 1;
        else if (path1[i] == 'L')
            start1[0] -= 1;
        else if (path1[i] == 'U')
            start1[1] += 1;
        else if (path1[i] == 'D')
            start1[1] -= 1;
        if (path2[i] == 'R')
            start2[0] += 1;
        else if (path2[i] == 'L')
            start2[0] -= 1;
        else if (path2[i] == 'U')
            start2[1] += 1;
        else if (path2[i] == 'D')
            start2[1] -= 1;
        if (start1[0] == start2[0] && start1[1] == start2[1])
        {
            console.log(start1[0] + ',' + start1[1] + ' ' + (i+1));
            return;
        }
    }
    if (path1.length < path2.length)
    {
        for (let i = path1.length; i < path2.length; i++)
        {
            if (path2[i] == 'R')
                start2[0] += 1;
            else if (path2[i] == 'L')
                start2[0] -= 1;
            else if (path2[i] == 'U')
                start2[1] += 1;
            else if (path2[i] == 'D')
                start2[1] -= 1;
            if (start1[0] == start2[0] && start1[1] == start2[1])
            {
                console.log(start1[0] + ',' + start1[1] + ' ' + (path1.length+i+1));
                return;
            }
        }
    }
    else if (path1.length > path2.length)
    {
        for (let i = path2.length; i < path1.length; i++)
        {
            if (path1[i] == 'R')
                start1[0] += 1;
            else if (path1[i] == 'L')
                start1[0] -= 1;
            else if (path1[i] == 'U')
                start1[1] += 1;
            else if (path1[i] == 'D')
                start1[1] -= 1;
            if (start1[0] == start2[0] && start1[1] == start2[1])
            {
                console.log(start1[0] + ',' + start1[1] + ' ' + (path2.length+i+1));
                return;
            }
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
