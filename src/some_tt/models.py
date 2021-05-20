from datetime import datetime
from typing import List, TypeVar, Generic

from pydantic import BaseModel
from pydantic.generics import GenericModel
from typing_extensions import Literal


class CallModel(BaseModel):
    call_guid: str = None
    call_id: int

    host: Literal['user', 'operator']  # для отображения иконки человечка или гарнитуры

    starts_at: datetime
    finished_at: datetime
    # продолжительность посчитаем на клиенте

    phone: str

    status: Literal['started', 'finished']
    result: str = '---'
    topic: str = 'Тематика'

    tags: List[str] = []

    media_id: str = 'some'  # как организовать отдачу медиафайлов - отдельный вопрос (например по rstp), в приложении не представлено


class Filter(BaseModel):
    # конкретный набор фильтров зависит от требований
    phone: str = None
    topic: str = None


Sort = Literal['asc', 'dsc']
T = TypeVar('T')


class Meta(GenericModel, Generic[T]):
    data: T
    page: int
    page_size: int
    sort: Sort
    total: int
    filter: Filter
