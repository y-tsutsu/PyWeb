# coding: utf-8

import cgi
import os
import time
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding = "utf-8")

class Request:
    """
    HTTPのリクエストをハンドリングするクラス
    CGI側でインスタンスを生成することによって利用する
    クエリデータや環境変数へのアクセス，主要ヘッダへの
    アクセス用メソッドを提供
    """

    def __init__(self, environ = os.environ):
        """
        インスタンスの初期化メソッド
        クエリ，環境変数をアトリビュートとして保持する
        """
        self.form = cgi.FieldStorage()
        self.environ = environ

_weekdayname = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
_monthname = [None, "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

class Response:
    """
    HTTPのレスポンスをハンドリングするクラス
    レスポンスを送る前にインスタンスを生成して利用する
    レスポンスやヘッダの内容の保持，ヘッダを含めたレスポンスの
    送信を行う
    """

    def __init__(self, charset = "utf-8"):
        """
        インスタンスの初期化メソッド
        ヘッダ用の辞書，本文用の文字列などを初期化する
        """
        self.headers = {"Content-type":"text/html; charset = {0}".format(charset)}
        self.body = ""
        self.status = 200
        self.status_message = ""

    def set_header(self, name, value):
        """
        レスポンスのヘッダを設定する
        """
        self.headers[name] = value

    def get_header(self, name):
        """
        設定済みのレスポンス用ヘッダを返す
        """
        return self.headers.get(name, None)

    def set_body(self, bodystr):
        """
        レスポンスとして出力する本文の文字列を返す
        """
        self.body = bodystr

    def make_output(self, timestamp = None):
        """
        ヘッダと本文を含めたレスポンス文字列を作る
        """
        if timestamp is None:
            timestamp = time.time()
        year, month, day, hh, mm, ss, wd, y, z = time.gmtime(timestamp)
        dtstr = "{0}, {1:02d} {2:<3} {3:4d}, {4:02d}:{5:02d}:{6:02d} GMT".format(_weekdayname[wd], day, _monthname[month], year, hh, mm, ss)
        self.set_header("Last-Modified", dtstr)
        headers = "\n".join(["{0}: {1}".format(k, v) for k, v in self.headers.items()])
        return headers + "\n\n" + self.body

    def __str__(self):
        """
        リクエストを文字列に変換する
        """
        return self.make_output()

def get_htmltemplate(title):
    """
    レスポンスとして返すHTMLのうち，定型部分を返す
    """
    html_body = """
    <html>
    <head>
        <title>{0}</title>
        <meta http-equiv="content-type" content="text/html; charset = utf-8" />
    </head>
    <body>
        {1}
    </body>
    </html>
    """.format(title, "{0}")
    return html_body
