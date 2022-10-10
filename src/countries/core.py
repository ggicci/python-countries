from dataclasses import dataclass, fields, is_dataclass
from typing import Type, TypeVar

from .dataloader import CountryCode, DataLoader
from .property import Property

# the builtin dataloader with the default database loaded
default_dataloader = DataLoader()


@dataclass(frozen=True)
class CountryPropertiesBase(CountryCode):
    _dataloader: "DataLoader"
    locale: str

    def __post_init__(self):
        # trick: hide "_dataloader" from asdict output
        self.__dataclass_fields__.pop("_dataloader", None)

    def lookup(self, name: str) -> Property:
        """Lookup a property value of the current country, with default locale `en`.

        Args:
            name: name of the property

        Returns:
            The named property.
        """
        return Property(
            loader=self._dataloader,
            country_code=self.alpha3_code,
            name=name,
            locale=self.locale,
        )

    def to_locale(self, locale: str):
        return load_country_generic(
            type(self),
            self.alpha3_code,
            locale=locale,
            loader=self._dataloader,
        )


@dataclass(frozen=True)
class CountryProperties(CountryPropertiesBase):
    name: Property


T_CountryProperties = TypeVar("T_CountryProperties", bound=CountryPropertiesBase)


def load_country_generic(
    country_cls: Type[T_CountryProperties],
    fuzzy_code: str,
    locale: str = "en",
    loader: DataLoader = default_dataloader,
) -> T_CountryProperties:
    """Load a country from the database.

    Args:
        fuzzy_code: can be alpha-3 code, alpha-2 code, or numeric code.
        locale: the default locale of the property values.
        country_cls: a dataclass representing a country with named properties.
        loader: the dataloader.

    Returns:
        The country data.

    Raises:
        KeyError: if the country is not found.
    """
    code = loader.lookup_country_code(fuzzy_code)
    if code is None:
        raise KeyError(f"Country code `{fuzzy_code}` not found")

    if not is_dataclass(country_cls):
        raise ValueError(f"country_cls `{country_cls}` must be a frozen dataclass")

    # memo_key = (alpha3_code, locale)
    # if memo_key in __memo:
    #     return __memo[memo_key]

    kwargs = {
        "_dataloader": loader,
        "locale": locale,
        "alpha2_code": code.alpha2_code,
        "alpha3_code": code.alpha3_code,
        "numeric_code": code.numeric_code,
    }
    for fld in fields(country_cls):
        if fld.name in kwargs:
            continue

        kwargs[fld.name] = Property(
            loader=loader,
            country_code=code.alpha3_code,
            name=fld.name,
            locale=locale,
        )

    data = country_cls(**kwargs)
    # __memo[memo_key] = data
    return data


def load_country(
    fuzzy_code: str, locale: str = "en", loader: DataLoader = default_dataloader
) -> CountryProperties:
    return load_country_generic(
        CountryProperties, fuzzy_code, locale=locale, loader=loader
    )
