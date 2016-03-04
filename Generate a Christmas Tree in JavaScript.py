function processData(input) {
    //Enter your code here
    console.log("        *        "); 
    console.log("        0        ");
    console.log("       000       ");
    console.log("      00000      ");
    console.log("     0000000     ");
    console.log("    000000000    ");
    console.log("   00000000000   ");
    console.log("  0000000000000  ");
    console.log(" 000000000000000 ");
    console.log("00000000000000000");
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
