from sqlalchemy.orm import Session

from src.shemas import ContactResponse
from src.database.models import Contact


async def get_contacts(db: Session):
    owners = db.query(Contact).all()
    return owners
