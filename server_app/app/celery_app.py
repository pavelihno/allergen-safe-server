import os, requests
from datetime import datetime, timedelta
from celery import Celery

from app.utils.jwt import signJWT
from app.utils.ai_service import get_ai_response

celery_app = Celery('tasks', broker=os.environ.get('CELERY_BROKER_URL'))

def __send_request(email, request_type, endpoint, json):
    valid_request_types = ['POST', 'PUT']
    if request_type in valid_request_types:
        request_method = getattr(requests, request_type.lower())
        headers = {'Authorization': f'Bearer {signJWT(email, datetime.now() + timedelta(minutes=1))}'}
        response = request_method(f'{os.environ.get('SERVER_URL')}/{endpoint}', json=json, headers=headers)
        response.raise_for_status()
        return response.json()
    raise ValueError(f"Invalid request type '{request_type}'. Must be one of {','.join(valid_request_types)}")

@celery_app.task
def identify_potential_allergens_task(email, profile_id, request_data):
    ai_response = get_ai_response(
        'allergens/identify',
        json=request_data
    )
    if ai_response:
        identified_allergens = ai_response.get('identified_allergens', [])
        updated_allergens = ai_response.get('updated_allergens', [])

        if identified_allergens:
            __send_request(email, 'POST', f'allergens/{profile_id}', {'allergens': identified_allergens})
        if updated_allergens:
            __send_request(email, 'PUT', f'allergens/{profile_id}', {'allergens': updated_allergens})
        return True
    else:
        return False