name=input("Enter Name")
email=input("Enter Email")
mobile=input("Enter Mobile")
data=name+' '+email+' '+mobole+'\n'

fp=open('data.txt','w')
fp.write('the new data')
fp.close()# to write data