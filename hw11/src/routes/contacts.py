from typing import List

from fastapi import Path, Depends, HTTPException, status, APIRouter
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from src.database.db import get_db
from src.shemas import ContactModel, ContactResponse
from src.repository import contacts as repository_contacts


router = APIRouter(prefix="/contacts", tags=["contacts"])


@router.get("", response_model=List[ContactResponse])
async def get_contacts(db: Session = Depends(get_db)):
    contacts = await repository_contacts.get_contacts(db)
    return contacts
