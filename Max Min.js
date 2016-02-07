function processData(input) {
    //Enter your code here
    input=input.split("\n");
    var n=parseInt(input[0]);
    var k=parseInt(input[1]);
    var nums=[];
    var nums2=[];
    for(i=2;i<2+n;i++)
    {
        nums.push(parseInt(input[i]));
        nums2.push(parseInt(input[i]));
    }
    nums2.sort(function(a,b){return a-b;});
    var diff=[];
    for(i=1;i<nums2.length;i++)
        diff.push(nums2[i]-nums2[i-1]);
    var mindiff=Number.MAX_VALUE;
    for(i=0;i<diff.length-k+2;i++)
    {
        var sum=0;
        for(j=0;j<k-1;j++)
            sum+=diff[i+j];
        mindiff=Math.min(mindiff,sum);
    }    
    console.log(mindiff);
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
