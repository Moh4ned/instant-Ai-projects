class Hospital:
    def __init__(self , name , address):
        self.name=name
        self.address=address
        self.department=[]
    def add_department(self,department):
        self.department.append(department)
    def  remove_department(self,department):
        self.department.remove(department)
    def get_departments(self):
        return self.department
class Department:
    def __init__(self, name):
        self.name =name
        self.doctors= []
        self.patients=[]

    def add_doctor(self,doctor):
        self.doctors.append(doctor)

    def remove_doctor(self,doctor):
        self.doctors.remove(doctor)

    def get_doctors(self):
        return self.doctors

    def add_patient(self, patient):
        self.patients.append(patient)

    def remove_patient(self,patient):
        self.patients.remove(patient)

    def get_patients(self):
        return self.patients
class Doctor:
    def __init__(self, name, specialization):
        self.name  = name
        self.specialization  = specialization
        self.patients  = []

    def add_patient(self, patient):
        self.patients.append(patient)

    def remove_patient(self, patient):
        self.patients.remove(patient)

    def get_patients(self):
        return self.patients
class Patient:
    def __init__(self, name ,age, doctor ):
        self.name= name
        self.age=age
        self.doctor= doctor
    def assign_doctor(self, doctor):
        self.doctor=doctor
    def  get_assigned_doctor(self):
        return self.doctor

hospital = Hospital("Hospital", "123address")
depart1 = Department(str(input("add department :")))
depart2 = Department(str(input("add department :")))
hospital.add_department(depart1)
hospital.add_department(depart2)
doctor1 = Doctor(str(input("add doctor  :") ),str(input("add  specialization :") ))
doctor2 = Doctor(str(input("add doctor  :") ),str(input("add  specialization :") ))
cardiology.add_doctor(doctor1)
pediatrics.add_doctor(doctor2)
patient1 = Patient("Patient1", 30 , doctor1.name)
patient2 = Patient("Patient2", 33,doctor2.name)
patient1.assign_doctor(doctor1)
patient2.assign_doctor(doctor2)
cardiology.add_patient(patient1)
pediatrics.add_patient(patient2)
departments = hospital.get_departments()
for department in departments:
    print("department:", department.name)
    doctors = department.get_doctors()
    for doctor in doctors:
        print("doctor:", doctor.name)
        patients = doctor.get_patients()
        for patient in patients:
            print("Patient:", patient.name, "Assigned Doctor:", patient.get_assigned_doctor().name)


