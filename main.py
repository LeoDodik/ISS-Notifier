import smtplib
import time
import requests
from datetime import datetime



MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude

def is_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.
    if MY_LONG-5 <= iss_longitude or MY_LONG+5 <=iss_longitude and MY_LAT-5 <= iss_latitude or MY_LAT+5 <= iss_latitude:
       return True



def is_night():
    if sunset >= time_now or time_now <= sunrise:
       return True

parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])




time_now = int(datetime.now())

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

while True:
    time.sleep(60)
    if is_night() and is_overhead():
        my_email = "mytest@gmail.com"
        password = "fs23s21s23s212s31"

        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="test71@gmail.com",
                                msg=f"Subject:Notification")



