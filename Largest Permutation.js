//Got time-out on the last three test case

var maximum=function(arr, start, end)
{
    var max = arr[start];
    var index = start;
    for(i=start+1; i<end; i++)
    {
        if(arr[i]>max)
        {
            max = arr[i];
            index = i;
        }
    }
    return index;
}

var swap=function(a, b)
{
    var temp=a;
    a = b;
    b = temp;
    return [a,b];
}

var largest_permutation=function(arr, n, k)
{
    for(j=0; j<n; j++)
    {
        var pos = maximum(arr,j,n);
        if(k>0 && pos!=j)
        {
            var res=swap(arr[pos], arr[j]);            
            arr[pos]=res[0];
            arr[j]=res[1];
            k--;
        }
    }
    return arr;
};

function processData(input) {
    //Enter your code here
    input=input.split("\n");
    input[0]=input[0].split(" ");
    var k=parseInt(input[0][1]);
    input[1]=input[1].split(" ");
    var nums=[];
    for(i=0;i<input[1].length;i++)
        nums.push(parseInt(input[1][i]));
    nums=largest_permutation(nums,nums.length,k);
    console.log(nums.join(" "));
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
