from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from ..models.allergen import AllergenRequestBody, AllergenResponseBody

async def identify_potential_allergens(request_body: AllergenRequestBody):
    try:
        # print(jsonable_encoder(request_body))
        # ai_service
        potential_allergens_data = [
            # {
            #     'nFASS': 3.5,
            #     'probability': 0.8,
            #     'allergen_type_id': 1
            # }
        ]

        updated_allergens_data = [
            {
                'id': 2,
                'nFASS': 1.0,
                'probability': 0.5
            }
        ]

        response = {
            'identified_allergens': potential_allergens_data,
            'updated_allergens': updated_allergens_data
        }

        return JSONResponse(content=jsonable_encoder(AllergenResponseBody(**response)), status_code=200)
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))