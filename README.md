# ExtractComments

HTML の中のコメントを抽出するシンプルなツールです。

[Beatifulsoup4](https://www.crummy.com/software/BeautifulSoup/) を使用して HTML をパースし、コメントを抽出します。

## インストール

```bash 
> python -m venv .venv
> .venv\Scripts\activate  # Windows の場合
> python -m pip install -r requirements.txt
```

## 使い方

```bash
> python extract_comments.py input.html
or
> python extract_comments.py https://example.com/input.html 
```