import pathlib

import tomllib

path = pathlib.Path(__file__).parent / "gntidy.toml"
with path.open(mode="rb") as fp:
    gntidy = tomllib.load(fp)
