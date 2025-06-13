import time
class Transaction:
    def __init__(self, sender : str, recipient : str, amount : float):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.timestamp = time.time()