# pythonの基本
* pythonは上からプログラムを実行していく
* 複数行コメントアウトはダブルクォート３つで囲う
"""
"""
* また、Pythonでは関数へのコメントは関数定義内で書くのが習わし。こうすることで、_doc_メソッドでコメント部分を呼び出すことができる。


# 演算子
* 商と余りは行列の行番号と列番号を使うのにつかえる。    
(0.0) (0.1) (0.2)   
(1.0) (1.1) (1.2)   
(2.0) (2.1) (2.2)   
例えば、左上から順に数えて4番目(左上は０番目とする)の行・列は4/3=1..余り1で(1,1)のように決められる


# リスト

i = [1, 2, 3, 4, 5]  
j = i  # iのアドレスを渡している。jはiのアドレスをさす  
j[0] = 100  # iのアドレスに書き込むことになる  
print("j=", j)  
print("i=", i)  

#対処法  
x = [1, 2, 3, 4, 5]  
y = x.copy()  
y[0] = 100  
print("y=", y)  
print("x=", x)  

* リストや辞書型は関数のデフォルト引数に与えないこと
  * 関数を定義した段階でメモリ領域が確保され、参照渡しとなる。バグの原因となるので推奨されない。　
  * 対処法としてはリストはNoneで初期化しデフォルト、のままの時は空のリストを代入する。

* リスト内包表記
  * forで回してリストを生成するような場合下記のように１行で書ける。生成速度も早いのでおすすめ。
    * r = [i for i in list if i % 2 ==0]
  * 可読性の観点から、多くてもfor は２個まで

# タプル
* タプルの利点として、要素が固定の配列を定義したいときに、リストを使うよりも開発してる際にバグに気づきやすくすること
* a, b = b, a　みたいな書き方も実はタプル

# 辞書型
* 定義するときは dict(key1=value1, key2=value2)とするのが楽
* 空の辞書型aに対して、a['key'] = valueのようにキーと値を同時に定義・代入できる
* リストで疑似的に辞書型ぽくできるが、キー検索のスピードは辞書型の方が早い。これはハッシュテーブルという目次のような仕組みでメモリを検索するため。
* dict.items()は辞書型の要素をタプルのリストとして返す。そのため、for文で２つのキーとバリューに値を入れることができる。 
  * [('entree', 'beef'), ('drink', 'ice cream'), ('dessert', 'ice')]のような感じ
* 辞書型内包表記
  * d = {x: y for x, y in zip(w, f)} -> w,fはリストとする

# Noneとis
* Noneは何もないオブジェクトを指す
* isはオブジェクト同士が等しいか否かを判定する
  * 例）　a=1  
         b=Noneのとき、　a is b はFalseとなる。

# if
* if文は１行で書ける
  * 例）print('a is 2') if a==2 else print('a is NOT 2')
  * ただし、この場合elseが必須
  * また、この書き方はラムダ関数の時ぐらいしか使わない


# While文
* continueはその後の処理をスキップして次のループへ行く
* else文はWhile文を抜けるときに実行される。breakの時は実行されない


# for文
* 例えば単に、For文をrange関数などで10回したいときは、インクリメントにiなどを指定せずにアンダースコアを書くと、
代入されずにただ１０回ループする
* range関数は終了値－1の値で終わる。

# 関数
* 関数はFunctionという型（オブジェクト）なので、適当な変数に代入して使うことができる
  * 例） f = function()
        f()
  * 複数の引数をまとめて受け取りたい場合は*argsを引数として使える（タプル化）される
  def say_something(*args):
    for arg in args:
        print(arg)

  say_something(1,2,3)
  t = ("Mike","Nancy")
  say_something("Hi!", *t) #　タプルでまとめて引数を渡すときもアスタリスクを使う

  * キーワード引数は*kwargsを使うことで、辞書型で受け取れる。
  キーワード引数を辞書型で受け取る
      def menu(**kwargs):
          # print kargs
          for k, v in kwargs.items():
              print(k, v)

      d = {
          "entree": "beef",
          "drink": "ice cream",
          "dessert": "ice"
      }
      menu(**d)
  * 上記の引数の受け取り方、渡し方は全て混ぜて使うことができる

# クロージャ
* クロージャは関数内関数があるときに、例えば親の関数まで引数を固定して内部の関数の引数は後で入れたいときに使える
def circle_area_func(pi):
    def circle_area(radius):
        return pi * radius ** 2

    return circle_area

ca1 = circle_area_func(3.14)
ca2 = circle_area_func(3.141592)

print(ca1(10))　-> 314
print(ca2(10))  -> 314.1592

# デコレーター
* ある引数の前後に定型的な処理を追加したいときは、＠マークで関数を指定することで実行できる（これをデコレーターと呼ぶ）
* 一度定義してしまえば使いまわせるので楽
def print_more(func):
    def wrapper(*args, **kwargs):
        print("func:", func.__name__)
        print("args", args)
        print("kwargs", kwargs)
        result = func(*args, **kwargs)
        print("result:", result)
        return result
    return wrapper

def print_info(func):
    def wrapper(*args, **kwargs):
        print("start")
        result = func(*args, **kwargs)　
        print("end")
        return result
    return wrapper

!# decorater
@print_info  →まずこれがよびだされる。この中でadd_numが呼び出されると次の@へ行く
@print_more
def add_num(a,b):
    return a + b

r = add_num(10,20)
print(r)

r = add_num(10,20)
print(r)

# lambda
* defやreturnなどを省いてちょっとした関数を一行で書けるようにするもの
* ファンクションを引数にとるときに使える。いちいち宣言しなくてよいので楽
例）　lambda word: word.capitalize()
→wordを引数として、先頭を大文字にした結果を返す

# ジェネレータ
* イテレーターの一種。yieldで値を生成する。生成したら処理を抜ける。生成した値はnext()で参照する。 


# 例外処理
* exceptに”Exeception”を指定すれば、ほぼすべての例外をキャッチできるが、Python的には非推奨
* finallyは何があっても実行される。　　


