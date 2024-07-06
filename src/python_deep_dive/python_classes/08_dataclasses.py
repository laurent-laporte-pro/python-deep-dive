import sys
import typing as t
from dataclasses import dataclass


def validate_year(year: int) -> int:
    if not 1900 <= year <= 2024:
        raise ValueError("L'année doit être comprise entre 1900 et 2024.")
    return year


@dataclass
class Vehicle:
    marque: str
    modèle: str
    année: int

    def __post_init__(self):
        self.année = validate_year(self.année)


# L'année 2020 est valide
véhicule = Vehicle("Toyota", "Corolla", 2020)

try:
    # L'année 2025 est invalide
    véhicule = Vehicle("Toyota", "Corolla", 2025)  # Lève une ValueError
except ValueError as e:
    print(e, file=sys.stderr)
else:
    print("L'année est valide.")


class _GPS(t.NamedTuple):
    latitude: float
    longitude: float


class GPS(_GPS):
    def __new__(cls, latitude: float, longitude: float):
        if not -90 <= latitude <= 90:
            raise ValueError("La latitude doit être comprise entre -90 et 90.")
        if not -180 <= longitude <= 180:
            raise ValueError("La longitude doit être comprise entre -180 et 180.")
        return super().__new__(cls, latitude, longitude)


# Les coordonnées de Paris sont valides
gps1 = GPS(48.8566, 2.3522)

try:
    gps2 = GPS(91, 2.3522)  # Lève une ValueError
except ValueError as e:
    print(e, file=sys.stderr)
else:
    print("Les coordonnées sont valides.")
