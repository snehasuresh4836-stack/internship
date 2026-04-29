import pandas as pd

data = [
["Chennai","T Nagar","North","ON",60,40,45,20,5],
["Chennai","T Nagar","South","ON",55,45,50,18,6],
["Chennai","Guindy","East","ON",70,30,60,15,8],
["Chennai","Guindy","West","OFF",0,0,30,25,2],
["Bangalore","Silk Board","North","ON",90,30,80,12,10],
["Bangalore","Silk Board","South","ON",85,35,75,14,9],
["Bangalore","Whitefield","East","ON",60,40,55,20,6],
["Bangalore","Whitefield","West","OFF",0,0,35,30,3],
["Mumbai","Andheri","North","ON",80,40,70,16,9],
["Mumbai","Andheri","South","ON",75,45,65,18,7],
["Mumbai","Bandra","East","ON",65,35,60,17,7],
["Mumbai","Bandra","West","OFF",0,0,40,28,3],
["Delhi","Connaught Place","North","ON",85,35,75,14,9],
["Delhi","Connaught Place","South","ON",80,40,70,15,8],
["Delhi","Karol Bagh","East","OFF",0,0,50,26,4],
]

columns = ["City","Junction","Direction","Signal_Status","Red_Time","Green_Time","Vehicles","Avg_Speed","Delay"]

df = pd.DataFrame(data, columns=columns)

print(df)