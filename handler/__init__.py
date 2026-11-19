from aiogram import Router
from . import start, about_us, ariza


def setup_message_routers():
    router = Router()
    router.include_router(start.router)
    router.include_router(about_us.router)
    router.include_router(ariza.router)
    return router