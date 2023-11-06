from datetime import date, datetime
from pydantic import BaseModel, Field, EmailStr


class ContactModel(BaseModel):
    id: int = Field(1, gt=0)
    first_name: str = Field("Taras", min_length=1, max_length=25, title="Ім'я")
    second_name: str = Field("Shechenko", min_length=1, max_length=25, title="Прізвище")
    email: EmailStr
    phone: str = Field(
        "", examples=["+380 44 123-4567"], max_length=25, title="Номер телефону"
    )
    birthday: date
    comments: str = Field("", title="Додаткові дані")
    favorite: bool = False


    # pattern=r"^+[0-9\s\(\)-]+$

class ContactResponse(BaseModel):
    id: int
    first_name: str
    second_name: str
    email: EmailStr
    phone: str
    birthday: date
    comments: str
    favorite: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

    # email: str = Field(default="email@examole.com", pattern=r'^\w+@\w+\.\w+$')


# class Contact(Base):
#     """
#     Ім'я
#     Прізвище
#     Електронна адреса
#     Номер телефону
#     День народження
#     Додаткові дані (необов'язково)
#     """
#     __tablename__ = "contacts"

#     id = Column(Integer, primary_key=True, index=True)
#     first_name = Column(String)
#     second_name = Column(String)
#     email = Column(String)
#     phone = Column(String)
#     birthday = Column(Date)
#     comments = Column(Text)
#     favorite = Column(Boolean, default=False)
#     created_at = Column(DateTime, default=func.now())
#     updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
