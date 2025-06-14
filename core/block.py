import time

class Block:
    def __init__(self, index : int, transactions : list, previous_hash : str):
        self.index = index
        self.transactions = transactions
        self.previous_hash = previous_hash

