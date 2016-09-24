import csv

#def collide(hour, hours):
    #for hour in hours:


#def makeSchedules(subjects):
    #amount = len(subjects)-1
    #for subject in subjects:
        #for hour in subject.hours[2:]
def assignToDict(dummy):
    if dummy=="":
        return ""
    if dummy.split("/")[1]=="":
        return "all"
    elif dummy.split("/")[1]=="P":
        return "even"
    else:
        return "odd"
class Subject:
    def __init__(self, name, number, type):
        self.name = name
        self.number = number
        self.type = type
        self.dummyData = []
        self.info = str(number) + " " + name + " " + type
        self.even = {"mon":"",
                "tue":"",
                "wed":"",
                "thu":"",
                "fri":"",
        }
        self.odd = {"mon":"",
                "tue":"",
                "wed":"",
                "thu":"",
                "fri":"",
        }
        self.all = {"mon":"",
                "tue":"",
                "wed":"",
                "thu":"",
                "fri":"",
        }
    def assignHours(self):
        days = ("mon", "tue", "wed", "thu", "fri")
        index = 0
        while index<len(self.dummyData):
            for data in self.dummyData[index].split(" "):
                if assignToDict(data)=="all":
                    self.all[days[index]]+=data.split("/")[0]
                    print(self.all)
                elif assignToDict(data)=="even":
                    self.even[days[index]]+=data.split("/")[0]
                elif assignToDict(data)=="odd":
                    self.odd[days[index]]+=data.split("/")[0]
                elif assignToDict(data)=="":
                    pass
            index+=1


def assignDummyData(listOfSubjects, listOfHours):
    for subject in listOfSubjects:
        for data in listOfHours:
            if subject.number==int(data[0]) and subject.type==data[1].lower():
                subject.dummyData=data[2:7]


def main():
    #Printowanie informacji o przedmiotach w semestrze
    names = []
    types = []
    subjects = []
    file = open("dummy.txt", "r")
    print("\n")
    count = 1
    for line in file:
        if line.strip():
            #print("%d. PRZEDMIOT: %50s\tGRUPY: %3s" % (count, line.split("/")[0], line.split("/")[1]))
            names.append(line.split("/")[0])
            types.append(line.split("/")[1][:-1])
            count+=1
    file.close()
    del count
    exampleFile = open("XDD.csv")
    exampleReader = csv.reader(exampleFile,delimiter=';')
    exampleData = list(exampleReader)
    exampleData.pop(0)
    index = 0
    for name in names:
        for i in range(len(types[index])):
            subjects.append(Subject(name, index+1, types[index][i]))
        index+=1
    assignDummyData(subjects, exampleData)
    for subject in subjects:
        subject.assignHours()
        print(subject.info)

if __name__=="__main__":
    main()
