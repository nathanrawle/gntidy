import sys
from pathlib import Path
from types import ModuleType

import pandas as pd
from pandas import DataFrame, Series

from config import gntidy as CFG

data_dir = Path(CFG["data"]["dir"])


class gnt_callable(ModuleType):
    def __init__(self):
        super().__init__(__name__)
        self.a1_to_ctr = pd.read_csv(data_dir / "a1_to_ctr.csv", index_col=["admin1"])
        self.a2_a1_to_ctr = pd.read_csv(
            data_dir / "a2_a1_to_ctr.csv", index_col=["admin2", "admin1"]
        )
        self.a2_ctr_to_a1 = pd.read_csv(
            data_dir / "a2_ctr_to_a1.csv", index_col=["admin2", "admin1"]
        )
        self.a2_to_a1 = pd.read_csv(data_dir / "a2_to_a1.csv", index_col=["admin2"])
        self.a2_to_ctr = pd.read_csv(data_dir / "a2_to_ctr.csv", index_col=["admin2"])
        self.ctran_to_ctr = pd.read_csv(
            data_dir / "ctran_to_ctr.csv", index_col=["admin2", "admin1"]
        )
        self.cty_a1_ctr_to_a2 = pd.read_csv(
            data_dir / "cty_a1_ctr_to_a2.csv", index_col=["name", "admin1", "country"]
        )
        self.cty_a1_to_a2 = pd.read_csv(
            data_dir / "cty_a1_to_a2.csv", index_col=["name", "admin1"]
        )
        self.cty_a1_to_ctr = pd.read_csv(
            data_dir / "cty_a1_to_ctr.csv", index_col=["name", "admin1"]
        )
        self.cty_a2_a1_to_ctr = pd.read_csv(
            data_dir / "cty_a2_a1_to_ctr.csv", index_col=["name", "admin2", "admin1"]
        )
        self.cty_a2_ctr_to_a1 = pd.read_csv(
            data_dir / "cty_a2_ctr_to_a1.csv", index_col=["name", "admin2", "country"]
        )
        self.cty_a2_to_a1 = pd.read_csv(
            data_dir / "cty_a2_to_a1.csv", index_col=["name", "admin2"]
        )
        self.cty_a2_to_ctr = pd.read_csv(
            data_dir / "cty_a2_to_ctr.csv", index_col=["name", "admin2"]
        )
        self.cty_ctr_to_a1 = pd.read_csv(
            data_dir / "cty_ctr_to_a1.csv", index_col=["name", "admin2", "country"]
        )
        self.cty_ctr_to_a2 = pd.read_csv(
            data_dir / "cty_ctr_to_a2.csv", index_col=["name", "admin2", "country"]
        )
        self.cty_to_a1 = pd.read_csv(
            data_dir / "cty_to_a1.csv", index_col=["name", "admin2", "country"]
        )
        self.cty_to_a2 = pd.read_csv(
            data_dir / "cty_to_a2.csv", index_col=["name", "admin2", "country"]
        )
        self.cty_to_ctr = pd.read_csv(
            data_dir / "cty_to_ctr.csv", index_col=["name", "admin2", "country"]
        )
        self.ctyan_a1_to_cty = pd.read_csv(
            data_dir / "ctyan_a1_to_cty.csv", index_col=["alternatename", "admin1"]
        )
        self.ctyan_a2_to_cty = pd.read_csv(
            data_dir / "ctyan_a2_to_cty.csv", index_col=["alternatename", "admin2"]
        )
        self.ctyan_ctr_to_cty = pd.read_csv(
            data_dir / "ctyan_ctr_to_cty.csv", index_col=["alternatename", "country"]
        )

    def __call__(self, df: DataFrame, in_place=False):
        if not in_place:
            df = df.copy()

        df.country = df["country"].map(self.ctran_to_ctr)


sys.modules[__name__] = gnt_callable()
