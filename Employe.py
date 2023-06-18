class Man_Employee:
    suku = "Jawa"
    empCount = 0
    
    def __init__(self, name, age, agama, jkel, alamat, status, salary):
        self.name = name
        self.age = age
        self.agama = agama
        self.jkel = jkel
        self.alamat = alamat
        self.status = status
        self.salary = salary
        Man_Employee.empCount += 1
        
    def displayCount(self):
        print("Total Employee %d" % Man_Employee.empCount)
        
    def displayEmployee(self):
        print("Name : ", self.name, ", Salary : ", self.salary)
        
    def biodata(self):
        # return f"{self.name} is {self.age} years old"
        return f"Nama : {self.name} \nUsia : {self.age} \nAgama : {self.agama} \nJenis Kelamin : {self.jkel} \nAlamat : {self.alamat} \nStatus : {self.status}"
    
tes_qois = Man_Employee("Anto", 12, "Agama", "Laki-Laki", "Semarang", "Jomblo", 1000000)
print(tes_qois.biodata())
print("Suku : ", tes_qois.suku)

tes_qois.displayEmployee()
tes_qois.displayEmployee()
print("Total Employee %d" % Man_Employee.empCount)