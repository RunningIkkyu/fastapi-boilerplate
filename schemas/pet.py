from pydantic import BaseModel, ConfigDict


class CommonFields(BaseModel):
    name: str
    age: int
    species: str


class Pet(BaseModel):
    config = ConfigDict(from_attributes=True)

    id: str
    name: str
    age: int
    species: str


class CreatePet(BaseModel):
    name: str
    age: int
    species: str


class UpdatePeg(BaseModel):
    id: str
    name: str
    age: int
    species: str
