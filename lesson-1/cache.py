class LRUCache:
    def __init__(self, capacity: int=10) -> None:
        self.const = 10
        self.dict = {} 

    def get(self, key: str) -> str:
        return self.dict.get(key,"")
        

    def set(self, key: str, value: str) -> None:
        if key in self.dict:
            del self.dict[list(self.dict)[0]]
            self.dict[key] = value
        elif len(self.dict) > self.const-1:
            del self.dict[list(self.dict)[0]]
            self.dict[key] = value
        else:
            self.dict[key] = value

    def rem(self, key: str) -> None:
        return self.set(key,"")
    
    def getall(self) -> None:
        return print(self.dict)