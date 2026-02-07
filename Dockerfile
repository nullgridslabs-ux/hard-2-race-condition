FROM python:3.11-slim
WORKDIR /app
COPY app.py .
RUN pip install flask
ENV FLAG=CTF{hard_race_condition}
EXPOSE 5000
CMD ["python","app.py"]
