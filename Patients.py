class Patient:
    # class variable 
    consultation_fee = 500
    def __init__(self, pid, name, days_of_admitted):
        self.pid = pid
        self.name = name
        self.days_of_admitted = days_of_admitted
        self.admitted = False
    # object method of admit patient
    def admit_patient(self):
        if self.admitted:
            print("Patient is already admitted")
        else:
            self.admitted = True
            print("Patient admitted successfully")
    # object method of discharge patient
    def discharge_patient(self):
        if not self.admitted:
            print("Patient is not admitted")
        else:
            self.admitted = False
            print("Patient discharged successfully")
    # object method of calculate bill
    def calculate_bill(self):
        if not self.admitted:
            print("Patient is not admitted. Bill cannot be generated")
            return
        room_charge_per_day = 1000
        total_bill = (self.days_of_admitted * room_charge_per_day) + Patient.consultation_fee
        print("Total bill amount :", total_bill)
    # class method to update consultation fee
    @classmethod
    def update_consultation_fee(cls, new_fee):
        cls.consultation_fee = new_fee
p1 = Patient(1, "Varsha", 3)
p1.admit_patient()
p1.calculate_bill()
print("\nUpdating consultation fee")
Patient.update_consultation_fee(700)
p1.calculate_bill()
p1.discharge_patient()