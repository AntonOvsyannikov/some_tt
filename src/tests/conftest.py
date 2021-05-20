import httpx
import pytest

from some_tt.models import CallModel


@pytest.fixture
def cli():
    with httpx.Client(base_url='http://127.0.0.1:8080', timeout=1) as client:
        yield client


GUID1 = '82763e15-16e0-4915-af4b-695b18b01fce'
GUID2 = 'fea78309-584e-4eca-9889-6bad0b08e0ee'
GUID3 = '2e99b0c6-738c-4bb1-ad4f-fe7f9b4c7549'
GUID4 = '8482bc8a-45b3-418d-a84e-b33c3505068c'
GUID5 = '0dae07f0-254c-44f4-a9c7-1180d96764e0'

# noinspection PydanticTypeChecker,PyTypeChecker
call1 = CallModel(call_guid='82763e15-16e0-4915-af4b-695b18b01fce', call_id=1, host='user',
                  starts_at='2021-05-20 18:30', finished_at='2021-05-20 18:31',
                  phone='+79266515960', status='finished')

# noinspection PydanticTypeChecker,PyTypeChecker
call2 = CallModel(call_guid='fea78309-584e-4eca-9889-6bad0b08e0ee', call_id=2, host='operator',
                  starts_at='2021-05-20 19:30', finished_at='2021-05-20 19:31',
                  phone='+79266515961', status='finished', topic='Влияние погоды на москвичей')


@pytest.fixture
async def test_data():
    from some_tt import db
    await db.init()

    await db.Calls.calls.collection.drop()
    await db.Calls.calls.create_indexes()

    for call in [call1, call2]: await db.Calls.calls.save(call)
