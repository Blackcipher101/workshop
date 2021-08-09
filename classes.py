
class student:

    def __init__(self,name,total_marks,number_of_subject):
        self.name=name
        self.total_marks=total_marks
        self.number_of_subject=number_of_subject

    def calc_percentage(self):
        percentage=(self.total_marks/self.number_of_subject)
        return percentage

Ram= student("ram",900,10)
print(Ram.name)
print(Ram.calc_percentage())
