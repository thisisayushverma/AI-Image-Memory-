from celery import Celery
from kombu import Queue

celery_app = Celery(
    "image_processing",
    broker="amqp://guest:guest@localhost:5672//",
    backend="rpc://",
    include=[
        "app.tasks.tasks",
    ],
)

celery_app.conf.worker_mingle = False

celery_app.conf.worker_send_task_events = False

celery_app.conf.event_queue_exclusive = True
celery_app.conf.event_queue_durable = False

celery_app.conf.task_queues = (
    Queue("image"),
)

# celery_app.conf.update(
#     # Serialization
#     task_serializer='json',
#     accept_content=['json'],
#     result_serializer='json',
    
#     # Timezone
#     timezone='UTC',
#     enable_utc=True,
    
#     # Task execution settings
#     task_acks_late=True,  # Acknowledge after task completes
#     task_reject_on_worker_lost=True,
#     worker_prefetch_multiplier=1,  # Fair distribution
    
#     # Result settings
#     result_expires=3600,  # Results expire after 1 hour
    
#     # Task time limits
#     task_time_limit=300,  # Hard limit: 5 minutes
#     task_soft_time_limit=240,  # Soft limit: 4 minutes
# )

celery_app.conf.task_routes = {
    "app.tasks.tasks.*": {
        "queue": "image",
    },
}







celery_app.conf.imports = {"app.tasks.tasks",}
