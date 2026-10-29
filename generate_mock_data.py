import json

import random

from datetime import datetime, timedelta



def create_mock_logs(days=90):

    logs = []

    # Start 90 days ago from today

    start_date = datetime.now() - timedelta(days=days)



    for i in range(days):

        current_day = (start_date + timedelta(days=i)).strftime("%Y-%m-%d")



        # Sleep hours between 4.0 and 9.0

        sleep = round(random.uniform(4.0, 9.0), 1)



        # Scale from 1 to 10

        workload = random.randint(1, 10)



        # Simple logic: higher workload + less sleep = higher stress

        if sleep < 6.0 or workload > 6:

            stress = random.randint(6, 10)

            mood = random.randint(2, 6)

        else:

            stress = random.randint(1, 5)

            mood = random.randint(6, 10)



        logs.append({

            "date": current_day,

            "sleep_hours": sleep,

            "workload_rating": workload,

            "stress_level": stress,

            "mood_rating": mood

        })



    # Save to a clean JSON file

    with open("mindtrack_data.json", "w") as f:

        json.dump(logs, f, indent=4)



    print("Success: Generated 90 days of test logs in mindtrack_data.json!")



if __name__ == "__main__":

    create_mock_logs() 