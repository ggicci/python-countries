from dataclasses import dataclass
from pathlib import Path
from typing import Optional

DEFAULT_DATA_DIR = Path(__file__).parent / "database"


@dataclass(frozen=True)
class CountryCode:
    alpha2_code: str
    alpha3_code: str
    numeric_code: str


@dataclass(frozen=True)
class Property:
    country: str  # alpha-3 code
    key: str


class DataLoader:
    def __init__(self, data_dir: Path = DEFAULT_DATA_DIR) -> None:
        self.data_dir = data_dir
        self.countries = {}  # { code: CountryCode }
        self.files = {}  # { field_name: { locale: file } }
        self.dat = {}  # { field_name: { locale: { alpha3_code: value } } }
        self.load_database()

    def load_database(self) -> None:
        self.__load_country_codes()
        self.__build_data_file_index()
        for field_name, locale_files in self.files.items():
            for locale, file in locale_files.items():
                self.__load_data_file(field_name, locale, file)

    def lookup(self, field: Property, locale: str = "en") -> Optional[str]:
        """Lookup a property value with specified locale."""
        locale_data = self.dat.get(field.key, {})
        return locale_data.get(locale, {}).get(field.country, None)

    def lookup_country_code(self, code: str) -> Optional["CountryCode"]:
        """Lookup country code by alpha-3 code, alpha-2 code, or numeric code."""
        return self.countries.get(code)

    def __load_country_codes(self) -> None:
        with open(self.data_dir / "codes.tsv") as f:
            for line in f:
                alpha2_code, alpha3_code, numeric_code = line.strip().split("\t")
                code = CountryCode(
                    alpha2_code=alpha2_code,
                    alpha3_code=alpha3_code,
                    numeric_code=numeric_code,
                )
                self.countries[alpha3_code] = code
                self.countries[alpha2_code] = code
                self.countries[numeric_code] = code

    def __build_data_file_index(self) -> None:
        for file in self.data_dir.glob("*/*.tsv"):
            if not file.is_file():
                raise ValueError(f"File {file} is not a file")
            relative = file.relative_to(
                self.data_dir
            )  # e.g. "name/en.tsv", "capital/zh.tsv", etc.
            field_name = relative.parent.name  # e.g. "name", "capital", etc.
            locale = relative.stem  # e.g. "en", "zh", etc.
            if field_name not in self.files:
                self.files[field_name] = {}
            self.files[field_name][locale] = file

    def __load_data_file(self, field_name: str, locale: str, file: Path) -> None:
        if field_name not in self.dat:
            self.dat[field_name] = {}
        if locale not in self.dat[field_name]:
            self.dat[field_name][locale] = {}
        with open(file) as f:
            for line in f:
                alpha2_code, value = line.strip().split("\t")
                self.dat[field_name][locale][alpha2_code] = value
