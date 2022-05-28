class Student:
     school = "Akirachix"
     def __init__(self,country,Firstname,Secondname,age):
        self.Firstname = Firstname
        self.country = country
        self.Secondname = Secondname
        self.age = age
     def full_name (self):

         return f"Hey {self.Firstname} {self.Secondname} How is {self.country}"
     def year_of_birth (self):  
         year=2022 - self.age
         return f"Hey {self.Firstname} {self.Secondname} How is {self.country} you are {year}"
     def initials (self):
         return f"Hey {self.Firstname} {self.Secondname} How is {self.country} your initials {self.Firstname[0]} {self.Secondname[0]}"
     
