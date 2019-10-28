To run the backend, run:

```
python -m venv venv
venv/Scripts/activate
pip install -r requirements.txt
docker run -p 6379:6379 -d redis:2.8
python manage.py runserver
```