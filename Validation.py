def validate_entry(entry):
    required_keys = ["date", "sleep_hours", "workload_rating", "stress_level", "mood_rating"]
    for key in required_keys:
        if key not in entry:
            return False, f"Missing required key: {key}"
            
    # Boundary checks (1-10 for ratings, 0-24 for sleep)
    if not (1 <= entry["workload_rating"] <= 10 and 1 <= entry["stress_level"] <= 10 and 1 <= entry["mood_rating"] <= 10):
        return False, "Ratings must be between 1 and 10."
        
    if not (0.0 <= entry["sleep_hours"] <= 24.0):
        return False, "Sleep hours must be between 0 and 24."
        
    return True, "Valid"