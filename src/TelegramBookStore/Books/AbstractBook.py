from abc import ABC
from dataclasses import dataclass
from typing import Optional


@dataclass
class AbstractBook(ABC):
    id: Optional[int]
    title: Optional[str]
    description: Optional[str]
    price: Optional[float]
    pages: Optional[int]
    imageUrl: Optional[str]

    def getId(self):
        return self.id

    def getTitle(self):
        return self.title

    def getDescription(self):
        return self.description

    def getPrice(self):
        return str(self.price)

    def getImageUrl(self):
        return self.imageUrl




