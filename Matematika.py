class Matematika:
    def __init__(self, nilai1,nilai2,nilai3,nilai4) -> None:
        self.nilai1 = nilai1
        self.nilai2 = nilai2
        self.nilai3 = nilai3
        self.nilai4 = nilai4
        
        hasil = 0
        
    def penjumlahan(nilai1,nilai2):
        hasil = nilai1 + nilai2
        print (hasil)
        return hasil
    
    def perkalian(nilai1, nilai2, nilai3):
        hasil = nilai1*nilai2*nilai3
        print(hasil)
        return hasil
    
    def pengurangan(nilai1,nilai2,nilai3,nilai4):
        hasil = nilai1-nilai2-nilai3-nilai4
        print(hasil)
        return hasil
    
    def perpangkatan(nilai1,nilai2):
        hasil = nilai1**nilai2
        print(hasil)
        return hasil
    
    penjumlahan(2,2)
    pengurangan(10,10,10,10)
    perkalian(20,10,6)
    perpangkatan(5,2)