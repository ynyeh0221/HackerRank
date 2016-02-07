function processData(input) {
    //Enter your code here
    input=input.split("\n");
    var s1=input[1].split(" ");
    var s2=input[2].split(" ");
    s1.splice(0,0,1);
    s2.splice(0,0,1);
    var T=[];
    var prev=[];
    for(i=0;i<=s1.length;i++)
    {
        var element=[];
        for(j=0;j<=s2.length;j++)
            element.push(0);
        T.push(element);
    }
    for(i=0;i<=s1.length;i++)
    {
        var element2=[];
        for(j=0;j<=s2.length;j++)
            element2.push(0);
        prev.push(element2);
    }
    //let -1 be left-up, -2 be left, -3 be up
    for(i=1;i<=s1.length;i++)
    {
        for(j=1;j<=s2.length;j++)
        {
            if(s1[i]==s2[j])
            {
                T[i][j]=T[i-1][j-1]+1;
                prev[i][j]=-1;
            }
            else
            {
                if(T[i-1][j]>T[i][j-1])
                {
                    T[i][j]=T[i-1][j];
                    prev[i][j]=-3;
                }
                else
                {
                    T[i][j]=T[i][j-1];
                    prev[i][j]=-2;
                }
            }
        }
    }
    //console.log(prev);
    var seq=[];
    var print_LCS=function(k, l)
    {
        if(k==0 || l==0) return;
 
        if (prev[k][l]==-1)
        {
            print_LCS(k-1, l-1);
            seq.push(s1[k]);
        }
        else if (prev[k][l]==-3)
            print_LCS(k-1, l);
        else if (prev[k][l]==-2)
            print_LCS(k, l-1);
    };
    print_LCS(s1.length,s2.length);
    console.log(seq.join(" "));
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
