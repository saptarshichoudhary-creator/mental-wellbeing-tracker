import json
import math

# 1. Load the data from the JSON file
def get_clean_data(file_name="mindtrack_data.json"):
    with open(file_name, "r") as f:
        data = json.load(f)
    return data

# Helper: compute average of a list
def mean(values):
    return sum(values) / len(values)

# 2. Pure Python Pearson Correlation (No pandas needed!)
def calculate_correlation(x_vals, y_vals):
    n = len(x_vals)
    mean_x = mean(x_vals)
    mean_y = mean(y_vals)
    
    numerator = sum((x - mean_x) * (y - mean_y) for x, y in zip(x_vals, y_vals))
    denominator_x = sum((x - mean_x) ** 2 for x in x_vals)
    denominator_y = sum((y - mean_y) ** 2 for y in y_vals)
    
    denominator = math.sqrt(denominator_x * denominator_y)
    if denominator == 0:
        return 0.0
    return round(numerator / denominator, 2)

def get_correlations(logs):
    mood_list = [entry["mood_rating"] for entry in logs]
    sleep_list = [entry["sleep_hours"] for entry in logs]
    stress_list = [entry["stress_level"] for entry in logs]
    workload_list = [entry["workload_rating"] for entry in logs]
    
    return {
        "sleep": calculate_correlation(sleep_list, mood_list),
        "workload": calculate_correlation(workload_list, mood_list),
        "stress": calculate_correlation(stress_list, mood_list)
    }

# 3. Pure Python Linear Regression Slope (No sklearn needed!)
# Formula: slope (m) = sum((x - mean_x)*(y - mean_y)) / sum((x - mean_x)^2)
def get_mood_trend(logs):
    mood_list = [entry["mood_rating"] for entry in logs]
    day_indices = list(range(len(logs)))  # 0, 1, 2, ...
    
    mean_x = mean(day_indices)
    mean_y = mean(mood_list)
    
    numerator = sum((x - mean_x) * (y - mean_y) for x, y in zip(day_indices, mood_list))
    denominator = sum((x - mean_x) ** 2 for x in day_indices)
    
    slope = round(numerator / denominator, 4) if denominator != 0 else 0.0
    
    if slope > 0.01:
        direction = "improving"
    elif slope < -0.01:
        direction = "declining"
    else:
        direction = "stable"
        
    return {"slope": slope, "direction": direction}

# 4. Turn numbers into plain English flags
def make_insights(correlations, trend):
    insights = []
    
    if correlations["stress"] < -0.4:
        insights.append("High stress levels are noticeably lowering your daily mood.")
        
    if correlations["sleep"] > 0.4:
        insights.append("Getting more sleep consistently boosts your mood scores.")
        
    if correlations["workload"] < -0.4:
        insights.append("Heavier workloads tend to reduce your mood.")
        
    if trend["direction"] == "declining":
        insights.append("Your mood has been slightly drifting downward over time.")
    elif trend["direction"] == "improving":
        insights.append("Your mood shows a positive upward trend over this period.")
    else:
        insights.append("Your mood has been generally steady.")
        
    return insights

# 5. Master function that puts it together
def run_analytics():
    logs = get_clean_data("mindtrack_data.json")
    
    corrs = get_correlations(logs)
    trend = get_mood_trend(logs)
    tips = make_insights(corrs, trend)
    
    # Last 7 days average
    last_7 = logs[-7:]
    recent_averages = {
        "avg_sleep": round(mean([e["sleep_hours"] for e in last_7]), 1),
        "avg_stress": round(mean([e["stress_level"] for e in last_7]), 1),
        "avg_mood": round(mean([e["mood_rating"] for e in last_7]), 1)
    }
    
    final_report = {
        "days_logged": len(logs),
        "correlations": corrs,
        "overall_trend": trend,
        "recent_7_day_averages": recent_averages,
        "generated_insights": tips
    }
    
    return final_report

if __name__ == "__main__":
    report = run_analytics()
    print("\n--- MINDTRACK ANALYTICS REPORT ---")
    print(json.dumps(report, indent=4))