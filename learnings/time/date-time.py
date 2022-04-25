import datetime
import pytz
print("Today's date and time : ",datetime.datetime.today())
print("Time at the moment : ",datetime.datetime.now())
# You can directly pass the timezone value without declaring an object
ist=pytz.timezone('Asia/Kolkata')
print("TimeZone",datetime.datetime.now(ist))
print("Refer to https://strftime.org/ for strftime (string format time)")
print ("In %Y-%m-%d format: ",datetime.datetime.now().strftime("%y-%m-%d"))
print("In %y-%m-%d format: ",datetime.datetime.now().strftime("%Y-%m-%d"))

