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
    country_code: str  # alpha-3 code
    key: str


class DataLoader:
    class OverrideLevel:
        """
        Override level for merging databases.

        {
            field_name: { // <-- FIELD level
                locale: { // <-- LOCALE level
                    country_code: value // ITEM level
                }
            }
        }
        """

        FIELD = 1
        LOCALE = 2
        ITEM = 3

    def __init__(self, data_dir: Path = DEFAULT_DATA_DIR) -> None:
        self.databases = []  # [ (Path, OverrideLevel) ]
        self.countries = {}  # { code: CountryCode }
        self.files = {}  # { field_name: { locale: file } }
        self.dat = {}  # { field_name: { locale: { alpha3_code: value } } }
        self.merge_database(data_dir)

    def merge_database(
        self, data_dir: Path, override_level: OverrideLevel = OverrideLevel.ITEM
    ) -> None:
        """
        Merge a new database into the data loader.

        Raises:
            ValueError: if the database is already loaded or the database is invalid.
        """
        if data_dir in self.databases:
            raise ValueError(f"Database {data_dir} already loaded")
        self.__load_database(data_dir, override_level)

    def __load_database(self, data_dir: Path, override_level: OverrideLevel) -> None:
        if not self.countries:
            self.__load_country_codes(data_dir)  # only load countries once
        files = self.__build_data_file_index(data_dir)
        for field_name, locale_files in files.items():
            for locale, file in locale_files.items():
                self.__load_data_file(field_name, locale, file, override_level)
        self.databases.append((data_dir, override_level))

    def lookup(self, country_code: str, key: str, locale: str = "en") -> Optional[str]:
        """Lookup a property value with specified locale."""
        locale_data = self.dat.get(key, {})
        return locale_data.get(locale, {}).get(country_code, None)

    def lookup_country_code(self, code: str) -> Optional["CountryCode"]:
        """Lookup country code by alpha-3 code, alpha-2 code, or numeric code."""
        return self.countries.get(code)

    def __load_country_codes(self, data_dir: Path) -> None:
        with open(data_dir / "codes.tsv") as f:
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

    def __build_data_file_index(self, data_dir: Path) -> dict:
        files = {}  # { field_name: { locale: file } }
        for file in data_dir.glob("*/*.tsv"):
            if not file.is_file():
                raise ValueError(f"File {file} is not a file")
            relative = file.relative_to(
                data_dir
            )  # e.g. "name/en.tsv", "capital/zh.tsv", etc.
            field_name = relative.parent.name  # e.g. "name", "capital", etc.
            locale = relative.stem  # e.g. "en", "zh", etc.
            if field_name not in files:
                files[field_name] = {}
            files[field_name][locale] = file
        return files

    def __load_data_file(
        self, field_name: str, locale: str, file: Path, override_level: OverrideLevel
    ) -> None:
        # update self.files
        if field_name not in self.files:
            self.files[field_name] = {}
        self.files[field_name][locale] = file

        if field_name not in self.dat or override_level == self.OverrideLevel.FIELD:
            self.dat[field_name] = {}

        if (
            locale not in self.dat[field_name]
            or override_level == self.OverrideLevel.LOCALE
        ):
            self.dat[field_name][locale] = {}

        with open(file) as f:
            for line in f:
                alpha2_code, value = line.strip().split("\t")
                self.dat[field_name][locale][alpha2_code] = value
