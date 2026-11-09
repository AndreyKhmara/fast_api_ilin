from fastapi import HTTPException

from app.schemas import OperationRequest, CreateWalletRequest

import app.repository.wallets as wallets_repository


def add_income(operation: OperationRequest):
    print('operation:', operation)
    if not wallets_repository.is_wallet_exist(operation.wallet_name):
        raise HTTPException(status_code=400, detail=f"Wallet {operation.wallet_name} not found")

    new_balance = wallets_repository.add_income(operation.wallet_name, operation.amount)
    return {
        "message": 'Income added successfully',
        "wallet": operation.wallet_name,
        "amount": operation.amount,
        "destination": operation.destination,
        "new_balance": new_balance
    }

# TODO остановился на 46:25; продолжить с блока подключение к бд
def add_expense(operation: OperationRequest):
    if not wallets_repository.is_wallet_exist(operation.wallet_name):
        raise HTTPException(status_code=400, detail=f"Wallet {operation.wallet_name} not found")

    balance = wallets_repository.get_wallet_balance_by_name(operation.wallet_name)

    if balance < operation.amount:
        raise HTTPException(status_code=400,
                            detail=f"Insufficient funds. Available balance: {balance}")

    new_balance = wallets_repository.add_expense(operation.wallet_name, operation.amount)

    return {
        "message": 'expense added successfully',
        "wallet": operation.wallet_name,
        "amount": operation.amount,
        "destination": operation.destination,
        "new_balance": new_balance
    }
