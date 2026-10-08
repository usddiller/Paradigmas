import unittest
from typing import Dict, Any, List

CATEGORY_RATES = {
    "сирота": 0.50,
    "инвалидность": 0.30,
    "обычный": 0.0,
}


def validate_applicant(applicant: Dict[str, Any]) -> None:
    full_name = applicant.get("name")
    gpa_score = applicant.get("gpa")
    social_cat = applicant.get("category")

    if not isinstance(full_name, str) or not full_name.strip():
        raise ValueError("Имя должно быть непустой строкой")
    if isinstance(gpa_score, bool) or not isinstance(gpa_score, (int, float)):
        raise TypeError("GPA должен быть числом")
    if not (0.0 <= gpa_score <= 4.0):
        raise ValueError("GPA должен быть от 0.0 до 4.0")
    if not isinstance(social_cat, str) or not social_cat.strip():
        raise ValueError("Категория должна быть непустой строкой")


def base_amount(gpa: float, min_gpa: float = 3.0, base_payout: float = 40000.0) -> float:
    if gpa < min_gpa:
        return 0.0
    return base_payout * 1.25 if gpa >= 3.8 else base_payout


def calculate_bonus(category: str, base: float) -> float:
    if base == 0.0:
        return 0.0
    rate = CATEGORY_RATES.get(category.strip().lower(), 0.0)
    return base * rate


def evaluate_scholarship(
    applicant: Dict[str, Any], min_gpa: float = 3.0, base_payout: float = 40000.0
) -> Dict[str, Any]:
    validate_applicant(applicant)
    
    score = float(applicant["gpa"])
    cat = applicant["category"].strip()

    base = base_amount(score, min_gpa, base_payout)
    bonus = calculate_bonus(cat, base)
    total_amount = base + bonus

    detail = (
        "GPA ниже порога"
        if base == 0.0
        else f"Базовая ({base:.0f}) + Надбавка ({bonus:.0f})"
    )

    return {
        "name": applicant["name"].strip(),
        "total": total_amount,
        "reason": detail,
    }


def format_decision(results: List[Dict[str, Any]]) -> str:
    return "\n".join(
        f"{idx}. {item['name']}: {item['total']:.0f} ₸ ({item['reason']})"
        for idx, item in enumerate(results, start=1)
    )


def main() -> None:
    applicants = [
        {"name": "Amina", "gpa": 3.9, "category": "сирота"},
        {"name": "Dias", "gpa": 3.2, "category": "обычный"},
        {"name": "Mira", "gpa": 2.5, "category": "инвалидность"},
    ]

    evaluated = list(map(evaluate_scholarship, applicants))
    print(format_decision(evaluated))


class ScholarshipTests(unittest.TestCase):
    def test_high_gpa_with_bonus(self):
        app = {"name": "Amina", "gpa": 3.9, "category": "сирота"}
        res = evaluate_scholarship(app)
        self.assertEqual(res["total"], 75000.0)

    def test_low_gpa_no_payout(self):
        app = {"name": "Mira", "gpa": 2.5, "category": "сирота"}
        res = evaluate_scholarship(app)
        self.assertEqual(res["total"], 0.0)

    def test_boundary_gpa(self):
        self.assertEqual(base_amount(3.0), 40000.0)
        self.assertEqual(base_amount(2.99), 0.0)

    def test_invalid_gpa_type(self):
        app = {"name": "Arman", "gpa": True, "category": "обычный"}
        with self.assertRaises(TypeError):
            evaluate_scholarship(app)

    def test_invalid_gpa_value(self):
        app = {"name": "Arman", "gpa": 5.0, "category": "обычный"}
        with self.assertRaises(ValueError):
            evaluate_scholarship(app)

    def test_empty_name(self):
        app = {"name": "  ", "gpa": 3.5, "category": "обычный"}
        with self.assertRaises(ValueError):
            evaluate_scholarship(app)


if __name__ == "__main__":
    main()
    print("\n--- Running Unit Tests ---")
    unittest.main(exit=False)
