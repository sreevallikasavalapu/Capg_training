class father:
    f_age=40
    def men(self):
        return "father is a men"
    def f_occupation(self):
        return "father is doctor"
class mother:
    m_age=35
    def women(self):
        return "mother is women"
    def m_occupation(self):
        return "mother is teacher"
class child(father,mother):
    # pass    #used to combine both parents
    def display(self):
        return "child class"
    def print_age(self,f_age,m_age):
        print(f"age of father and mother are {f_age} and {m_age}")
c=child()
print(c.men())
print(c.women())
c.print_age(c.f_age,c.m_age)
print(c.f_occupation())
print(c.m_occupation())
f=father()
f=c
print(f.display())