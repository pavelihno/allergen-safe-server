import json

from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from app.models.allergen import AllergenRequestBody, AllergenResponseBody
from app.ai_service import get_ai_response

async def identify_potential_allergens(request_body: AllergenRequestBody):
    try:
        allergens_data = get_ai_response('identify_potential_allergens', {
            'potential_allergens': jsonable_encoder(request_body.potential_allergens),
            'reactions': jsonable_encoder(request_body.reactions),
            'identified_allergens': jsonable_encoder(request_body.identified_allergens),
            'response_format': json.dumps(AllergenResponseBody.get_annotations())
        })
        return JSONResponse(content=jsonable_encoder(AllergenResponseBody(**allergens_data)), status_code=200)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))