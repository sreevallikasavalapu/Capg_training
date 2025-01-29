class management:
    def __init__(self,name,rno):
        self.name=name
        self.rno=rno
class school(management):
    def __init__(self, name, rno):
        super().__init__(name, rno)
    def show_details(self,name,rno):
        print(f"{self.name} of {self.rno} is school student")
class ug_student(management):
    def __init__(self, name, rno):
        super().__init__(name, rno)
    def show_details(self,name,rno):
        print(f"{name} of {rno} is undergraduate student")
class pg_student(management):
    def __init__(self, name, rno):
        super().__init__(name, rno)
    def show_details(self,name,rno):
        print(f"{name} of {rno} is pg student")
m=management("vallika",101)
s=int(input("select option 1.school 2.undergraduate 3.postgraduate"))
if(s==1):
    # sh=school("vallika",101)
    # sh.show_details()
    print(m.name)
elif (s==2):
    ug=ug_student("vallika",101)
    ug.show_details()
else:
    pg=pg_student("vallika",101)
    pg.show_details()    