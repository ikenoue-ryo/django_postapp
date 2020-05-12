# 公式からpython3.7 イメージをpull
FROM python:3.7

RUN mkdir /usr/src/app

# 作業ディレクトリを設定
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app

RUN pip install -r requirements.txt

# 環境変数を設定
# Pythonがpyc filesとdiscへ書き込むことを防ぐ
ENV PYTHONDONTWRITEBYTECODE 1
# Pythonが標準入出力をバッファリングすることを防ぐ
ENV PYTHONUNBUFFERED 1

# entrypoint.shをコピー
COPY entrypoint.sh /usr/src/app/entrypoint.sh

# ホストのカレントディレクトリを作業ディレクトリにコピー
COPY . /usr/src/app/

# entrypoint.shを実行
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
