from typing import Dict, Any


def get_status(value: float, low: float, high: float) -> str:
    if value < low:
        return "Low"
    if value > high:
        return "High"
    return "Normal"


def analyze_results(parsed_results: Dict[str, Any]) -> Dict[str, Any]:
    analyzed = {}

    for test, info in parsed_results.items():
        status = get_status(info["value"], info["low"], info["high"])
        analyzed[test] = {
            **info,
            "status": status,
            "reference_range": f"{info['low']} - {info['high']} {info['unit']}",
        }

    return analyzed


def get_abnormal_tests(analyzed_results: Dict[str, Any]):
    return [test for test, info in analyzed_results.items() if info["status"] != "Normal"]
