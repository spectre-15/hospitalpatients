import random, string

patient_stopcheckin = False
patient_list = []
while patient_stopcheckin == False:
    # enter patient's information (name, age, status of new or not)
    patient_name = input("Enter patient name: ")
    patient_age = int(input("Enter patient age: "))
    # checks if patient is new or not
    new_patient = input(f"Is {patient_name} a new patient? ")
    new_patient = new_patient.casefold()
    if new_patient == "yes" or new_patient == "y" or new_patient == "t" or new_patient == "true":
        new_patient = True
    elif new_patient == "no" or new_patient == "n" or new_patient == "f" or new_patient == "false":
        new_patient = False
    # adds patient information to a list
    patient_tuple = patient_name, patient_age, new_patient
    patient_list.append(patient_tuple)
    # requests if you want to check in a new patient
    patient_stopcheckin = input("Do you want to check in a new patient? ")
    patient_stopcheckin = patient_stopcheckin.casefold()
    if patient_stopcheckin == "yes" or patient_stopcheckin == "y":
        patient_stopcheckin = False
    elif patient_stopcheckin == "no" or patient_stopcheckin == "n":
        patient_stopcheckin = True

# patient list
for patient in patient_list:
    g = 1
    (pat, age, new) = patient
    while g <= len(patient_list):
        pplreq = input(f"Print {pat}'s information? ")
        pplreq = pplreq.casefold()
        if pplreq == "yes" or pplreq == "y":
            if new:
                print(f"{pat} is {age} and is a new patient.")
                g += 1
            if not new:
                print(f"{pat} is {age} and is not a new patient.")
                g += 1
        elif pplreq == "no" or pplreq == "n":
            g += 1
        else:
            g += 1
