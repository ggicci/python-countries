from dataclasses import dataclass
from pathlib import Path

from countries.core import CountryPropertiesBase, Property

CUSTOM_DATA_DIR = Path(__file__).parent / "custom"
TOTAL_COUNTRIES = 249


@dataclass(frozen=True)
class CustomCountry(CountryPropertiesBase):
    flag: Property
    national_flower: Property


@dataclass(frozen=True)
class CustomCountryIndex:
    USA: CustomCountry
    CAN: CustomCountry