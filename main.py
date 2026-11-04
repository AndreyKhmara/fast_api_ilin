from fastapi import FastAPI, HTTPException
from fastapi.responses import Response

app = FastAPI()

BALANCE = {}


@app.get("/balance")
def get_balance(wallet_name: str | None = None):
    if wallet_name is None:
        print('case0')
        return {"total balance:", sum(BALANCE.values())}

    if wallet_name not in BALANCE:
        print('case1')
        raise HTTPException(status_code=404, detail=f"Balance {wallet_name} not found")
    print('case2')
    return {"wallet:": wallet_name, "balance:": BALANCE[wallet_name]}


@app.post("/wallets/{name}")
def receive_Money(name: str, amount: int):
    if name not in BALANCE:
        BALANCE[name] = 0

    BALANCE[name] += amount

    return {
        "message": f"add {amount} to {name}for ",
        "wallet:": name,
        "new balance:": BALANCE[name]
    }
