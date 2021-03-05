class student():
    def nama(self):
        print("nama    :", self.full_name)
        
    def get_age (self):
        print("umur    :", self.age)
    def get_gender (self):
        print("gender  :", self.gender)
    def get_alamat (self):
        print("alamat  :", self.alamat)
farah = student()

farah.full_name = "Farah Cantik"
farah.age = "19"
farah.gender = "perempuan"
farah.alamat = "bekasi"

farah.nama()
farah.get_age()
farah.get_gender()
farah.get_alamat()

