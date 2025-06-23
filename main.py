from typing import Union

from fastapi import FastAPI
from fastapi_utilities import repeat_every

import requests

import FuelPriceAggregator
from contextlib import asynccontextmanager
import asyncio

app = FastAPI()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: fetch prices every hour in the background

    async def periodic_fetch():
        global FuelPriceAggregator
        while True:
            FuelPriceAggregator = FuelPriceAggregator.fetch_all()
            await asyncio.sleep(3600)

    task = asyncio.create_task(periodic_fetch())
    yield
    task.cancel()

app = FastAPI(lifespan=lifespan)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/prices/asda")
def return_asda_prices():
    r = requests.get("https://storelocator.asda.com/fuel_prices_data.json")
    r.raise_for_status()
    return r.json()

@app.get("/prices/bp")
def return_bp_prices():
    r = requests.get("https://www.bp.com/en_gb/united-kingdom/home/fuelprices/fuel_prices_data.json")
    r.raise_for_status()
    return r.json()

@app.get("/prices/esso")
def return_esso_prices():
    r = requests.get("https://fuelprices.esso.co.uk/latestdata.json")
    r.raise_for_status()
    return r.json()

# @app.get("/prices/jet")
# def return_jet_prices():
#     r = requests.get("https://jetlocal.co.uk/fuel_prices_data.json")
#     r.raise_for_status()
#     return r.json()

@app.get("/prices/morrisons")
def return_morrisons_prices():
    r = requests.get("https://www.morrisons.com/fuel-prices/fuel.json")
    r.raise_for_status()
    return r.json()

@app.get("/prices/moto")
def return_moto_prices():
    r = requests.get("https://moto-way.com/fuel-price/fuel_prices.json")
    r.raise_for_status()
    return r.json()

@app.get("/prices/motorfuelgroup")
def return_motorfuel_group_prices():
    r = requests.get("https://fuel.motorfuelgroup.com/fuel_prices_data.json")
    r.raise_for_status()
    return r.json()

@app.get("/prices/rontec")
def return_rontec_prices():
    r = requests.get("https://www.rontec-servicestations.co.uk/fuel-prices/data/fuel_prices_data.json")
    r.raise_for_status()
    return r.json()

@app.get("/prices/sainsburys")
def return_sainsburys_prices():
    r = requests.get("https://api.sainsburys.co.uk/v1/exports/latest/fuel_prices_data.json")
    r.raise_for_status()
    return r.json()

@app.get("/prices/sgn")
def return_sgn_prices():
    r = requests.get("https://www.sgnretail.uk/files/data/SGN_daily_fuel_prices.json")
    r.raise_for_status()
    return r.json()

@app.get("/prices/shell")
def return_shell_prices():
    r = requests.get("https://www.shell.co.uk/fuel-prices-data.html")
    r.raise_for_status()
    return r.json()

@app.get("/prices/tesco")
def return_tesco_prices():
    r = requests.get("https://www.tesco.com/fuel_prices/fuel_prices_data.json")
    r.raise_for_status()
    return r.json()
    


