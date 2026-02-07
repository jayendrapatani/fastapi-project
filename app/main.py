from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from app.api import routes_auth,routes_predict
from app.middelware.logging_middelware import LoggingMiddelware
from app.core.exceptions import register_exception_handlers

app=FastAPI(title='Car Price  Prediction API')

# link middleware
app.add_middleware(LoggingMiddelware)

# link endpoints
app.include_router(routes_auth.router,tags=['Auth'])
app.include_router(routes_predict.router,tags=["prediction"])


# monitoring using prometheus

Instrumentator().instrument(app).expose(app)

# add excepition handler

register_exception_handlers(app)

