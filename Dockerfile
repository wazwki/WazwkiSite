FROM python:3.12.3
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1 
RUN git clone https://github.com/wazwki/WazwkiSite.git
WORKDIR /WazwkiSite/app
RUN pip install --no-cache-dir -r /WazwkiSite/requirements.txt
RUN python manage.py collectstatic --noinput