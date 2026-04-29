#constructor
class student:
    name='sam'
    age=21
    def __init__(self,n1,a1):
        self.name=n1
        self.age=a1
    def set_data(self,n,a):
        self.name=n
        self.age=a
    def display_data(self):
        print(self.name)
        print(self.age)
    def __del__(delf):
        print('this is distructor')
st=student('sneha',21)
st.display_data()