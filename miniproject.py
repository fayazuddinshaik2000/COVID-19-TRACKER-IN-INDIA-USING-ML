import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
while True:
     print(" ")
     print("COVID TRACKER :\n ""1) view all data: \n"  
                     " 2)view few data: \n" 
                     " 3) Get info: \n" 
                     " 4) get column details: \n " 
                     "5) List of States affected: \n"
                     " 6)List of confirmed cases in every State:\n "
                    "7)List of Total no of confirmed , Cured , Death cases in India:\n"
                    " 8)Top n  States in Death rates\n"
                    " 9)List of States with Total data\n"
                    " 10)List of Particular state\n"
                    " 11)Visualize The Covid rate in India")
     print()
     i=int(input("enter number:"))
     data = pd.read_csv("covid19.csv")
     if i==1:
         print(data)
     if i==2:
        a=int(input("enter number of rows you need to see:"))
        print(data.head(a))
     if i==3:
        print(data.info())
     if i==4:
         a=input("enter column name:")
         i=list(data.columns)
         if (a in i ):
             print(data[a])
         else:
             print("Not found")

     if  i==5:
         country=data["State"].unique()
         for i in country:
             print(i)
         print("Total countries effected are:",len(country))
     if  i==6:
         cases=pd.DataFrame(data.groupby('State')['Confirmed'].sum())
         print(cases)
     if  i==7:
         print()
         print("Confirmed Cases:",data["Confirmed"].sum())
         print("Cured Cases:", data["Cured"].sum())
         print("Death Cases:", data["Deaths"].sum())
     if  i==8:
          n=int(input("Enter number of states would u like to see:"))
          a=pd.DataFrame(data.groupby('State')['Deaths'].sum().sort_values(ascending=False)[:n])
          print(a)
     if  i==9:
         b=pd.DataFrame(data.groupby('State').sum())
         print (b)
     if  i==10:
         States=input("Enter State name:")
         d=States.capitalize()
         print(d)
         c=pd.DataFrame(data[data['State']==d])
         print(c)
     if  i==11:
          plt.plot(data.groupby('State').sum()['Confirmed'].index,data.groupby('State').sum()['Confirmed'],color='g',marker='o',label="COVID 19")
          plt.xticks(rotation=65)
          plt.title("VISUALIZATION OF COVID RATE IN DIFFERENT STATES OF INDIA",color='red')
          plt.xlabel('State')
          plt.tick_params(axis='x', which='major', labelsize=4.2)
          plt.legend(title='GRADE')
          plt.ylabel('Confirmed')
          plt.show()
