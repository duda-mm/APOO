# model/item.py
from dataclasses import dataclass
from typing import Optional

@dataclass
class Item:
    id: Optional[int] = None
    nome: str = ""
    descricao: str = ""
    quantidade: int = 0