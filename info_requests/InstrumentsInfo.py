from .base import Base


class InstrumentInfo:
    """Class to save single instrument info"""
    def __init__(self, data):
        list_data = data['list'][0]
        lotSizeFilter_data = list_data['lotSizeFilter']
        priceFilter_data = list_data['priceFilter']

        self.category = data['category']
        
        self.symbol = list_data['symbol']
        self.baseCoin = list_data['baseCoin']
        self.quoteCoin = list_data['quoteCoin']
        self.innovation = list_data['innovation']
        self.status = list_data['status']
        
        self.basePrecision=lotSizeFilter_data['basePrecision']
        self.quotePrecision=lotSizeFilter_data['quotePrecision']
        self.minOrderQty=lotSizeFilter_data['minOrderQty']
        self.maxOrderQty=lotSizeFilter_data['maxOrderQty']
        self.minOrderAmt=lotSizeFilter_data['minOrderAmt']
        self.maxOrderAmt=lotSizeFilter_data['maxOrderAmt']

        self.tickSize=priceFilter_data['tickSize']
    
    def __str__(self):
        return f"category: {self.category}\n" + \
            f"symbol: {self.symbol}\n" + \
            f"baseCoin: {self.baseCoin}\n" + \
            f"quoteCoin: {self.quoteCoin}\n" + \
            f"innovation: {self.innovation}\n" + \
            f"status: {self.status}\n" + \
            f"basePrecision: {self.basePrecision}\n" + \
            f"quotePrecision: {self.quotePrecision}\n" + \
            f"minOrderQty: {self.minOrderQty}\n" + \
            f"maxOrderQty: {self.maxOrderQty}\n" + \
            f"minOrderAmt: {self.minOrderAmt}\n" + \
            f"maxOrderAmt: {self.maxOrderAmt}\n" + \
            f"tickSize: {self.tickSize}\n"


class InstrumentsInfo(Base):
    """Class to save all instruments info"""

    def __init__(self):
        self.reset_session()
        self.list = {}
        
    
    def add_instrument(self, category, symbol):
        responce = self.session.get_instruments_info(category=category, symbol=symbol)
        if responce is not None and responce['retCode'] == 0:
            self.list[f'{category}:{symbol}'] = InstrumentInfo(responce['result'])
            return True
        return False
    
    def add_instruments(self, category, symbols):
        for symbol in symbols:
            if not self.add_instrument(category, symbol):
                return False
        return True
    
    