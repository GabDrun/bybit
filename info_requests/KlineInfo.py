from .base import Base


class KlineInfo:
    """Class to save single kline data"""
    def __init__(self, data):
        self.symbol = data['symbol']
        self.category = data['category']
        self.list = data['list']

    def __str__(self):
        return f"symbol: {self.symbol}\n" + \
            f"category: {self.category}\n"
    

class KlinesInfo(Base):
    """Class to save all klines"""
    def __init__(self):
        self.reset_session()
        self.list = {}

    def _add_kline(self, response, category, symbol, interval):
        if response is not None and response['retCode'] == 0 and response['retMsg'] == 'OK':
            self.list[f'{category}:{symbol}:{interval}'] = KlineInfo(response['result'])
            return True
        return False
    
    def add_kline(self, category, symbol, interval, start, end):
        if None not in [start, end]:
            return self._add_kline(self.session.get_kline(category=category, symbol=symbol, interval=interval, start=start, end=end),
                                   category, symbol, interval)   
        else:
            return self._add_kline(self.session.get_kline(category=category, symbol=symbol, interval=interval),
                                   category, symbol, interval)  
        
    def add_klines(self, category, symbols, interval, start=None, end=None):
        for symbol in symbols:
            if not self.add_kline(category, symbol, interval, start, end):
                return False
        return True
