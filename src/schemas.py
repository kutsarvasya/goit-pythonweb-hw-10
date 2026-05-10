from datetime import date

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class ContactModel(BaseModel):
    first_name: str = Field(max_length=50)
    last_name: str = Field(max_length=50)
    email: EmailStr
    phone: str = Field(max_length=20)
    birthday: date
    additional_data: str | None = Field(default=None, max_length=250)


class ContactUpdate(ContactModel):
    pass


class ContactResponse(ContactModel):
    id: int

    model_config = ConfigDict(from_attributes=True)
