import communication
import Sensors

def main():
    heart_rate = Sensors.heart_rate()
    temperature = Sensors.temperature()
    glucose = Sensors.glucose_level()
    patient, txid = communication.createPatient('Bob', '04/21/00', 'ABC123', 23, 195, 72, 'Male', 'Cancer', heart_rate, temperature, glucose)
    print(patient)
    print(txid)
    print(communication.retrievePatient(txid))
if __name__ == "__main__":
    main()