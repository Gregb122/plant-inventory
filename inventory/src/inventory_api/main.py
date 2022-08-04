from fastapi import FastAPI, Request, status, Depends
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer

from routers import user_route, plant_route, event_route

from helpers.exceptions import AdminUserameException
from models import user_model, plant_model, event_model

from helpers.database import engine

app = FastAPI()
app.include_router(user_route.router)
app.include_router(plant_route.router)
app.include_router(event_route.router)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.get('/')
def index(token: str = Depends(oauth2_scheme)):
    return {'token': token}

@app.exception_handler(AdminUserameException)
def admin_userame_exception_handler(requst: Request, exc: AdminUserameException):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={'detail': exc.name}
    )

user_model.Base.metadata.create_all(engine)
plant_model.Base.metadata.create_all(engine)
event_model.Base.metadata.create_all(engine)
