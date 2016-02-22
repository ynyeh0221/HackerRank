function P(
	o, //array passed in as only parameter.
	w, //binary representation of iterator 0...(2^n)-1 (see 's' below)
	e, //represents an iterator that loops through each bit in w 
	r, //the powerset array that will be returned, an array of subset arrays
	s, //iterator that steps -1 as ((2^n)-1)...0
	E, //the length of the original set
	t  //accounts for lack of preceding 0's in w.  For example (1).toString(2) == "1", not "001"
) {

	for(r=[s=1<<(E=o.length)];s;) 	//initialize r=[(2^n)].

		for(w=s.toString(2), 		//Store binary representaion
			e=t=w.length,		//Length of the binary (see parameter t)
			r[--s]=[];		//new subset
		e;)				//e iterates over (t-1)...0

			~-w[--e]||		//if bit in position e is 1
			r[s].push(o[e+E-t]);	// ... add respective set item to subset
						// ... NOTE: the subset order is reversed

	return r				//return the powerset
}

function isPrime(value) {
    for(var i = 2; i < value; i++) {
        if(value % i === 0) {
            return false;
        }
    }
    return value > 1;
}

function processData(input) {
    //Enter your code here
    input=input.split("\n");
    input[1]=input[1].split(" ");
    var ps=P(input[1]);
    var result=[];
    for(i=0;i<ps.length-1;i++)
    {
        var sum=0;
        for(j=0;j<ps[i].length;j++)
            sum+=parseInt(ps[i][j]);
        if(isPrime(sum) && result.indexOf(sum)==-1)
            result.push(sum);
    }
    console.log(result.length);
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
