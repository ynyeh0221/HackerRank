function processData(input) {
    //Enter your code here
    input=input.split(" ");
    var edges=[];
    for(i=0;i<input.length;i++)
        edges.push(parseInt(input[i]));
    var ACD=edges[4]+edges[3]+edges[0];
    var ABD=edges[1]+edges[5]+edges[0];
    var ABCD=edges[0]+edges[1]+edges[2]+edges[3];
    var num=0;
    if(ACD>=0 && ABD>=0 && ABCD<0)
        num=0-ABCS;
    else if(ACD>=0 && ABD<0 && ABCD>=0)
        num=0-ABD;
    else if(ACD<0 && ABD>=0 && ABCD>=0)
        num=0-ACD;
    else if(ACD>=0 && ABD<0 && ABCD<0)
        num=Math.max(0-ABD, 0-ABCD);
    else if(ACD<0 && ABD>=0 && ABCD<0)
        num=Math.max(0-ACD, 0-ABCD);
    else if(ACD<0 && ABD<0 && ABCD>=0)
        num=Math.max(0-ACD, 0-ABD);
    else if(ACD<0 && ABD<0 && ABCD<0)
        num=Math.max(0-ABD, 0-ACD, 0-ABCD);
    console.log(num);
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
