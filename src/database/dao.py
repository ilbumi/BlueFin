from sqlalchemy import select
from .database import async_session_maker


class BaseDAO:
    model = None

    @classmethod
    async def find_all(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalars().all()

    @classmethod
    async def create(cls, **values):
        async with async_session_maker() as session:
            obj = cls.model(**values)
            session.add(obj)
            await session.commit()
