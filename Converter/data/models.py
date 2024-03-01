from pydantic import BaseModel

class ResponseKCmod(BaseModel):
    amount: int
    try_price: float
    bgn_price: float
    ingame_cash: float

    @classmethod
    def from_query_result(cls, amount, 
                          try_price, 
                          bgn_price, ingame_cash):
        return cls(amount=amount,
                   try_price=try_price,
                   bgn_price=bgn_price,
                   ingame_cash=ingame_cash)
