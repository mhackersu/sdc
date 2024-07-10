FROM python:3.8
COPY app.py requirements.txt test.json /
RUN pip install -r requirements.txt
CMD ["python", "app.py"]