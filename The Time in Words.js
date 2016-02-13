process.stdin.resume();
process.stdin.setEncoding('ascii');

var input_stdin = "";
var input_stdin_array = "";
var input_currentline = 0;

process.stdin.on('data', function (data) {
    input_stdin += data;
});

process.stdin.on('end', function () {
    input_stdin_array = input_stdin.split("\n");
    main();    
});

function readLine() {
    return input_stdin_array[input_currentline++];
}

/////////////// ignore above this line ////////////////////

times = {
     1: 'one minute',
     2: 'two minutes',
     3: 'three minutes',
     4: 'four minutes',
     5: 'five minutes',
     6: 'six minutes',
     7: 'seven minutes',
     8: 'eight minutes',
     9: 'nine minutes',
    10: 'ten minutes',
    11: 'eleven minutes',
    12: 'twelve minutes',
    13: 'thirteen minutes',
    14: 'fourteen minutes',
    15: 'quarter',
    16: 'sixteen minutes',
    17: 'seventeen minutes',
    18: 'eighteen minutes',
    19: 'nineteen minutes',
    20: 'twenty minutes',
    21: 'twenty one minutes',
    22: 'twenty two minutes',
    23: 'twenty three minutes',
    24: 'twenty four minutes',
    25: 'twenty five minutes',
    26: 'twenty six minutes',
    27: 'twenty seven minutes',
    28: 'twenty eight minutes',
    29: 'twenty nine minutes',
    30: 'half'
}

hour_words = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
   10: 'ten',
   11: 'eleven',
   12: 'twelve',
}


function main() {
    var hours = parseInt(readLine());
    var minutes = parseInt(readLine());
    var min_word=0;
    if(minutes > 30)
        min_word=60-minutes;
    else
        min_word=minutes;
    if(minutes===0)
        console.log(hour_words[hours] + " o' clock");
    else
    {
        var words=times[min_word];
        if(minutes<=30)
            words+=' past '+hour_words[hours];
        else
            words+=' to '+hour_words[hours+1];
        console.log(words);
    }
}
