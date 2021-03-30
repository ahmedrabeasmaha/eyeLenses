let today = new Date();
let dd = String(today.getDate()).padStart(2, '0');
let mm = String(today.getMonth() + 1).padStart(2, '0');
let yyyy = today.getFullYear();
today = dd + "-" + mm + "-" + yyyy;
const focus = ["#id_lAxisF", "#id_lCylF", "#id_lSphF", "#id_rAxisF", "#id_rCylF", "#id_rSphF", "#id_lAxisN", "#id_lCylN", "#id_lSphN", "#id_rAxisN", "#id_rCylN", "#id_rSphN"]

function FocusClickIn(id){
    if (document.getElementById(id).getAttribute("value") === "--") {
        document.getElementById(id).setAttribute("value", "");
    }
}

function FocusOut(id){
    if (document.getElementById(id).getAttribute("value") === "") {
        document.getElementById(id).setAttribute("value", "--");
    }
}

// $(function(){
//     $("input").focus(function(){
//         for (let i = 0; i < focus.length; i++) {
//             if ($(focus[i]).val() === "") {
//                 $(focus[i]).val("--");
//             }
//         }
//     });
//
//     $("#submit").click(function(){
//         for (let i = 0; i < focus.length; i++) {
//             if ($(focus[i]).val() === "") {
//                 $(focus[i]).val("--");
//             }
//         }
//     });
// });

$("#date").datepicker({
    todayHighlight: true,
    autoclose: true,
    isRTL: true,
});

$("#revealDate").datepicker({
    todayHighlight: true,
    autoclose: true,
    isRTL: true,
});

$(function(){
    $("#reset").click(function(){
        $("input").val("");
        for (let i = 0; i < focus.length; i++) {
            if ($(focus[i]).val() === "") {
                $(focus[i]).val("--");
            }
        }
        $("#date").datepicker({
            todayHighlight: true,
            autoclose: true,
            isRTL: true,
        });
        $("#revealDate").datepicker({
            todayHighlight: true,
            autoclose: true,
            isRTL: true,
        });
    });
});

let curVal, prevVal, pressedOp, newInputToggle, display, storedOp, doTheMath, ans, displayLength, mem, num;
curVal = prevVal = storedOp, calcActive = null;
newInputToggle = true;
display = $('#display');
displayLength = 10;
mem = 0;

document.addEventListener("keydown", function(event) {
    if ($("input").is(":focus") === false){
        if (event.keyCode === 96) {
            num = 0;
            if (newInputToggle) {
                display.val('');
                newInputToggle = false;
                calcActive = true;
                storedOp = pressedOp;
            }

            if (display.val().length < 10 && (num !== '.' || (display.val().match(/\./g) || []).length < 1)) {
                display.val((display.val() + num)
                    .replace(/^0*\./, '0.'))
                console.log(num)
            }
        }
        else if (event.keyCode === 97) {
            num = 1;
            if (newInputToggle) {
                display.val('');
                newInputToggle = false;
                calcActive = true;
                storedOp = pressedOp;
            }

            if (display.val().length < 10 && (num !== '.' || (display.val().match(/\./g) || []).length < 1)) {
                display.val((display.val() + num)
                    .replace(/^0*\./, '0.'))
                console.log(num)
            }
        }
        else if (event.keyCode === 98) {
            num = 2;
            if (newInputToggle) {
                display.val('');
                newInputToggle = false;
                calcActive = true;
                storedOp = pressedOp;
            }

            if (display.val().length < 10 && (num !== '.' || (display.val().match(/\./g) || []).length < 1)) {
                display.val((display.val() + num)
                    .replace(/^0*\./, '0.'))
                console.log(num)
            }
        }
        else if (event.keyCode === 99) {
            num = 3;
            if (newInputToggle) {
                display.val('');
                newInputToggle = false;
                calcActive = true;
                storedOp = pressedOp;
            }

            if (display.val().length < 10 && (num !== '.' || (display.val().match(/\./g) || []).length < 1)) {
                display.val((display.val() + num)
                    .replace(/^0*\./, '0.'))
                console.log(num)
            }
        }
        else if (event.keyCode === 100) {
            num = 4;
            if (newInputToggle) {
                display.val('');
                newInputToggle = false;
                calcActive = true;
                storedOp = pressedOp;
            }

            if (display.val().length < 10 && (num !== '.' || (display.val().match(/\./g) || []).length < 1)) {
                display.val((display.val() + num)
                    .replace(/^0*\./, '0.'))
                console.log(num)
            }
        }
        else if (event.keyCode === 101) {
            num = 5;
            if (newInputToggle) {
                display.val('');
                newInputToggle = false;
                calcActive = true;
                storedOp = pressedOp;
            }

            if (display.val().length < 10 && (num !== '.' || (display.val().match(/\./g) || []).length < 1)) {
                display.val((display.val() + num)
                    .replace(/^0*\./, '0.'))
                console.log(num)
            }
        }
        else if (event.keyCode === 102) {
            num = 6;
            if (newInputToggle) {
                display.val('');
                newInputToggle = false;
                calcActive = true;
                storedOp = pressedOp;
            }

            if (display.val().length < 10 && (num !== '.' || (display.val().match(/\./g) || []).length < 1)) {
                display.val((display.val() + num)
                    .replace(/^0*\./, '0.'))
                console.log(num)
            }
        }
        else if (event.keyCode === 103) {
            num = 7;
            if (newInputToggle) {
                display.val('');
                newInputToggle = false;
                calcActive = true;
                storedOp = pressedOp;
            }

            if (display.val().length < 10 && (num !== '.' || (display.val().match(/\./g) || []).length < 1)) {
                display.val((display.val() + num)
                    .replace(/^0*\./, '0.'))
                console.log(num)
            }
        }
        else if (event.keyCode === 104) {
            num = 8;
            if (newInputToggle) {
                display.val('');
                newInputToggle = false;
                calcActive = true;
                storedOp = pressedOp;
            }

            if (display.val().length < 10 && (num !== '.' || (display.val().match(/\./g) || []).length < 1)) {
                display.val((display.val() + num)
                    .replace(/^0*\./, '0.'))
                console.log(num)
            }
        }
        else if (event.keyCode === 105) {
            num = 9;
            if (newInputToggle) {
                display.val('');
                newInputToggle = false;
                calcActive = true;
                storedOp = pressedOp;
            }

            if (display.val().length < 10 && (num !== '.' || (display.val().match(/\./g) || []).length < 1)) {
                display.val((display.val() + num)
                    .replace(/^0*\./, '0.'))
                console.log(num)
            }
        }
        else if (event.keyCode === 110) {
            num = '.';
            if (newInputToggle) {
                display.val('');
                newInputToggle = false;
                calcActive = true;
                storedOp = pressedOp;
            }

            if (display.val().length < 10 && (num !== '.' || (display.val().match(/\./g) || []).length < 1)) {
                display.val((display.val() + num)
                    .replace(/^0*\./, '0.'))
                console.log(num)
            }
        }
        else if (event.keyCode === 106) {
            num = "×";
            pressedOp = num
            newInputToggle = true;
            if (!prevVal) {
                prevVal = parseFloat(display.val(), 10);
                calcActive = false;
            }

            else if (calcActive) {
                curVal = parseFloat(display.val(), 10);
                ans = doTheMath[storedOp](prevVal, curVal)
                display.val(truncateAns(ans));
                calcActive = false;


                if (pressedOp === '=') {
                    prevVal = null;
                } else {
                    prevVal = parseFloat(display.val(), 10);
                }
            }
        }
        else if (event.keyCode === 107) {
            num = "+";
            pressedOp = num
            newInputToggle = true;
            if (!prevVal) {
                prevVal = parseFloat(display.val(), 10);
                calcActive = false;
            }

            else if (calcActive) {
                curVal = parseFloat(display.val(), 10);
                ans = doTheMath[storedOp](prevVal, curVal)
                display.val(truncateAns(ans));
                calcActive = false;


                if (pressedOp === '=') {
                    prevVal = null;
                } else {
                    prevVal = parseFloat(display.val(), 10);
                }
            }
        }
        else if (event.keyCode === 109) {
            num = "−";
            pressedOp = num
            newInputToggle = true;
            if (!prevVal) {
                prevVal = parseFloat(display.val(), 10);
                calcActive = false;
            }

            else if (calcActive) {
                curVal = parseFloat(display.val(), 10);
                ans = doTheMath[storedOp](prevVal, curVal)
                display.val(truncateAns(ans));
                calcActive = false;


                if (pressedOp === '=') {
                    prevVal = null;
                } else {
                    prevVal = parseFloat(display.val(), 10);
                }
            }
        }
        else if (event.keyCode === 111) {
            num = "÷";
            pressedOp = num
            newInputToggle = true;
            if (!prevVal) {
                prevVal = parseFloat(display.val(), 10);
                calcActive = false;
            }

            else if (calcActive) {
                curVal = parseFloat(display.val(), 10);
                ans = doTheMath[storedOp](prevVal, curVal)
                display.val(truncateAns(ans));
                calcActive = false;


                if (pressedOp === '=') {
                    prevVal = null;
                } else {
                    prevVal = parseFloat(display.val(), 10);
                }
            }
        }
        else if (event.keyCode === 13) {
            num = "=";
            pressedOp = num
            newInputToggle = true;
            if (!prevVal) {
                prevVal = parseFloat(display.val(), 10);
                calcActive = false;
            }

            else if (calcActive) {
                curVal = parseFloat(display.val(), 10);
                ans = doTheMath[storedOp](prevVal, curVal)
                display.val(truncateAns(ans));
                calcActive = false;


                if (pressedOp === '=') {
                    prevVal = null;
                } else {
                    prevVal = parseFloat(display.val(), 10);
                }
            }
        }
        else if (event.keyCode === 8) {
            curVal = prevVal = storedOp = null;
            newInputToggle = true;
            display.val('0');
        }
        else if (event.keyCode === 46) {
            curVal = prevVal = storedOp = null;
            newInputToggle = true;
            display.val('0');
        }
    }
});

$(".numbers").click(function() {
    if (newInputToggle) {
        display.val('');
        newInputToggle = false;
        calcActive = true;
        storedOp = pressedOp;
    }

    if (display.val().length < 10 && ($(this).text() !== '.' || (display.val().match(/\./g) || []).length < 1)) {
        display.val((display.val() + $(this).text())
            .replace(/^0*\./, '0.'))
        console.log($(this).text())
    }
});

$('.op').click(function() {
    pressedOp = $(this).text()
    newInputToggle = true;
    if (!prevVal) {
        prevVal = parseFloat(display.val(), 10);
        calcActive = false;
    }

    else if (calcActive) {
        curVal = parseFloat(display.val(), 10);
        ans = doTheMath[storedOp](prevVal, curVal)
        display.val(truncateAns(ans));
        calcActive = false;


        if (pressedOp === '=') {
            prevVal = null;
        } else {
            prevVal = parseFloat(display.val(), 10);
        }
    }
});

doTheMath = {
    '\u002B': function(a, b) {
        return a + b;
    },
    '\u2212': function(a, b) {
        return a - b;
    },
    '\u00D7': function(a, b) {
        return a * b;
    },
    '\u00F7': function(a, b) {
        return a / b;
    },
    '=': function(a, b) {
        return b;
    }
};

$('#clear-all').click(function() {
    curVal = prevVal = storedOp = null;
    newInputToggle = true;
    display.val('0');
});

function truncateAns(num) {
    if (num === Infinity){
        return '8008135'
    } else if (num > Math.pow(10, displayLength - 1)) {
        return num.toExponential(displayLength - 5).toString().
        replace(/\.0+e/, 'e');
    } else if (num.toString().length >= displayLength) {
        return num.toFixed(displayLength - Math.round(num).toString().length - 1).
        toString().
        replace(/\.0+e/, 'e');
    } else {
        return num;
    }
}
function showTime(){
    const date = new Date();
    let h = date.getHours();
    let m = date.getMinutes();
    let s = date.getSeconds();
    let session = "صباحا";
    let today = new Date();
    let dd = String(today.getDate()).padStart(2, '0');
    let mm = String(today.getMonth() + 1).padStart(2, '0');
    let yyyy = today.getFullYear();

    today = yyyy + " - " + mm + " - " + dd;
    if(h === 0) {
        h = 12;
    }

    if(h > 12) {
        h = h - 12;
        session = "مساءً";
    }

    h = (h < 10) ? "0" + h : h;
    m = (m < 10) ? "0" + m : m;
    s = (s < 10) ? "0" + s : s;
    // let h1 = h.toIndiaDigits;
    // let m1 = m.toIndiaDigits;
    // let s1 = s.toIndiaDigits;
    let time = "الساعه الان" + " " + h + ":" + m + ":" + s + " " +  session;
    document.getElementById("MyClockDisplay").innerText = time;
    document.getElementById("MyClockDisplay").textContent = time;

    setTimeout(showTime, 1000);

    document.getElementById("MyDateDisplay").innerText = today;
    document.getElementById("MyDateDisplay").textContent = today;

    const arabicNumbers = ['۰', '١', '٢', '٣', '٤', '٥', '٦', '٧', '٨', '٩'];

    $('.translate').text(function(i, v) {
        let chars = v.split('');
        for (let i = 0; i < chars.length; i++) {
            if (/\d/.test(chars[i])) {
                chars[i] = arabicNumbers[chars[i]];
            }
        }
        return chars.join('');
    });
}

showTime();
