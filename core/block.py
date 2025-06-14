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
            json_represensation = serialization_utils.to_json(block_content)
            hash_final = serialization_utils.to_sha256(json_represensation)

            return hash_final