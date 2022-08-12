# sslの問題でpip installできない

* 事象：    
powershellからpip installしようとすると下記のエラーが起こる。
    ```
    Could not fetch URL https://pypi.org/simple/python-pptx/: There was a problem confirming the ssl certificate: HTTPSConnectionPool(host=’pypi.org’, port=443): Max retries exceeded with url: /simple/python-pptx/ (Caused by SSLError(“Can’t connect to HTTPS URL because the SSL module is not available.”)) – skipping
    ```

* 原因：　調査中
* 解決策：　WindowsにOpenSSlをインストールすることで解決した。

* 参考
  * https://wanna-try.net/pip_error/149/
  * [OpenSSLインストール方法](https://atmarkit.itmedia.co.jp/ait/articles/1601/29/news043.html) 
