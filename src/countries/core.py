from dataclasses import dataclass

from .dataloader import CountryCode, DataLoader, Property

_dataloader = DataLoader()


class StringField(str):
    def __new__(cls, field: Property) -> "StringField":
        default_value = _dataloader.lookup(field)  # default is "en" value
        return super().__new__(cls, default_value)

    def __init__(self, field: Property) -> None:
        super().__init__()
        self.field = field

    def to_locale(self, locale: str) -> str:
        return _dataloader.lookup(self.field, locale=locale)


@dataclass(frozen=True)
class CountryData(CountryCode):
    name: StringField


def load_country(alpha3_code: str) -> CountryData:
    code = _dataloader.lookup_country_code(alpha3_code)
    if code is None:
        raise KeyError(f"Country code `{alpha3_code}` not found")

    return CountryData(
        **code.__dict__,
        name=StringField(Property(alpha3_code, "name")),
    )
