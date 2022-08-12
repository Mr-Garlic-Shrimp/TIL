; 下記はUS配列、60%キーボード向けのAutoHotKeyである。

;「スペース＋文字キー」が押されたら矢印キーが押されたことにする
Space & h:: Send,{Blind}{Left}
Space & j:: Send,{Blind}{Down}
Space & k:: Send,{Blind}{Up}
Space & l:: Send,{Blind}{Right}
Space & y:: Send,{Blind}{Home}
Space & u:: Send,{Blind}{PgDn}
Space & i:: Send,{Blind}{PgUp}
Space & o:: Send,{Blind}{End}
Space:: Send,{Blind}{Space}

;「Space & F」で日本語変換の動作をさせる
Space & f:: Send,{Blind}{vkF3sc029} 

;「スペース＋セミコロン／コロン」が押されたらバックスペース・デリートが押されたことにする
Space & `;:: Send,{Blind}{BS}
Space & ':: Send,{Blind}{Delete}

;「無変換+スペース」でエンターキーの動作をさせる
;Space & Space::　Send,{Blind}{Enter} 

;「capslock」で日本語変換の動作をさせる
;F13::Send,{Blind}{vkF3sc029} 
;RAlt:: Send,{Blind}{vkF3sc029} 

