function decideImg() {
    // var flag = false; // 選択されているか否かを判定するフラグ

    //決定ボタンのdisabledがtrueだったらfalseにして押せるようにする
    if(document.decide.decide_button.disabled){
        document.decide.decide_button.disabled = false
    }
   
    //　ラジオボタンの数だけ判定を繰り返す
    for(var i=0; i<document.imageBoxes.img.length;i++){
        // i番目のラジオボタンがチェックされているかを判定
        if(document.imageBoxes.img[i].checked){ 
            // flag = true;    
            document.decide.img_Name.value = document.imageBoxes.img[i].id
            console.log(document.imageBoxes.img[i].id + "が選択されました。")
            // alert(document.imageBoxes.img[i].id + "が選択されました。");
        }
    }
    // 何も選択されていない場合の処理
    // if(!flag){ 
    //     console.log("画像が選択されていません。")
    //     alert("画像が選択されていません。");
    // } 
}

function onAddButton(){
    //input[type="file"]のvalueの値に応じて画像追加ボタンの活性化・非活性化を変更
    if(document.add.add_image.value == ""){
        document.add.add_button.disabled = true
    }
    else{
        document.add.add_button.disabled = false
    }
}