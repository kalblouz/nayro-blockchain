import time
class Transaction:
    def __init__(self, sender : str, recipient : str, amount : float):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.timestamp = time.time()

    def to_dict(self):
        return {
            'sender': self.sender,
            'recipient': self.recipient,
            'amount': self.amount,
            'timestamp': self.timestamp
        }

if __name__ == "__main__":
    # Example usage
    transaction = Transaction("Alice", "Bob", 50.0)
    print(transaction.to_dict())
    # Output: {'sender': 'Alice', 'recipient': 'Bob', 'amount': 50.0, 'timestamp': <current_time>}