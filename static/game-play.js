var target = "";

var dragid = document.getElementsByClassName('dragtarget');
var dropbox = document.getElementsByClassName('dragpoint');
var dropblock = document.getElementsByClassName('block');

let startTime = 0, timer; // 開始時間、タイマー
let gamestatus = "ready"; // ステータス（ready/start）

document.getElementById("time").innerText = "--.--";
// カウントダウン開始
startTime = Date.now();
timer = setInterval(countdown, 20);

function countdown(){
    // カウントダウン
    let time = 3 - Math.floor((Date.now() - startTime) / 1000);
    if (time == 0) {
        // スタート
        gamestatus = "start";
        startTime = Date.now();
        clearInterval(timer);
        timer = setInterval(update, 20);
    }
    // カウントダウンの描画
    update();
    drawText(time, "red");
}

function update(){
    // タイムの表示
    let time = ((Date.now() - startTime) / 1000).toFixed(2);
    if ((gamestatus == "start") && (time < 1)) setUp();
    time = ("0" + time).slice(-5);
    if (gamestatus == "ready") time = "--.--";
    drawText(time);
}

function drawText(text, color="black"){
    // テキストの描画
    document.getElementById("time").innerText = text;
    document.getElementById("time").style.color = color;
}


function setUp(){
    for(var i = 0; i < dragid.length; i++) {
        dragid[i].addEventListener('dragstart', function(element){
            target = element.target;
        }, false);
    }
    
    for(var i = 0; i < dropbox.length; i++){
        dropbox[i].addEventListener('dragover', function(element){
            element.preventDefault();
        }, false);
    
        dropbox[i].addEventListener('dragenter', function(element){
            if (element.target.className == "drogpoint") {
                element.target.style.background = '#a9a9a9';
            }
        });
    
        dropbox[i].addEventListener('drop', function(element){
            element.preventDefault();
            count = 0
            if(element.target.className == "dragpoint"){
                target.parentNode.removeChild(target);
                element.target.appendChild(target);
            }
            for(i = 0; i<dropbox.length; i++){
                data = dropbox[i].innerHTML
    
                if(data === dragid[i].outerHTML){
                    console.log(data+"\n"+dragid[i].outerHTML);
                    console.log("true");
                    count++;
                    console.log(count);
                }
            }
            // 終了判定
            // if(count === dropbox.length){
            //     // 画面遷移
            // clearInterval(update)
            //     window.location.href = 'http://127.0.0.1:5000';
            // }
        }, false);
    }
    
    for (var i = 0; i < dropblock.length; i++){
        dropblock[i].addEventListener('dragover', function(element){
            element.preventDefault();
        }, false);
        dropblock[i].addEventListener('dragenter', function(element){
            if (element.target.className == "drogpoint") {
                element.target.style.background = '#a9a9a9';
            }
        });
        dropblock[i].addEventListener('drop', function(element){
            element.preventDefault();
            if(element.target.className == "block" && element.target.innerHTML.trim()==""){
                target.parentNode.removeChild(target);
                element.target.appendChild(target);
            }
        }, false);
    }
}