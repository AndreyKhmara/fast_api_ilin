from fastapi import HTTPException

from app.database import SessionLocal
from app.schemas import CreateWalletRequest
from app.repository import wallets as wallet_repository


def get_balance(wallet_name: str | None = None):
    db = SessionLocal()
    try:
        if wallet_name is None:
            wallets = wallet_repository.get_all_wallet(db)

            return {"total balance:", sum([w.balance for w in wallets])}

        if not wallet_repository.is_wallet_exist(db, wallet_name):
            raise HTTPException(status_code=404, detail=f"Balance {wallet_name} not found")

        wallet = wallet_repository.get_wallet_balance_by_name(db, wallet_name)
        return {"wallet:": wallet_name, "balance:": wallet.balance}
    finally:
        db.close()


def create_wallet(wallet: CreateWalletRequest):
    db = SessionLocal()
    try:
        if wallet_repository.is_wallet_exist(db, wallet.name):
            raise HTTPException(status_code=404, detail=f"Wallet {wallet.name} already exists")

        wallet = wallet_repository.create_wallet(db, wallet.name, wallet.initial_balance)
        db.commit()
        return {"message": f"wallet {wallet.name} created", "wallet": wallet.name, "balance": wallet.balance}
    finally:
        db.close()
