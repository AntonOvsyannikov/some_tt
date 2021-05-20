import pymotyc
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import IndexModel

from some_tt.models import CallModel, Sort, Filter

engine = pymotyc.Engine()


@engine.database
class Calls:
    calls: pymotyc.Collection[CallModel] = pymotyc.Collection(
        indexes=[
            IndexModel('call_id', unique=True),
            IndexModel('call_guid', unique=True),
            'phone', 'topic'
        ],
    )


async def init():
    motor = AsyncIOMotorClient("mongodb://mongo:27017")
    await engine.bind(motor=motor, inject_motyc_fields=True)


async def get_calls(page: int, page_size: int, sort: Sort, filter_: Filter):
    query = {}

    if filter_.phone is not None:
        query['phone'] = filter_.phone

    if filter_.topic is not None:
        query['topic'] = {'$regex': filter_.topic}

    return await Calls.calls.find(
        query,
        skip=page * page_size,
        limit=page_size,
        sort={'call_id': 1 if sort == 'asc' else -1}
    )


async def get_total():
    return await Calls.calls.collection.count_documents({})
