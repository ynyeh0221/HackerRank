function processData(input) {
    //Enter your code here
    input=input.split("\n");
    input[0]=input[0].split(" ");
    var n=parseInt(input[0][0]);
    var k=parseInt(input[0][1]);
    var num=input[1].split(" ");
    for(i=0;i<n;i++)
        num[i]=parseInt(num[i]);
    var cur_page=1;
    var pages=[];
    for(i=0;i<n;i++)
    {
        pages.push([]);
        var count=1;
        for(j=1;j<=num[i];j++)
        {
            if(count<=k)
            {
                if(count==k)
                {
                    pages[pages.length-1].push(j);
                    if(j!=num[i])
                        pages.push([]);
                    count=1;
                }
                else
                {
                    pages[pages.length-1].push(j);
                    count++;
                }
            }
        }
    }
    var sum=0;
    for(i=0;i<pages.length;i++)
    {
        if(pages[i].indexOf(i+1)!=-1)
            sum++;
    }
    console.log(sum);
    
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
