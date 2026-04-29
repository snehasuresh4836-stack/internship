class calculation:
    n1=int(input('enter first number')) 
    n2=int(input('enter second number'))
    def data(self,a,b):
        self.n1=a
        self.n2=b
    def add_data(self):
        print('sum=',self.n1+self.n2)
    def subtract_data(self):
        print('difference=',self.n1-self.n2)
    def mul_data(self):
        print('multiply=',self.n1*self.n2)
    def devide_data(self):
        print('division=',self.n1/self.n2)    
st=calculation()
st.add_data()
st.subtract_data()
st.mul_data()
st.devide_data()



