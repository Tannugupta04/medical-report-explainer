import re
from typing import Dict, Any

# Basic reference ranges. These can vary by age, gender, lab, and unit.
# For a real clinical product, use lab-specific reference ranges from the report.
TEST_PATTERNS = {
    "Hemoglobin": {
        "aliases": ["hemoglobin", "haemoglobin", "hb"],
        "unit": "g/dL",
        "low": 12.0,
        "high": 16.0,
    },
    "WBC Count": {
        "aliases": ["wbc", "white blood cell", "total leukocyte count", "tlc"],
        "unit": "10^3/uL",
        "low": 4.0,
        "high": 11.0,
    },
    "RBC Count": {
        "aliases": ["rbc", "red blood cell"],
        "unit": "million/uL",
        "low": 4.2,
        "high": 5.9,
    },
    "Platelets": {
        "aliases": ["platelet", "platelets"],
        "unit": "10^3/uL",
        "low": 150,
        "high": 450,
    },
    "Fasting Glucose": {
        "aliases": ["fasting glucose", "fasting blood sugar", "fbs", "glucose fasting"],
        "unit": "mg/dL",
        "low": 70,
        "high": 100,
    },
    "Random Glucose": {
        "aliases": ["random glucose", "random blood sugar", "rbs"],
        "unit": "mg/dL",
        "low": 70,
        "high": 140,
    },
    "Total Cholesterol": {
        "aliases": ["total cholesterol", "cholesterol total"],
        "unit": "mg/dL",
        "low": 0,
        "high": 200,
    },
    "Vitamin D": {
        "aliases": ["vitamin d", "25 hydroxy vitamin d", "25-oh vitamin d"],
        "unit": "ng/mL",
        "low": 30,
        "high": 100,
    },
    "TSH": {
        "aliases": ["tsh", "thyroid stimulating hormone"],
        "unit": "mIU/L",
        "low": 0.4,
        "high": 4.0,
    },
    "Creatinine": {
        "aliases": ["creatinine", "serum creatinine"],
        "unit": "mg/dL",
        "low": 0.6,
        "high": 1.3,
    },
}


def _find_value_near_alias(text: str, alias: str):
    """
    Tries to find a numeric value near a test name.
    Works for many simple reports like: Hemoglobin 13.2 g/dL
    """
    pattern = rf"({re.escape(alias)})[^\n\r:]*[:\s-]*([0-9]+(?:\.[0-9]+)?)"
    match = re.search(pattern, text, flags=re.IGNORECASE)
    if match:
        return float(match.group(2))
    return None


def parse_report_text(text: str) -> Dict[str, Any]:
    results = {}

    clean_text = re.sub(r"\s+", " ", text)

    for test_name, details in TEST_PATTERNS.items():
        found_value = None
        matched_alias = None

        for alias in details["aliases"]:
            found_value = _find_value_near_alias(clean_text, alias)
            if found_value is not None:
                matched_alias = alias
                break

        if found_value is not None:
            results[test_name] = {
                "value": found_value,
                "unit": details["unit"],
                "low": details["low"],
                "high": details["high"],
                "matched_alias": matched_alias,
            }

    return results
