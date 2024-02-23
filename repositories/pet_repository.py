from models.pet import Pet
from repositories.base_respository import BaseRepository


class PetRepository(BaseRepository):
    def __init__(self, session):
        super().__init__(session, model_class=Pet)
