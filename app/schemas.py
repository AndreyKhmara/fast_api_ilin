from decimal import Decimal

from pydantic import BaseModel, Field, field_validator


class OperationRequest(BaseModel):
    wallet_name: str = Field(..., max_length=127)
    amount: Decimal
    destination: str | None = Field(None, max_length=255)

    @field_validator("amount")
    def amount_mast_be_positive(cls, v: float) -> float:
        if v <= 0:
            raise ValueError(
                "Amount must be positive."
            )
        return v

    @field_validator("wallet_name")
    def name_not_empty(cls, v: str) -> str:
        v = v.strip()
        if not v:
            raise ValueError("Wallet name cannot be empty.")
        return v


class CreateWalletRequest(BaseModel):
    name: str = Field(..., max_length=127)
    initial_balance: float = 0

    @field_validator("initial_balance")
    def balance_most_be_negative(cls, v: float) -> float:
        if v < 0:
            raise ValueError(
                "initial_balance can not be negative."
            )
        return v

    @field_validator("name")
    def name_not_empty(cls, v: str) -> str:
        v = v.strip()
        if not v:
            raise ValueError("name cannot be empty.")
        return v
