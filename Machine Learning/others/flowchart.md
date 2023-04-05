```flow
開始=>start: 開始  
終了=>end: 終了  

分岐(align-next=no)=>condition: おなかすいた？
処理1=>operation: おやつを手に取る
定義済み処理=>subroutine: おいしく食べる

分岐2=>condition: 満足した？
処理2=>operation: それは残念

開始->分岐
分岐(yes)->処理1
分岐(no)->処理2(top)->分岐

処理1->定義済み処理(right)->分岐2
分岐2(yes)->終了
分岐2(no, bottom)->処理1
```
