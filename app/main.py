from fastapi import FastAPI
from config import engine
import router
import model

model.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
async def Home():
    return "Welcome Home!"

app.include_router(router.router,prefix="/book", tags=["book"])

