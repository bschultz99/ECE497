import random

def heart_rate():
    # Generate random value for heart rate
    heart_rate = random.randint(60, 100)

    print("Heart Rate: {} bpm".format(heart_rate))

    # Return the heart rate value
    return {
        "heart_rate": heart_rate
    }

def temperature():
    # Generate random value for temperature
    temperature = round(random.uniform(36.0, 37.5), 1)

    print("Temperature: {} C".format(temperature))

    # Return the temperature 
    return {
        "temperature": temperature
    }

def glucose_level():
    # Generate random value for glucose level
    glucose_level = round(random.uniform(4.0, 6.0), 2)

    print("Glucose Level: {} mmol/L".format(glucose_level))

    # Return the glucose level
    return {
        "glucose_level": glucose_level
    }

heart_rate()
temperature()
glucose_level()