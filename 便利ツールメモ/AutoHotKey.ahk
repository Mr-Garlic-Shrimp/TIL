
;「スペース＋文字キー」が押されたらHome,PgDn,PgUp,Endが押されたことにする
Space & h:: Send,{Blind}{Left}
Space & j:: Send,{Blind}{Down}
Space & k:: Send,{Blind}{Up}
Space & l:: Send,{Blind}{Right}
Space & y:: Send,{Blind}{Home}
Space & u:: Send,{Blind}{PgDn}
Space & i:: Send,{Blind}{PgUp}
Space & o:: Send,{Blind}{End}
Space:: Send,{Blind}{Space}

;「スペース＋セミコロン／コロン」が押されたらバックスペース・デリートが押されたことにする
Space & `;:: Send,{Blind}{BS}
Space & ':: Send,{Blind}{Delete}

;「Space & F」で日本語変換の動作をさせる
Space & f:: Send,{Blind}{vkF3sc029} 


;
F12 & o::MouseClick, Left,,,,,D
F12 & o UP::MouseClick, Left,,,,,U
F12 & [::MouseClick, Right
F12 & .::MouseClick, WheelUp
F12 & /::MouseClick, WheelDown

;「スペース＋左側のキー」が押されたらマウスカーソルを移動させる
;F12 & p::MouseMove 0, -20, 0, R
;F12 & `;::MouseMove 0, 20, 0, R
;F12 & l::MouseMove -20, 0, 0, R
;F12 & '::MouseMove 20, 0, 0, R

F12 & p::
If GetKeyState("Ctrl", "P") {
                MouseMove 0, -200, 0, R
              }else{
                MouseMove 0, -20, 0, R
              }
Return

F12 & `;::
If GetKeyState("Ctrl", "P") {
                MouseMove 0, 200, 0, R
              }else{
                MouseMove 0, 20, 0, R
              }
Return

F12 & l::
If GetKeyState("Ctrl", "P") {
                MouseMove -200, 0, 0, R
              }else{
                MouseMove -20, 0, 0, R
              }
Return

F12 & '::
If GetKeyState("Ctrl", "P") {
                MouseMove 200, 0, 0, R
              }else{
                MouseMove 20, 0, 0, R
              }
Return





;↓多分もうつかわないやつ

/*
Space & z::MouseMove 0, -100, 0, R
Space & x::MouseMove 0, 100, 0, R
Space & q::MouseMove -100, 0, 0, R
Space & d::MouseMove 20, 0, 0, R

Space & k::
If GetKeyState("Ctrl", "P") {
                MouseMove 0, -10, 0, R
              }else{
                Send {Blind}{Up}
              }
Return

Space & ,::
If GetKeyState("Ctrl", "P") {
                MouseMove 0, -100, 0, R
              }
Return


Space & j::
If GetKeyState("Ctrl", "P") {
                MouseMove 0, 10, 0, R
              }else{
                Send {Blind}{Down}
              }
Return

Space & m::
If GetKeyState("Ctrl", "P") {
                MouseMove 0, 100, 0, R
              }
Return

Space & h::
If GetKeyState("Ctrl", "P") {
                MouseMove -10, 0, 0, R
              }else{
                Send {Blind}{Left}
              }
Return

Space & n::
If GetKeyState("Ctrl", "P") {
                MouseMove -100, 0, 0, R
              }
Return

Space & l::
If GetKeyState("Ctrl", "P") {
                MouseMove 10, 0, 0, R
              }else{
                Send {Blind}{Right}
              }
Return

Space & .::
If GetKeyState("Ctrl", "P") {
                MouseMove 100, 0, 0, R
              }
Return

*/

