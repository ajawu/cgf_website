celery -A celery_worker.celery_app worker --loglevel=info
celery flower -A celery_worker.celery_app --broker:redis://localhost:6379/0