from pydantic import BaseModel

class ResponseKCmod(BaseModel):
    amount_kc: str
    try_price: str
    bgn_price: str
    ingame_cash: str

    @classmethod
    def from_query_result(cls, amount_kc, 
                          try_price, 
                          bgn_price, ingame_cash):
        return cls(amount_kc=f'{amount_kc} KC',
                try_price=f'{try_price} TRY',
                   bgn_price=f'{bgn_price} BGN',
                   ingame_cash=f'{ingame_cash} GB')
