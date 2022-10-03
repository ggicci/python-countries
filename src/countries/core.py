from dataclasses import dataclass, fields
from pathlib import Path
from typing import Type, TypeVar

from .dataloader import CountryCode, DataLoader

# the builtin dataloader with the default database loaded
default_dataloader = DataLoader()


def merge_database(
    data_dir: Path,
    override_level: DataLoader.OverrideLevel = DataLoader.OverrideLevel.ITEM,
    reload=True,
) -> None:
    """Merge a new database into the data loader.

    Raises:
        ValueError: if the database is already loaded or the database is invalid.
    """
    default_dataloader.merge_database(data_dir, override_level, reload)


class Property(str):
    __slots__ = "_key"

    def __new__(cls, country_code: str, attr: str, locale: str = "en"):
        return super().__new__(
            cls,
            _empty_if_none(
                default_dataloader.lookup(country_code, attr, locale=locale)
            ),
        )

    def __init__(self, country_code: str, attr: str, locale: str = "en"):
        self._key = (country_code, attr)

    @property
    def key(self) -> str:
        return self._key

    def to_locale(self, locale: str) -> str:
        """Get the translation of the given `locale`.

        Returns:
            The translation string, None if not found.
        """
        return _empty_if_none(default_dataloader.lookup(*self.key, locale=locale))

    def __deepcopy__(self, memo):
        """Return a copy of the Property object. Since the object is immutable, we just return self."""
        return self  # property is read-only


@dataclass(frozen=True)
class CountryData(CountryCode):
    locale: str
    name: Property

    def lookup(self, attr: str) -> Property:
        """Lookup a property value of the current country, with default locale `en`.

        Args:
            attr: name of the property

        Returns:
            The named property.
        """
        return Property(country_code=self.alpha3_code, attr=attr, locale=self.locale)

    def to_locale(self, locale: str) -> "CountryData":
        return load_country(self.alpha3_code, locale=locale)


CountryDataType = TypeVar("CountryDataType", bound=CountryData)


def load_country(
    alpha3_code: str,
    locale: str = "en",
    data_cls: Type[CountryDataType] = CountryData,
) -> CountryDataType:
    """Load a country from the database.

    Returns:
        The country data.

    Raises:
        KeyError: if the country is not found.
    """
    code = default_dataloader.lookup_country_code(alpha3_code)
    if code is None:
        raise KeyError(f"Country code `{alpha3_code}` not found")

    # memo_key = (alpha3_code, locale)
    # if memo_key in __memo:
    #     return __memo[memo_key]

    kwargs = {}
    for fld in fields(data_cls):
        if fld.name == "locale":
            kwargs[fld.name] = locale
            continue
        if fld.name == "alpha2_code":
            kwargs[fld.name] = code.alpha2_code
            continue
        if fld.name == "alpha3_code":
            kwargs[fld.name] = code.alpha3_code
            continue
        if fld.name == "numeric_code":
            kwargs[fld.name] = code.numeric_code
            continue

        kwargs[fld.name] = Property(
            country_code=alpha3_code,
            attr=fld.name,
            locale=locale,
        )

    data = data_cls(**kwargs)
    # __memo[memo_key] = data
    return data


def _empty_if_none(value):
    if value is None:
        return ""
    return value


@dataclass(frozen=True)
class CustomCountryData(CountryData):
    age: Property
