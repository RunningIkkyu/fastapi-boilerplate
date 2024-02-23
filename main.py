import sentry_sdk
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sentry_sdk.integrations.fastapi import FastApiIntegration
from sentry_sdk.integrations.starlette import StarletteIntegration

from custom_logger import init_logger
from database import init_db
from middlewares.request import RequestMiddleware
from settings import settings

init_db()
init_logger()

sentry_sdk.init(
    dsn=settings.sentry_dsn_api,
    environment=settings.sentry_env,
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    enable_tracing=True,
    traces_sample_rate=1.0,
    integrations=[
        StarletteIntegration(transaction_style="url"),
        FastApiIntegration(transaction_style="url"),
    ],
)

docs_url = "/docs"
app = FastAPI(
    title="Sengine Workflow",
    description="Welcome to Sengine's API documentation! Here you will able to discover all of the ways you can interact with the Sengine API.",
    docs_url=docs_url,
)
app.add_middleware(RequestMiddleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
