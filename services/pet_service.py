from typing import List

from fastapi import HTTPException
from sqlalchemy.orm import Session

from repositories.pet_repository import PetRepository
from schemas.pet import CreatePet
from schemas.pet import Pet as PetSchema


class PetService:
    def __init__(self, db: Session):
        self.pet_repository = PetRepository(db)

    def get_pet_by_id(self, pet_id: str) -> PetSchema:
        pet = self.pet_repository.get_by_id(pet_id)
        if not pet:
            raise HTTPException(status_code=404, detail="Pet not found")
        return PetSchema.model_validate(pet)

    def list_all_pets(self, limit: int, offset: int) -> List[PetSchema]:
        pets = self.pet_repository.get_all(limit=limit, offset=offset)
        if not pets:
            return []
        l = []
        for pet in pets:
            p = PetSchema.model_validate(pet)
            l.append(p)
        return l

    def create_pet(self, req: CreatePet) -> PetSchema:
        p = self.pet_repository.create(name=req.name, age=req.age, species=req.species)
        return PetSchema.model_validate(p)

    def update_pet(self, pet_id: int, name: str, species: str) -> PetSchema:
        p = self.pet_repository.update(pet_id, name=name, species=species)
        if not p:
            raise HTTPException(status_code=404, detail="Pet not found")
        return PetSchema.model_validate(p)

    def delete_pet(self, pet_id: int) -> PetSchema:
        pet = self.pet_repository.delete(pet_id)
        if not pet:
            raise HTTPException(status_code=404, detail="Pet not found")
        return PetSchema.model_validate(pet)
