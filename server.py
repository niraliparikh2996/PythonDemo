import aiohttp
import asyncio
import uvicorn
import pathlib
import sys
from io import BytesIO
from starlette.applications import Starlette
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import HTMLResponse, JSONResponse
from starlette.staticfiles import StaticFiles
# from TextProcessor import ping,getPrediction,getPredictionImages,getPredictionForNLU
path = pathlib.Path(__file__).parent

app = Starlette()
app.add_middleware(CORSMiddleware, allow_origins=['*'], allow_headers=['X-Requested-With', 'Content-Type'])


# @app.route('/sentiment', methods=['POST','GET'])
# async def analyze(request):
#     text = await request.json()
#     return JSONResponse({"Prediction":getPrediction([text])} )


# @app.route('/images', methods=['POST','GET'])
# async def analyze_images(request):
#     text = await request.json()
#     return JSONResponse({"Prediction":getPredictionImages([text])} )

# @app.route('/nlu', methods=['POST','GET'])
# async def analyze_images(request):
#     text = await request.json()
#     return JSONResponse({"Prediction":getPredictionForNLU([text])} )
@app.route('/')
async def homepage(request):
    return JSONResponse({'hello': 'world'})

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
# if __name__ == '__main__':
#     uvicorn.run(app=app, host='0.0.0.0', port=5000, log_level="info")
    # if 'serve' in sys.argv:
    #     uvicorn.run(app=app, host='0.0.0.0', port=5000, log_level="info")
