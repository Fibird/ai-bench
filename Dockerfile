FROM python:3.7.10

RUN pip3 install --upgrade tensorflow && \
    pip3 install ai-benchmark

WORKDIR = /app

ADD ai_bench.py /app

CMD ["python3", "/app/ai_bench.py"]
