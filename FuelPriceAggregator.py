import requests

class FuelPriceAggregator:
    PROVIDERS = {
        "asda": "https://storelocator.asda.com/fuel_prices_data.json",
        "bp": "https://www.bp.com/en_gb/united-kingdom/home/fuelprices/fuel_prices_data.json",
        "esso": "https://fuelprices.esso.co.uk/latestdata.json",
        "morrisons": "https://www.morrisons.com/fuel-prices/fuel.json",
        "moto": "https://moto-way.com/fuel-price/fuel_prices.json",
        "motorfuelgroup": "https://fuel.motorfuelgroup.com/fuel_prices_data.json",
        "rontec": "https://www.rontec-servicestations.co.uk/fuel-prices/data/fuel_prices_data.json",
        "sainsburys": "https://api.sainsburys.co.uk/v1/exports/latest/fuel_prices_data.json",
        "sgn": "https://www.sgnretail.uk/files/data/SGN_daily_fuel_prices.json",
        "shell": "https://www.shell.co.uk/fuel-prices-data.html",
        "tesco": "https://www.tesco.com/fuel_prices/fuel_prices_data.json",
    }

    async def fetch_all(self):
        results = []
        for provider, url in self.PROVIDERS.items():
            try:
                r = requests.get(url)
                r.raise_for_status()
                data = r.json()
                normalize_func = getattr(self, f"normalize_{provider}", self.default_normalize)
                normalized = normalize_func(data)
                results.extend(normalized)
            except Exception as e:
                print(f"Error fetching {provider}: {e}")
        return results

    def default_normalize(self, data):
        # Fallback if no specific normalization is implemented
        return []

    # Normalization for Asda data
    def normalize_asda(self, data):
        stations = data.get("stations", [])
        result = []
        for s in stations:
            result.append({
                "site_id": s.get("site_id"),
                "brand": "Asda",
                "address": s.get("address"),
                "postcode": s.get("postcode"),
                "location": {
                    "longitude": s.get("longitude"),
                    "latitude": s.get("latitude"),
                },
                "prices": {
                    "E10": s.get("unleadedPrice"),
                    "E5": s.get("superUnleadedPrice"),
                    "B7": s.get("dieselPrice"),
                },
            })
        return result

    # Add similar normalization methods for other providers...

# Example usage:
# aggregator = FuelPriceAggregator()
# all_prices = aggregator.fetch_all()
# print(all_prices)