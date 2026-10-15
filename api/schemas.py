from typing import Any
from pydantic import BaseModel, Field, ConfigDict


class AnaliseCreate(BaseModel):
    cidade: str = Field(min_length=2)
    tipo_imovel: str = Field(min_length=2)
    finalidade: str = Field(min_length=2)
    preco_maximo: float | None = Field(default=None, gt=0)
    quartos: int | None = Field(default=None, ge=1)
    area_minima: float | None = Field(default=None, gt=0)
    bairros: str | None = None

class AnaliseUpdate(BaseModel):
     model_config = ConfigDict(extra="forbid")
     cidade: str = Field(min_length=2)

class AnaliseResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    cidade: str
    relatorio: dict[str, Any] | list[Any] | str