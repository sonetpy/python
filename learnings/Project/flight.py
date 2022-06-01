'''
If user enters the keyword "reservation" as command then it should invoke the class Reservation.
1. enter the name
2. from and to
3. date in dd-mm-yyyy format
4. API should pull all the flight details from and to destination
5. user selects the flight details and save it in postgres db and it will give a unique id.
6. user can retrive the booking details just by entering the the unique id. eg. : $ reservation <booking id>
'''
import airlines
class Reservation:
    def __init__(self,pax_name,pax_age,pax_sex,from_dest,to_dest,date_time):
        self.pax_name=pax_name
        self.pax_age=pax_age
        self.pax_sex=pax_sex
        self.from_dest=from_dest
        self.to_dest=to_dest
        self.date_time=date_time

    def flight_api():
        
        

def passenger_details():
    print('Name: ', res.pax_name)
    print('Age: ', res.pax_age)
    print(res.from_dest,'-',res.to_dest)
    print(res.date_time)

def print_details():
    if (res.pax_sex == 'F') or (res.pax_sex == 'f'):
        print('Your Reservation Details Mrs/Miss.',res.pax_name)
        passenger_details()
    else:
        print('Your Reservation Details Mr.',res.pax_name)
        passenger_details()

if __name__=='__main__':
    print('\n')
    print("Welcome to Bakchod Travel's")
    print(Reservation.flight_api())
    pax_name=input('Enter Your Name:')
    res=Reservation(pax_name,'33','M','SEA','JFK','22-09-2022')
    print_details()