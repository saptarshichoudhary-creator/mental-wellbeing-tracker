import json
import Validation
data={}
l=[]
print("=" * 50)
print("     🧠 MINDTRACK - DAILY WELLNESS CHECK-IN      ")
print("=" * 50)
print("Take a quick moment to reflect on your day (1-10):")

mood = int(input("😊 How would you rate your overall mood today? (1-10): "))
sleep = int(input("😴 How well did you sleep last night? (1-10): "))
workload = int(input("📚 How heavy was your workload or academic pressure today? (1-10): "))
social_interaction = int(input("🤝 How connected did you feel with friends or family today? (1-10): "))
activity = int(input("🏃 How physically active were you today? (1-10): "))
anxiety = int(input("🌊 How much tension or anxiety did you experience? (1-10): "))
data={"mood":mood,"sleep":sleep,"workload":workload,"social_interaction":social_interaction,"physical_activity":activity,"anxiety":anxiety}
is_valid,message=Validation.validate_entry(data)
if is_valid==True:
 l.append(data)
 json_dump=json.dumps(l,indent=4)
 print("Success")
 print(json_dump)
else:
 print(f"Error:{message}")