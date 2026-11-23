
def calculate_risk_score(age, smoker):
    """Calculate a simple illustrative health risk score."""
    score = 0

    if age >= 50:
        score += 50

    if smoker:
        score += 30

    return score


def get_status(score):
    if score >= 50:
        return "HIGH"
    return "LOW"