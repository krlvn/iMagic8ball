from sqlalchemy.future import select
from sqlalchemy.sql import functions

from engine import db_session
from models import User

async def get_user_by_uid(uid):
    """
    Ищет одного пользователя по id телеграм.
    :param tg_uid:
    :return:
    """
    async with db_session() as session:
        sql = select(User).where(User.id == uid).limit(1)
        request = await session.execute(sql)
        user = request.scalar_one_or_none()
    print(user)
    return user

async def get_or_create_user(uid, language):
    """
    Метод ищет существующую запись или создаёт новую запись в БД
    с языком, который определён в телеграм
    :param uid: id пользователя telegram
    :return:
    """
    user = await get_user_by_uid(uid)
    if user:
        print(user)
        return user
    else:
        new_user = User(id=uid, language=language)
        async with db_session() as session:
            session.add(new_user)
            await session.commit()
        print(new_user)
        return new_user

async def update_user(uid, **columns):
    """
    Метод обновляет данные пользователя в БД.
    Обязательно передаём id, и факультативно поля, которые нужно обновить.
    :param tg_uid:
    :return:
    """
    user = await get_user_by_uid(uid)
    if not user:
        return None

    for k, v in columns.items():
        if hasattr(user, k):
            setattr(user, k, v)

    async with db_session() as session:
        session.add(user)
        await session.commit()
    return user
