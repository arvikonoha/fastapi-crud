from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.user import User, UserCreate, UserUpdate
from app.db.session import get_db
from app.crud.users import create_user, update_user, get_user, delete_user

router = APIRouter()


@router.post("/", response_model=User)
async def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    new_user = await create_user(user=user, db=db)
    return new_user


@router.put("/{user_id}", response_model=User)
async def update_prev_user(user_id: int, user_update: UserUpdate, db: Session = Depends(get_db)):
    updated_user = await update_user(user_id, user_update=user_update, db=db)
    return updated_user


@router.get("/{user_id}", response_model=User)
async def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    user = await get_user(user_id, db=db)
    return user


@router.delete("/{user_id}", response_model=int)
async def delete_user_by_id(user_id: int, db: Session = Depends(get_db)):
    user_id = await delete_user(user_id, db=db)
    return user_id
