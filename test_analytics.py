from analytics import calculate_correlation, get_mood_trend

def test_math_engine():
    # Test 1: Check correlation bounds (-1.0 to 1.0)
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]
    corr = calculate_correlation(x, y)
    assert corr == 1.0, f"Expected 1.0, got {corr}"

    # Test 2: Check improving trend detection
    improving_logs = [{"mood_rating": i} for i in range(1, 10)]
    trend = get_mood_trend(improving_logs)
    assert trend["direction"] == "improving"

    # Test 3: Check declining trend detection
    declining_logs = [{"mood_rating": i} for i in range(10, 1, -1)]
    trend = get_mood_trend(declining_logs)
    assert trend["direction"] == "declining"

    print("All unit tests passed successfully!")

if __name__ == "__main__":
    test_math_engine()