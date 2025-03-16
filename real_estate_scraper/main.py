from fastapi import FastAPI
import sqlite3
import subprocess

app = FastAPI()

@app.get("/annonces")
def get_annonces():
    conn = sqlite3.connect("annonces.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM annonces")
    rows = cursor.fetchall()
    conn.close()
    return [{"id": row[0], "title": row[1], "price": row[2], "property_type": row[3],
             "location": row[4], "area": row[5], "description": row[6], "contact": row[7],
             "publication_date": row[8], "url": row[9]} for row in rows]

@app.post("/scrape")
def scrape():
    subprocess.run(["scrapy", "crawl", "tunisie_annonce"], cwd="real_estate_scraper")
    subprocess.run(["python", "db_setup.py"])
    return {"message": "Scraping completed and data updated"}