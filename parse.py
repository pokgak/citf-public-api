import pandas as pd

malaysia = pd.read_csv("../citf-public/vax_malaysia.csv")

# daily
daily_stats = pd.melt(
    malaysia,
    id_vars=["date"],
    value_vars=["dose1_daily", "dose2_daily", "total_daily"],
    var_name="type",
    value_name="count",
).replace({"dose1_daily": "first", "dose2_daily": "second", "total_daily": "total"})

# cumulative
cumulative_stats = pd.melt(
    malaysia,
    id_vars=["date"],
    value_vars=["dose1_cumul", "dose2_cumul", "total_cumul"],
    var_name="type",
    value_name="count",
).replace({"dose1_cumul": "first", "dose2_cumul": "second", "total_cumul": "total"})
