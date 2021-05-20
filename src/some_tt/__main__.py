from typing import List

import uvicorn
from fastapi import FastAPI

from some_tt import db
from some_tt.models import CallModel, Meta, Filter, Sort


app = FastAPI(
    title='Call processing software',
    description='Сервис управления вызовами.',
    version="0.1.0",
    openapi_tags=[
        {"name": "Calls", "description": "Методы для управления вызовами."},
    ]
)


@app.on_event("startup")
async def init_app():
    await db.init()


@app.get('/calls', response_model=Meta[List[CallModel]], tags=['Calls'])
async def get_calls(
        page: int = 0,
        page_size: int = 15,
        sort: Sort = 'asc',  # сортировку предполагаем по call_id
        filter_phone: str = None,  # конкретный набор фильтров зависит от требований
        filter_topic: str = None
) -> Meta[List[CallModel]]:
    """ Возвращает список вызовов из базы данных. """
    filter_ = Filter(
        phone=filter_phone,
        topic=filter_topic
    )

    data = await db.get_calls(page, page_size, sort, filter_)
    total = await db.get_total()

    return Meta(
        data=data,
        page=page,
        page_size=page_size,
        sort=sort,
        total=total,
        filter=filter_
    )


uvicorn.run(app, host='0.0.0.0', port=8080)
