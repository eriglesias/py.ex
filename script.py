from blockchain import Blockchain

block_one_transactions = {"sender":"José López de Santamaría", "receiver": "Jesus Antonio de Zeballos", "amount":"50"}
block_two_transactions = {"sender": "Dolores Perpetuos", "receiver":"Piedad Absoluta", "amount":"25"}
block_three_transactions = {"sender":"José López de Santamaría", "receiver":"Piedad Absoluta", "amount":"35"}
fake_transactions = {"sender": "Dolores Perpetuos", "receiver":"Piedad Absoluta, José López de Santamaría", "amount":"25"}

local_blockchain = Blockchain()
local_blockchain.print_blocks()

local_blockchain.add_block(block_one_transactions)
local_blockchain.add_block(block_two_transactions)
local_blockchain.add_block(block_three_transactions)
local_blockchain.print_blocks()
local_blockchain.chain[2].transactions = fake_transactions
local_blockchain.validate_chain()
