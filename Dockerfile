FROM python:3.12.3
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1 
RUN git clone https://github.com/wazwki/wazwki.git
WORKDIR /wazwki/app
RUN pip install --no-cache-dir -r /wazwki/requirements.txt
RUN python manage.py collectstatic --noinput