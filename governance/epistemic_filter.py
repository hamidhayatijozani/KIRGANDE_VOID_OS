"""
Epistemic Filter
Separates Observations from Ontological Overclaims.
"""

from enum import Enum
from typing import List, Dict, Any
import re

class ClaimType(Enum):
    OBSERVATION = "OBSERVATION"
    INFERENCE = "INFERENCE"
    ONTOLOGICAL_CLAIM = "ONTOLOGICAL_CLAIM"
    OVERCLAIM = "OVERCLAIM"

class EpistemicFilter:
    """
    Audits statements and classifies their epistemic weight.
    Overclaims are quarantined for later signal extraction.
    """

    OVERCLAIM_PATTERNS = [
        r"\balways\b", r"\bnever\b", r"\bimpossible\b",
        r"\babsolute\b", r"\bultimate\b", r"\bperfect\b",
        r"\bthe only\b", r"\bwithout exception\b"
    ]

    def __init__(self):
        self.quarantine: List[Dict[str, Any]] = []
        self.pass_count = 0

    def classify(self, statement: str) -> ClaimType:
        statement_lower = statement.lower()

        # Simple heuristic for overclaims
        for pattern in self.OVERCLAIM_PATTERNS:
            if re.search(pattern, statement_lower):
                return ClaimType.OVERCLAIM

        if any(w in statement_lower for w in ["i observed", "data shows", "measured"]):
            return ClaimType.OBSERVATION
        if any(w in statement_lower for w in ["therefore", "implies", "suggests"]):
            return ClaimType.INFERENCE

        return ClaimType.ONTOLOGICAL_CLAIM

    def audit(self, statement: str) -> Dict[str, Any]:
        claim_type = self.classify(statement)
        result = {
            "statement": statement,
            "type": claim_type.value,
            "quarantined": claim_type == ClaimType.OVERCLAIM
        }

        if claim_type == ClaimType.OVERCLAIM:
            self.quarantine.append(result)
        else:
            self.pass_count += 1

        return result

    def get_quarantine(self):
        return self.quarantine

    def status(self):
        return {
            "passed": self.pass_count,
            "quarantined": len(self.quarantine)
        }
