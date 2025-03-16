# Tunisia Real Estate Scraper
A web scraping solution to collect real estate listings from Tunisie Annonce and expose them via a REST API.

## Installation
1. Clone the repository: `git clone <repo-url>`
2. Set up a virtual environment: `python -m venv venv`
3. Activate it: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`

## Usage
- Run the scraper: `cd real_estate_scraper && scrapy crawl tunisie_annonce`
- Start the API: `uvicorn main:app --reload`
- Access endpoints:
  - `GET /annonces`: Retrieve all listings.
  - `POST /scrape`: Trigger a new scrape.

## Dependencies
See `requirements.txt` for the full list.
