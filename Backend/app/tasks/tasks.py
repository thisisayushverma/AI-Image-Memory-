from app.celery_app import celery_app


@celery_app.task
def process_image(image_id):
    print(f"processing image {image_id}")
    c = 0
    for i in range(1, 100000000):  # range(start, stop) - stop is exclusive, so use 1001
        c = i%7



    print(f"value after loop {c}")
    return {
        "image_id": image_id,
        "status": "completed"
    }