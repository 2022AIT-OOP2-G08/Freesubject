//ゲーム開始ボタンの活性化
function Oncpuz(){
    //縦横の分割数を選択していないとスタートできない
    var colv=document.getElementById('rowcol');
    var rows=document.getElementById('send-image');
    var cpuz = document.getElementById('create_puzzle')
    if(colv.value==""||rows.value==""){
        cpuz.disabled = true;
    }else{
        cpuz.disabled = false; 
    }
}


