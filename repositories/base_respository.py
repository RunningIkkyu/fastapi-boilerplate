from typing import Generic, List, Optional, Type, TypeVar

from sqlalchemy.orm import Session

# Define a generic type for the model
ModelType = TypeVar("ModelType")

LIMIT = 100


class BaseRepository(Generic[ModelType]):
    def __init__(self, session: Session, model_class: Type[ModelType]):
        self.session = session
        self.model_class = model_class

    def get_by_id(self, id: str) -> Optional[ModelType]:
        return self.session.get(self.model_class, id)

    def get_all(self, limit: int = LIMIT, offset: int = 0) -> Optional[List[ModelType]]:
        return self.session.query(self.model_class).offset(offset).limit(limit).all()

    def create(self, **kwargs) -> ModelType:
        instance = self.model_class(**kwargs)
        self.session.add(instance)
        return instance

    def update(self, id: int, **kwargs) -> Optional[ModelType]:
        instance = self.session.get(self.model_class, id)
        for key, value in kwargs.items():
            setattr(instance, key, value)
        self.session.add(instance)
        return instance

    def delete(self, id: int) -> Optional[ModelType]:
        instance = self.session.get(self.model_class, id)
        if instance:
            self.session.delete(instance)
            return None
        return instance
