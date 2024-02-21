from fastapi import FastAPI, HTTPException
from typing import Optional
from pydantic import BaseModel
from database import engine, SessionLocal
from models import Currency
from datetime import datetime
import httpx

app = FastAPI()

async def update_exchange_rates():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://openexchangerates.org/api/latest.json?app_id=8c1573bcf1d042f59a4e05178205ce4f")
        data = response.json()
        
    db = SessionLocal()
    for code, rate in data['rates'].items():
        currency = db.query(Currency).filter(Currency.code == code).first()
        if currency:
            currency.rate = rate
            currency.updated_at = str(datetime.utcnow())
        else:
            db.add(Currency(code=code, rate=rate))
    db.commit()
    db.close()

@app.get("/update_rates")
async def update_rates():
    await update_exchange_rates()
    return {"message": "Exchange rates updated successfully."}

@app.get("/last_update")
async def last_update():
    db = SessionLocal()
    latest_currency = db.query(Currency).order_by(Currency.updated_at.desc()).first()
    db.close()
    if latest_currency:
        return {"last_update": latest_currency.updated_at}
    else:
        raise HTTPException(status_code=404, detail="No data available.")

class ConversionRequest(BaseModel):
    source_currency: str
    target_currency: str
    amount: float

@app.post("/convert")
async def convert(request: ConversionRequest):
    db = SessionLocal()
    source = db.query(Currency).filter(Currency.code == request.source_currency).first()
    target = db.query(Currency).filter(Currency.code == request.target_currency).first()
    db.close()

    if not source or not target:
        raise HTTPException(status_code=400, detail="Invalid currency code.")

    result = (request.amount / source.rate) * target.rate
    return {"result": result}