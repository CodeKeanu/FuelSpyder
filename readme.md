# FuelSpyder

FuelSpyder is a FastAPI-based web service that provides real-time UK fuel price data from major fuel retailers via simple REST API endpoints.

## Features

- Fetches live fuel prices from multiple UK retailers
- Unified JSON API for easy integration
- Built with FastAPI for speed and reliability

## Supported Retailers

- Asda
- BP
- Esso
- Jet
- Morrisons
- Moto
- Motor Fuel Group
- Rontec
- Sainsbury's
- SGN
- Shell
- Tesco

## Endpoints

Each retailer has its own endpoint under `/prices/{retailer}`.  
For example:

- `GET /prices/asda`
- `GET /prices/bp`
- `GET /prices/esso`
- `GET /prices/jet`
- `GET /prices/morrisons`
- `GET /prices/moto`
- `GET /prices/motorfuelgroup`
- `GET /prices/rontec`
- `GET /prices/sainsburys`
- `GET /prices/sgn`
- `GET /prices/shell`
- `GET /prices/tesco`

Each endpoint returns the latest JSON data as provided by the retailer.

## Quick Start

1. **Clone the repository:**
    ```bash
    git clone https://github.com/CodeKeanu/fuelspy.git
    cd fuelspy
    ```

2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the app:**
    ```bash
    fastapi dev main.py
    ```

4. **Access the API:**
    - Visit [http://localhost:8000](http://localhost:8000)
    - Interactive docs at [http://localhost:8000/docs](http://localhost:8000/docs)

## Example Usage

```bash
curl http://localhost:8000/prices/asda
```

## License

MIT License

---

**Note:** This project simply proxies public data from retailer APIs. Data accuracy and availability depend on the source sites.