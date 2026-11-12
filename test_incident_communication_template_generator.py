import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import unittest
from main import render

def incident(severity="P1", status="investigating", eta=60):
    return {"id": "INC-42", "severity": severity, "service": "Email",
            "status": status, "started": "2026-11-08T09:00:00", "eta_minutes": eta}

class TestIncidentCommunication(unittest.TestCase):
    def test_p1_impact_wording(self):
        self.assertIn("Service is unavailable", render(incident("P1")))
    def test_p2_impact_wording(self):
        self.assertIn("major feature is degraded", render(incident("P2")))
    def test_p4_impact_wording(self):
        self.assertIn("No customer-facing effect", render(incident("P4")))
    def test_unknown_severity_falls_back_to_p4(self):
        self.assertIn("No customer-facing effect", render(incident("P9")))
    def test_next_update_computed(self):
        self.assertIn("Next update: 2026-11-08 10:00 (60 minutes)", render(incident()))
    def test_all_fields_appear(self):
        note = render(incident())
        self.assertIn("INC-42", note)
        self.assertIn("Email", note)
        self.assertIn("investigating", note)
    def test_severity_case_insensitive(self):
        self.assertIn("Service is unavailable", render(incident("p1")))
