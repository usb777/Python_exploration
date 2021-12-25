class Home:
    def __init__(self, first_name,last_name, age, race, job):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.race= race
        self.job = job

    def getProps(self):
        print("age"+str(self.age))
        print("race"+self.race)

    def setAge(self,age):
        self.age = age

    def getAge(self):
        return self.age

    
    def setJob(self,job):
        self.job = job

    def getJob(self):
        return self.job
    



    

      
