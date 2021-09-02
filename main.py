import hashlib

class cyberchain:

    def __init__(self,previous_block_hash, transaction_list):
        self.prevous_block_hash = previous_block_hash
        self.transaction_list = transaction_list

        self.block_data = "-".join(transaction_list) + "-" + previous_block_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()

t1 = "some transaction 1"
t2 = "some transaction 2"
t3 = "some transaction 3"
t4 = "some transaction 4"
t5 = "some transaction 5"
t6 = "some transaction 6"

initial_block = cyberchain("",[t1,t2])
print(initial_block.block_data)
print(initial_block.block_hash)

second_block = cyberchain("",[t3,t4])
print(second_block.block_data)
print(second_block.block_hash)

third_block = cyberchain("",[t5,t6])
print(third_block.block_data)
print(third_block.block_hash)
