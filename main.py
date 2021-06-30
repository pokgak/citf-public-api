import json

from enum import Enum
from datetime import date
from typing import Optional
from fastapi import FastAPI, HTTPException
from fastapi.param_functions import Query

from parse import daily_stats, cumulative_stats


class DoseType(str, Enum):
    FIRST = "first"
    SECOND = "second"
    TOTAL = "total"


def get_records(data, date_from, date_until, dose_type, offset, limit):
    if date_from and date_until and date_until < date_from:
        raise HTTPException(400, detail="Until date cannot be bigger than from!")

    tmp = data
    if dose_type is not None:
        tmp = tmp[tmp["type"] == dose_type]

    if date_from is not None:
        tmp = tmp[tmp["date"] >= date_from.isoformat()]

    if date_until is not None:
        tmp = tmp[tmp["date"] <= date_until.isoformat()]

    # FIXME
    # tmp = tmp.loc[offset : offset + limit - 1]

    return {"data": json.loads(tmp.to_json(orient="records"))}


app = FastAPI()


@app.get("/")
async def get_info():
    return {"message": "HELLO WORLD!"}


@app.get("/daily")
async def get_daily(
    date_from: Optional[date] = None,
    date_until: Optional[date] = None,
    dose_type: Optional[DoseType] = None,
    offset: Optional[int] = Query(0, min=0),
    limit: Optional[int] = Query(50, min=0),
):
    return get_records(
        daily_stats,
        date_from=date_from,
        date_until=date_until,
        dose_type=dose_type,
        offset=offset,
        limit=limit,
    )


@app.get("/cumulative")
async def get_cumulative(
    date_from: Optional[date] = None,
    date_until: Optional[date] = None,
    dose_type: Optional[DoseType] = None,
    offset: Optional[int] = Query(0, min=0),
    limit: Optional[int] = Query(50, min=0),
):
    return get_records(
        cumulative_stats,
        date_from=date_from,
        date_until=date_until,
        dose_type=dose_type,
        offset=offset,
        limit=limit,
    )
