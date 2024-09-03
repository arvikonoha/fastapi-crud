from app.db.models.user import User
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserUpdate


async def get_user(user_id: int, db: Session):
    return db.query(User).filter(User.id == user_id).first()


async def update_user(user_id: int, user_update: UserUpdate, db: Session):
    user = await get_user(user_id, db)

    # Update only the fields that are passed
    if user:
        update_data = user_update.dict(exclude_unset=True)  # Get only the fields that are provided in the request

        for key, value in update_data.items():
            setattr(user, key, value)  # Set attribute on the user object
        db.commit()
        db.refresh(user)
        return user
    else:
        return None


async def create_user(user: UserCreate, db: Session):
    db_user = User(email=user.email, password=user.password, first_name=user.first_name, last_name=user.last_name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


async def delete_user(user_id: int, db: Session):
    user = await get_user(user_id, db)
    if user:
        db.delete(user)
        db.commit()
        return user_id
    else:
        raise None
