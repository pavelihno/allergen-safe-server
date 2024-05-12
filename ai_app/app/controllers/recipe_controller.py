import json

from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from app.models.recipe import RecipeRequestBody, RecipeResponseBody
from app.ai_service import get_ai_response

async def generate_recipe(request_body: RecipeRequestBody):
    try:
        recipe_data = get_ai_response('generate_recipe', {
            'cuisine': request_body.cuisine,
            'description': request_body.description,
            'allergens': jsonable_encoder(request_body.allergens),
            'response_format': json.dumps(RecipeResponseBody.get_annotations())
        })
        return JSONResponse(content=jsonable_encoder(RecipeResponseBody(**recipe_data)), status_code=200)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))