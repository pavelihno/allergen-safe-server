from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from app.models.recipe import RecipeRequestBody, RecipeResponseBody

async def generate_recipe(request_body: RecipeRequestBody):
    try:
        # print(jsonable_encoder(request_body))
        # ai_service
        recipe_data = {
            'name': 'Spaghetti Bolognese',
            'ingredients': 'Spaghetti, ground beef, tomato sauce, onion, garlic, olive oil, salt, pepper',
            'description': 'A classic Italian dish made with spaghetti, ground beef, and tomato sauce.'
        }

        return JSONResponse(content=jsonable_encoder(RecipeResponseBody(**recipe_data)), status_code=200)

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))