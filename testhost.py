from planetmint_driver import Planetmint
from planetmint_driver.crypto import generate_keypair
from ipld import *
import time
#import multihash as mh
import pymultihash as mh #import decode, digest
import base58
from pymultihash.codecs import CodecReg
plntmnt = Planetmint('https://test.ipdb.io')
#plntmnt = Planetmint('http://localhost:9984')
alice = generate_keypair()

tx = plntmnt.transactions.prepare(
    operation='CREATE',
    signers=alice.public_key,
    assets=[
        {'data': 
           multihash(marshal({'message': 'Blockchain all the things!'}))
           }   
    ],
    metadata = multihash(marshal({'message': 'Blockchain all the things!'}) )
)
signed_tx = plntmnt.transactions.fulfill(tx, private_keys=alice.private_key)
plntmnt.transactions.send_commit(signed_tx)
tid = signed_tx['id']
block_height = plntmnt.transactions.retrieve(txid=tid)
print(block_height['assets'][0]['data'])
print(multihash(marshal({'message': 'Blockchain all the things!'})))