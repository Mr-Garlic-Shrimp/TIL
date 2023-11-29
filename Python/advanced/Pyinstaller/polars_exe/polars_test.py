#!/bin/python3
import polars as pl

df = pl.Dataframe({'a': [1, 2, 3], 'b': [-1, -2, -3] })
print(df)
