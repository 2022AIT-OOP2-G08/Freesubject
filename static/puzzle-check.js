//console.log('JavaScript index.js fire!')  // JavaScriptが読み込まれて実行されたことをこれで確認できます。

//ここでjson等でパズルの縦横分割数を取得する。
rows=3;
cols=3;
chunks = rows*cols;


// 要素の位置座標を取得

//全ピースの座標を取得する
//パズルピースはパズルピースの中に"chunk_(番号)"というIDを持っているとして取得できるようになっています.
function get_coordinate(){
    var r=new Array;
    for (var i=0; i<chunks; i++){
        var elem = document.getElementById('chunk_'+i);
        r.push(elem.getBoundingClientRect());

        //console.log(r[i].left, r[i].top, r[i].width, r[i].height);
    }
    return r;

}
//初期状態の座標
/** 
window.onload = function(){
    var r=new Array;
    for (var i=0; i<chunks; i++){
        var elem = document.getElementById('chunk_'+i);
        r.push(elem.getBoundingClientRect());

        console.log(r[i].left, r[i].top, r[i].width, r[i].height);
    }
	console.log("")

} 
*/

//puzzle check
//　綺麗に並んでいるとみなせる状態になった時にchunkと同じ数を出力できるようにして
//  同じとき正解とする動作を追加する

function check(){
    //console.log("start check");
    var r=new Array;
    r=get_coordinate();
    checkcount=0;
    chunk=0;
    range=6;
    for (var row=1; row<=rows; row++){
        for (var col=1; col<=cols; col++){
            if (chunk<cols){
                if(chunk==0){
                    checkcount++;
                }else {
                    if((r[chunk].left>=r[chunk-1].right-r[chunk].width/range) && (r[chunk].left<=r[chunk-1].right+r[chunk].width/range) && (r[chunk].bottom<=r[cols*row].top+r[cols*row].height/range) && (r[chunk].bottom>=r[cols*row].top-r[cols*row].height/range)){
                        checkcount++;
                    }
                }
            }else{
                if(col==1){
                    if((r[chunk].top>=r[chunk-cols].bottom-r[chunk].height/range) && (r[chunk].top<=r[chunk-cols].bottom+r[chunk].height/range)){
                        checkcount++;
                    }
                }else{
                    if((r[chunk].left>=r[chunk-1].right-r[chunk].width/range) && (r[chunk].left<=r[chunk-1].right+r[chunk].width/range) && (r[chunk].top>=r[chunk-cols].bottom-r[chunk].height/range) && (r[chunk].top<=r[chunk-cols].bottom+r[chunk].height/range)){
                        checkcount++;
                    }
                }
            }
            chunk++;
        }
    }
    //console.log("checkcount",checkcount);
    //console.log("end check");
    return checkcount;
}


function correct_action(){
    //全ピースの座標及びその画像サイズを取得
    r=get_coordinate();
    for(var i=0; i<chunks; i++){
        console.log(r[i].left, r[i].top, r[i].width, r[i].height);
    }
    //ピースの正答率
    console.log('正しいピース数',check()+"/"+chunks);
    //正解時のアクション
    if (chunks==check()){
        console.log("正解")
        //次のページへ遷移する
        window.location.href ='/page6'
    }
}







