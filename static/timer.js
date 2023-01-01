var sec = 0;   // 秒数カウント用変数
 
function start() {
    PassageID = setInterval('showPassage()',1000);
 }
 // 繰り返し処理の中止
 function stop() {
    clearInterval( PassageID );
 }
 // 繰り返し処理の中身
 function showPassage() {
    sec = sec + 1;
    var msg = "時間:" + sec + "秒";
    document.getElementById("timer").innerHTML = msg;
 }

window.onload = start;
