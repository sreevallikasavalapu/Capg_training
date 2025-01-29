class management:
    def __init__(self,name,rno):
        self.name=name
        self.rno=rno
class school(management):
    def display(self,name,rno):
        print(name)
        print(rno)
        print("school student")
m=management("vallika",101)
s=int(input("select option 1.school 2.undergraduate 3.postgraduate"))
if(s==1):
    s=school()
    print(m.name)
    print(m.rno)
    print("school student")
"""
elif (s==2):
    ug=ug_student("vallika",101)
    ug.show_details()
else:
    pg=pg_student("vallika",101)
    pg.show_details()    
    """