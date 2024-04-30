from typing import Any, List
from fastapi import APIRouter, HTTPException
from sqlalchemy import select, func
from starlette.responses import Response

from app.deps.db import CurrentAsyncSession
from app.models.library import Library
from app.schemas.library import Library as LibrarySchema, LibraryCreate, LibraryUpdate
from app.deps.request_params import LibraryRequestParams

router = APIRouter(prefix="/libraries")

@router.get("", response_model=List[LibrarySchema])
async def get_libraries(response: Response, session: CurrentAsyncSession, request_params: LibraryRequestParams) -> Any:
    total = await session.scalar(
        select(func.count(Library.id))
    )
    libraries = (await session.execute(select(Library))).scalars().all()
    response.headers[
        "Content-Range"
    ] = f"{request_params.skip}-{request_params.skip + len(libraries)}/{total}"
    return libraries

@router.post("", response_model=LibrarySchema, status_code=201)
async def create_library(library_in: LibraryCreate, session: CurrentAsyncSession) -> Any:
    library = Library(**library_in.dict())
    session.add(library)
    await session.commit()
    return library

@router.put("/{library_id}", response_model=LibrarySchema)
async def update_library(library_id: int, library_in: LibraryUpdate, session: CurrentAsyncSession) -> Any:
    library: Library = await session.get(Library, library_id)
    if not library:
        raise HTTPException(404)
    update_data = library_in.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(library, field, value)
    session.add(library)
    await session.commit()
    return library

@router.get("/{library_id}", response_model=LibrarySchema)
async def get_library(library_id: int, session: CurrentAsyncSession) -> Any:
    library: Library = await session.get(Library, library_id)
    if not library:
        raise HTTPException(404)
    return library

@router.delete("/{library_id}")
async def delete_library(library_id: int, session: CurrentAsyncSession) -> Any:
    library: Library = await session.get(Library, library_id)
    if not library:
        raise HTTPException(404)
    session.delete(library)
    await session.commit()
    return {"success": True}
