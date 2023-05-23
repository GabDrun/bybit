from pybit.unified_trading import HTTP
import json


config = json.load(open('config.json', 'r'))


class Base():
    session = None

    def reset_session(self):
        self.session = HTTP(testnet=True,
                            api_key=config['api_key'],
                            api_secret=config['api_secret'],)
        return self
    
    def __iter__(self):
        return iter(self.list)
    
    def __len__(self):
        return len(self.list)
    
    def __getitem__(self, key):
        return self.list[key]
    
    def __add__(self, other):
        if isinstance(other, self.__class__):
            self.list.update(other.list)
            return self
        else:
            raise TypeError(f"unsupported for: '{self.__class__}' and '{type(other)}'")