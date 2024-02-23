from typing import List

from fastapi import APIRouter

from dependences.db import SessionDeps
from dependences.pagination import PaginationDeps
from schemas.pet import CreatePet, Pet
from services.pet_service import PetService

router = APIRouter(prefix="/pets")


@router.get("/{pet_id}", response_model=Pet)
def get_pet_by_id(pet_id: str, session: SessionDeps):
    service = PetService(session)
    return service.get_pet_by_id(pet_id)


@router.get("/", response_model=List[Pet])
def list_all_pets(session: SessionDeps, pagination: PaginationDeps):
    service = PetService(session)
    return service.list_all_pets(pagination.limit, pagination.offset)


@router.post("/", response_model=Pet)
def create_pet(request: CreatePet, session: SessionDeps):
    service = PetService(session)
    return service.create_pet(request)
