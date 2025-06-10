import pandas
from datetime import datetime 

patient_ts_str = "2025-01-01 11:05:00"
patient_ts_dt = datetime.strptime(patient_ts_str, "%Y-%m-%d %H:%M:%S" )
print(patient_ts_dt, type(patient_ts_dt))
print(patient_ts_dt.day)

now_dt= datetime.now()
print("Current Date:", now_dt)
time_since_patient= now_dt- patient_ts_dt
print(time_since_patient)

patient_ts_str2= patient_ts_dt.strftime("%B %d, %Y at %I:%M %p")
print(patient_ts_str2)

#make timezone aware using tzinfo=zoneinfo
#this will go off of UTC (PST will be -8)
#to do calculations you must have all aware or all naive data 

#pandas equivalent is pandas.timestamp

#use utc=true to make timezone aware data

#To-Do: research resample more
