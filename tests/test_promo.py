"""Your TDD workspace. The first test is deliberately RED -- that is step one."""
from datetime import date

import pytest

from tdd_lab.promo import PromoError, apply_promo

TODAY = date(2026, 11, 9)


def test_save10_takes_ten_percent_off():
    assert apply_promo(10_000, "SAVE10", TODAY) == 9_000


def test_save10_rounds_discount_down():
    # 10% of 1,005 is 100.5; the discount rounds down to 100 cents.
    assert apply_promo(1_005, "SAVE10", TODAY) == 905


def test_flat5_minimum_boundary():
    assert apply_promo(2_000, "FLAT5", TODAY) == 1_500
    with pytest.raises(PromoError):
        apply_promo(1_999, "FLAT5", TODAY)


def test_welcome_expiry_boundary():
    assert apply_promo(10_000, "WELCOME", date(2026, 12, 31)) == 8_500
    with pytest.raises(PromoError):
        apply_promo(10_000, "WELCOME", date(2027, 1, 1))


def test_codes_ignore_case_and_surrounding_whitespace():
    assert apply_promo(10_000, "  save10 ", TODAY) == 9_000


def test_unknown_code_raises_and_total_never_goes_below_zero():
    with pytest.raises(PromoError):
        apply_promo(10_000, "NOT_A_CODE", TODAY)
    assert apply_promo(0, "WELCOME", TODAY) == 0

# Next: write a failing test for the next rule, make it pass, refactor. Repeat.
# Think edge cases: rounding, case/whitespace, minimums, expiry date boundary,
# unknown code, and a total that would otherwise go negative.
