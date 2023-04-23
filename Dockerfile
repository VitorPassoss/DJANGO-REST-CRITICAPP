FROM python:3.10

ARG USERNAME=ecodots
ARG WAIT_VERSION=2.9.0

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
  && rm -rf /var/lib/apt/lists/*

ADD https://github.com/ufoscout/docker-compose-wait/releases/download/${WAIT_VERSION}/wait /wait
RUN chmod +x /wait

RUN curl -fsSL https://deb.nodesource.com/setup_18.x | bash - && apt-get install -y nodejs

RUN adduser --disabled-password --gecos "" ${USERNAME}

WORKDIR /app

COPY --chown=${USERNAME}:${USERNAME} requirements.txt .
COPY --chown=${USERNAME}:${USERNAME} . .


USER ${USERNAME}

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

ENV PATH="/home/ecodots/.local/bin:${PATH}"

CMD ["daphne", "-b", "0.0.0.0", "-p", "8000", "project.asgi:application"]