function decideImg() {
    var flag = false; // 選択されているか否かを判定するフラグ
   
    //　ラジオボタンの数だけ判定を繰り返す
    for(var i=0; i<document.imageBoxes.img.length;i++){
  
        // i番目のラジオボタンがチェックされているかを判定
        if(document.imageBoxes.img[i].checked){ 
            flag = true;    
            alert(document.imageBoxes.img[i].id + "が選択されました。");
        }
    }
    // 何も選択されていない場合の処理
    if(!flag){ 
        alert("画像が選択されていません。");
    } 
}