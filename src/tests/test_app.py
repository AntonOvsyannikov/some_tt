import json

import httpx


# noinspection PyUnusedLocal
def test_app(cli: httpx.Client, test_data):
    resp = cli.get('/calls')
    assert resp.status_code == 200
    assert resp.json() == json.loads("""
    {
        "data": [
            {
                "call_guid": "82763e15-16e0-4915-af4b-695b18b01fce",
                "call_id": 1,
                "host": "user",
                "starts_at": "2021-05-20T18:30:00",
                "finished_at": "2021-05-20T18:31:00",
                "phone": "+79266515960",
                "status": "finished",
                "result": "---",
                "topic": "Тематика",
                "tags": [],
                "media_id": "some"
            },
            {
                "call_guid": "fea78309-584e-4eca-9889-6bad0b08e0ee",
                "call_id": 2,
                "host": "operator",
                "starts_at": "2021-05-20T19:30:00",
                "finished_at": "2021-05-20T19:31:00",
                "phone": "+79266515961",
                "status": "finished",
                "result": "---",
                "topic": "Влияние погоды на москвичей",
                "tags": [],
                "media_id": "some"
            }
        ],
        "page": 0,
        "page_size": 15,
        "sort": "asc",
        "total": 2,
        "filter": {
            "phone": null,
            "topic": null
        }
    }
    """)

    resp = cli.get('/calls?page_size=1&page=1&sort=dsc')
    assert resp.status_code == 200
    assert resp.json() == json.loads("""
    {
        "data": [
            {
                "call_guid": "82763e15-16e0-4915-af4b-695b18b01fce",
                "call_id": 1,
                "host": "user",
                "starts_at": "2021-05-20T18:30:00",
                "finished_at": "2021-05-20T18:31:00",
                "phone": "+79266515960",
                "status": "finished",
                "result": "---",
                "topic": "Тематика",
                "tags": [],
                "media_id": "some"
            }
        ],
        "page": 1,
        "page_size": 1,
        "sort": "dsc",
        "total": 2,
        "filter": {
            "phone": null,
            "topic": null
        }
    }
    """)

    resp = cli.get('/calls?filter_topic=погод')
    assert resp.status_code == 200
    assert resp.status_code == 200
    assert resp.json() == json.loads("""
    {
        "data": [
            {
                "call_guid": "fea78309-584e-4eca-9889-6bad0b08e0ee",
                "call_id": 2,
                "host": "operator",
                "starts_at": "2021-05-20T19:30:00",
                "finished_at": "2021-05-20T19:31:00",
                "phone": "+79266515961",
                "status": "finished",
                "result": "---",
                "topic": "Влияние погоды на москвичей",
                "tags": [],
                "media_id": "some"
            }
        ],
        "page": 0,
        "page_size": 15,
        "sort": "asc",
        "total": 2,
        "filter": {
            "phone": null,
            "topic": "погод"
        }
    }
    """)