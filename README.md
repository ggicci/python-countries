# python-countries

<div align="center">

[![Run tests](https://github.com/ggicci/python-countries/actions/workflows/run-tests.yml/badge.svg?branch=main)](https://github.com/ggicci/python-countries/actions/workflows/run-tests.yml)
[![codecov](https://codecov.io/gh/ggicci/python-countries/branch/main/graph/badge.svg?token=DPVPXJLDND)](https://codecov.io/gh/ggicci/python-countries)

</div>

Country Database in Python

- name
- currency
- flag
- official_languages
- ...

See [ggicci/countries](https://github.com/ggicci/countries) for the full list of the properties.

## Install

```bash
pip install country-database
```

## Usage

### Load all countries

```python
from country_database import load_countries

CountryIndex = load_countries()
print(CountryIndex.CAN.alpha2_code) # "CA"
print(CountryIndex.CAN.name) # "Canada"
print(CountryIndex.CAN.name.to_locale("zh")) # "加拿大"


CountryIndexZh = load_countries(locale="zh")
print(CountryIndexZh.CAN.name) # "加拿大"
print(CountryIndexZh.CAN.name.to_locale("en")) # "Canada"
```

### Load one country

```python
from country_database import load_country

ca = load_country("CA") # or "CAN"
print(ca.name) # "Canada"
```

### Load a custom list of countries

```python
from dataclasses import dataclass
from country_database import CountryProperties, load_countries_generic

@dataclass(frozen=True)
class MyCountryIndex:
    CAN: CountryProperties
    USA: CountryProperties
    CHN: CountryProperties

CountryIndex = load_countries_generic(MyCountryIndex)
```

### Add custom properties to a country

The default database is [ggicci/countries](https://github.com/ggicci/countries).
You can add your own data and load them easily by instantiate a [DataLoader](./src/country_database/dataloader.py) and pass it to the `load_countries*`, `load_country*` or just merge your database to the `default_dataloader`.

```python
from pathlib import Path
from dataclasses import dataclass
from country_database import (
    CountryProperties,
    DataLoader,
    FullCountryIndex,
    Property,
)

CUSTOM_DATA_DIR = Path("/path/to/your/custom/data/dir")

# NOTE: if you don't need the fields from the default database,
# you can just inherit CountryPropertiesBase instead of CountryProperties
@dataclass(frozen=True)
class MyCountry(CountryProperties):
    custom_field_1: Property
    custom_field_2: Property


# WAY 1: create a new dataloader.
loader = DataLoader() # will load the default database
loader.merge_database(CUSTOM_DATA_DIR)

# NOTE: If you don't want to load the default database, use the following statement:
# It will create a loader which only loads
# 1. the country codes from the default database;
# 2. data from CUSTOM_DATA_DIR;
# but data from the default database won't be loaded.
#
# loader = DataLoader(CUSTOM_DATA_DIR)

CountryIndex = load_countries_generic(FullCountryIndex[MyCountry], loader=loader)

# WAY 2: merge your database to the default_dataloader.
from country_database import default_dataloader
default_dataloader.merge_database(CUSTOM_DATA_DIR)
CountryIndex = load_countries_generic(FullCountryIndex[MyCountry])
```
