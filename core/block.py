import time

from core.serialization_utils import to_json, to_sha256


class Block:
    def __init__(self, index : int, transactions : list, previous_hash : str, nonce : int):

        self.index = index
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.timestamp = time.time()
        self.nonce = nonce


        def calculate_hash(self):
            block_content = {
                'index': self.index,
                'timestamp': self.timestamp,
                'previous_hash': self.previous_hash,
                'nonce': self.nonce,
                'transactions': self.transactions
                }
            json_represensation = to_json(block_content)
            hash_final = to_sha256(json_represensation)

            return hash_final

if __name__ == "__main__":
    # Example usage
    block = Block(1, [], "0", 0)
    print(block.calculate_hash())
    # Output: <hash_value>
    # Note: The output will be a hash value based on the block's content.