from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from app.dependency import get_db
from app.services import operations as operations_service
from app.models import User
from app.dependency import get_current_user

from app.schemas import OperationRequest

router = APIRouter()


@router.post("/operations/income")
def add_income(operation: OperationRequest, db: Session = Depends(get_db),
               current_user: User = Depends(get_current_user)):
    return operations_service.add_income(db, current_user, operation)


@router.post("/operations/expense")
def add_expense(operation: OperationRequest, db: Session = Depends(get_db),
                current_user: User = Depends(get_current_user)):
    return operations_service.add_expense(db, current_user, operation)
