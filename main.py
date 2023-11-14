from starlette.middleware.cors import CORSMiddleware

from api import app
import uvicorn

if __name__ == "__main__":
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    uvicorn.run(app)

