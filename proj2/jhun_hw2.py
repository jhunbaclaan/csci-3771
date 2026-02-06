# @jhunbaclaan
# d.o.c (date of creation): 02/01/2026
# objective -- create a program that has class 'Professors' that contains the attributes:
# name, course_id, description, location
# Professors will have a method named showResults that displays up to five records

class Professors:
    name = ""
    course_id = ""
    description = ""
    location = ""
    def __init__(self, name, course_id, description, location):
        self.name = name
        self.course_id = course_id
        self.description = description
        self.location = location
    def showResults(self):
        print(self.name, "\t", self.course_id, "\t", self.description, "\t", self.location)
        
print("Professor Name\tCourse ID\tDescription\tLocation")
prof1 = Professors("Mary Smith", "CSCI-4911", "Software Project", "PL13")
prof2 = Professors("Curt Powley", "CSCI-4711", "Audio Processing in Python", "PL15")
prof3 = Professors("Azhar Ishaque", "CSCI-3771", "Python", "Hickam AFB")
prof4 = Professors("Yi Zhu     ", "CSCI-3601", "Operating Systems", "PL15") # added whitespace for alignment...
prof5 = Professors("Edward Pier", "CSCI-3731", "Programming in C++", "PL15")
prof1.showResults()
prof2.showResults()
prof3.showResults()
prof4.showResults()
prof5.showResults()