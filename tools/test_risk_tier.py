"""Unit tests for risk_tier.py. Run: python -m unittest test_risk_tier -v"""
import unittest
from risk_tier import assess


class TestRiskTier(unittest.TestCase):
    def test_stop_check_is_tier0(self):
        r = assess({"A": ["A3"], "C": [], "autonomy": "L1"})
        self.assertEqual(r["tier"], 0)
        self.assertTrue(r["legal_escalation"])

    def test_high_risk_domain_is_tier1_even_with_low_score(self):
        r = assess({"B": ["B5"], "C": [], "autonomy": "L1"})
        self.assertEqual(r["tier"], 1)
        self.assertTrue(r["committee_approval_required"])

    def test_boundaries(self):
        self.assertEqual(assess({"C": ["C1"], "autonomy": "L1"})["tier"], 3)            # 3
        self.assertEqual(assess({"C": ["C1", "C2"], "autonomy": "L1"})["tier"], 2)      # 4
        self.assertEqual(assess({"C": ["C1", "C2", "C3", "C4"], "autonomy": "L1"})["tier"], 2)  # 7
        self.assertEqual(assess({"C": ["C1", "C2", "C3", "C4", "C6"], "autonomy": "L1"})["tier"], 1)  # 8

    def test_agent_floor(self):
        base = {"C": ["C2"], "autonomy": "L3"}  # score 3 -> Tier 3
        self.assertEqual(assess(base)["tier"], 3)
        self.assertEqual(assess({**base, "production_write_access": True})["tier"], 2)

    def test_l2_has_no_floor(self):
        r = assess({"C": ["C2"], "autonomy": "L2", "production_write_access": True})
        self.assertEqual(r["tier"], 3)

    def test_l4_needs_committee(self):
        r = assess({"C": [], "autonomy": "L4", "production_write_access": True})
        self.assertTrue(r["committee_approval_required"])
        self.assertEqual(r["tier"], 2)

    def test_l4_alone_is_never_tier3(self):
        # L4 = 4 points, so Tier 2 by score even without production write access
        r = assess({"C": [], "autonomy": "L4", "production_write_access": False})
        self.assertEqual(r["score"], 4)
        self.assertEqual(r["tier"], 2)
        self.assertTrue(r["committee_approval_required"])

    def test_legal_escalation_covers_tier0_and_every_tier1_path(self):
        # Tier 0
        self.assertTrue(assess({"A": ["A3"], "autonomy": "L1"})["legal_escalation"])
        # Tier 1 via high-risk domain
        self.assertTrue(assess({"B": ["B5"], "autonomy": "L1"})["legal_escalation"])
        # Tier 1 via score >= 8 with no Section B domain
        r = assess({"C": ["C1", "C2", "C3", "C4", "C6"], "autonomy": "L1"})
        self.assertEqual((r["tier"], r["score"]), (1, 8))
        self.assertTrue(r["legal_escalation"])
        # Tier 2 and Tier 3 do not require a Legal confirmation
        self.assertFalse(assess({"C": ["C1", "C2"], "autonomy": "L1"})["legal_escalation"])
        self.assertFalse(assess({"C": ["C1"], "autonomy": "L1"})["legal_escalation"])

    def test_unknown_codes_rejected(self):
        for bad in ({"A": ["A99"]}, {"B": ["B0"]}, {"C": ["C10"]}, {"autonomy": "L5"}):
            with self.assertRaises(ValueError):
                assess(bad)

    def test_duplicate_codes_not_double_counted(self):
        self.assertEqual(assess({"C": ["C1", "C1"], "autonomy": "L1"})["score"], 3)


if __name__ == "__main__":
    unittest.main()
