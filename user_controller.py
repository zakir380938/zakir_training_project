from fastapi import APIRouter, Depends, status
from schema import UserCreateRequest
from database import get_db
from service import UserService
from sqlalchemy.orm import session

router=APIRouter(
    prefix="/user",

)
@router.post("/create")
def create_user(payload: UserCreateRequest, db: session = Depends(get_db)):
    service = UserService()
    return service.creat_user(db, payload)

@router.get("/list")
def get_all_users(db: session = Depends(get_db)):
    service = UserService()
    return service.get_all_users(db)

@router.get("/{email}")
def get_user_by_email(email:str, db: session = Depends(get_db)):
    service = UserService()
    return service.get_user_by_email(db, email)

@router.delete("/{email}")
def delete_user_by_email(email:str, db: session = Depends(get_db)):
    service= UserService()
    return service.delet_by_mail(db, email)