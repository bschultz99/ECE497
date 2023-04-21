import communication
import Sensors
from ipld import marshal, multihash

def main():
    heart_rate = Sensors.heart_rate()
    temperature = Sensors.temperature()
    glucose = Sensors.glucose_level()
    patient, txid = communication.createPatient('Bob', '04/21/00', 'ABC123', 23, 195, 72, 'Male', 'Cancer', heart_rate, temperature, glucose)
    retrieved = communication.retrievePatient(txid)
    print("Patient Keys: {}".format(patient))
    print("Patient Public Key From chain: {}".format(retrieved['outputs'][0]['public_keys']))
    print("Hashed data from chain: {}".format(retrieved['assets'][0]['data']))
    fixed_data = [{
        'data': multihash(marshal({
            'patient': {
                'name': 'Bob',
                'dob': '04/21/00',
                'id': 'ABC123',
               },
           }))
       }]
    print("Original hashed data: {}".format(fixed_data[0]['data']))
    print("Hashed metadata from chain: {}".format(retrieved['metadata']))
    meta_data = multihash(marshal({
        'data': {
            'patient': {
                'age': 23,
                'weight': 195,
                'height': 72,
                'gender': 'Male',
                'conditions': 'Cancer',
                'heartrate': heart_rate,
                'temperature': temperature,
                'glucose': glucose,
            },
        }
    }))
    print("Original hashed meta_data: {}".format(meta_data))
if __name__ == "__main__":
    main()