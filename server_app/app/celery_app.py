import os
from celery import Celery

from app.controllers.allergen_controller import identify_potential_allergens

celery_app = Celery('tasks', broker=os.environ.get('CELERY_BROKER_URL'))

@celery_app.task
def identify_potential_allergens_task(profile_id, reaction_id):
    return identify_potential_allergens(profile_id, reaction_id)