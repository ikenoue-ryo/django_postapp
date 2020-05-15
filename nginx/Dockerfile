FROM nginx

#デフォルトのconfを決して別の設定を追加
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d
