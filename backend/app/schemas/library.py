from pydantic import BaseModel


class LibraryCreate(BaseModel):
    name: str
    location: str


class LibraryUpdate(LibraryCreate):
    pass


class Library(LibraryCreate):
    id: int

    class Config:
        orm_mode = True
