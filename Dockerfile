FROM python:3-slim-bullseye as builder

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt
COPY . /app/

RUN /app/bin/generate.py

FROM nginxinc/nginx-unprivileged:1.23-alpine

USER root

# hadolint ignore=DL3018
RUN apk --no-cache add shadow   && \
    usermod -u 1000 nginx       && \
    groupmod -g 1000 nginx      && \
    apk del shadow

USER nginx

COPY nginx/default.conf /etc/nginx/conf.d/default.conf
COPY --from=builder /app/build/ /usr/share/nginx/html/