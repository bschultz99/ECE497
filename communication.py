from planetmint_driver import Planetmint
from planetmint_driver.crypto import generate_keypair
from ipld import marshal, multihash
import time
plntmnt = Planetmint('https://test.ipdb.io')
alice = generate_keypair()
tx = plntmnt.transactions.prepare(
    operation='CREATE',
    signers=alice.public_key,
    assets=[
        {'data': 
            multihash(marshal({'message': 'Blockchain all the things!'}))
            }   
    ]
)
signed_tx = plntmnt.transactions.fulfill(tx, private_keys=alice.private_key)
print(plntmnt.transactions.send_commit(signed_tx))
tid = signed_tx['id']
block_height = plntmnt.blocks.get(txid='92c731f299136039f880395918e1194a2971c72d732fa0aaa71013c2f44fb4c4') #signed_tx['id'])
time.sleep(15)
print(block_height)


def 