from planetmint_driver import Planetmint
from planetmint_driver.crypto import generate_keypair
from ipld import marshal, multihash
import time
plntmnt = Planetmint('https://test.ipdb.io')
#plntmnt = Planetmint('http://localhost:9984')
def createPatient(name, dob, id, age=None, weight=None, height=None, gender=None, conditions=None): 
    fixed_data = [{
        'data': multihash(marshal({
            'patient': {
                'name': name,
                'dob': dob,
                'id': id,
               },
           }))
       }]

    meta_data = multihash(marshal({
        'data': {
            'patient': {
                'age': age,
                'weight': weight,
                'height': height,
                'gender': gender,
                'conditions': conditions,
            },
        }
    }))
    patient = generate_keypair()
    tx = plntmnt.transactions.prepare(
        operation = 'CREATE',
        signers = patient.public_key,
        assets = fixed_data,
        metadata = meta_data
    )
    signed_tx = plntmnt.transactions.fulfill(tx, private_keys=patient.private_key)
    print(plntmnt.transactions.send_commit(signed_tx))
    txid = signed_tx['id']
    return patient, txid

def updatePatient(patient, txid, age=None, weight=None, height=None, gender=None, conditions=None):
    meta_data = {
        'data': {
            'patient': {
                'age': age,
                'weight': weight,
                'height': height,
                'gender': gender,
                'conditions': conditions,
            },
        },
    }
    tx = plntmnt.transactions.prepare(
        operation = 'UPDATE',
        signers = patient.public_key,
        asset = txid,
        metadata = meta_data,
    )
    signed_tx = plntmnt.transactions.fulfill(tx, private_key=patient.private_key)
    plntmnt.transactions.send_commit(signed_tx)

print(createPatient('bob', '09/20/45', 'asd123', 56, 186, 156, "Male", "Cancer"))