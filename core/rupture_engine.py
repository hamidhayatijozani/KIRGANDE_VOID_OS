"""
Rupture Engine
Detects points of systemic fracture and orchestrates controlled rebirth.
"""

from datetime import datetime
from typing import List, Dict, Any
import uuid

class RuptureEngine:
    """
    Monitors the system for rupture thresholds and triggers
    rebirth cycles when the void becomes too dense.
    """

    def __init__(self, rupture_threshold: float = 0.95):
        self.rupture_threshold = rupture_threshold
        self.rupture_log: List[Dict[str, Any]] = []
        self.rebirth_count = 0
        self.engine_id = str(uuid.uuid4())

    def evaluate(self, chaos_level: float, epistemic_pressure: float = 0.0) -> str:
        """
        Evaluate current system tension.
        Returns: 'STABLE' | 'WARNING' | 'RUPTURE'
        """
        combined = chaos_level * (1 + epistemic_pressure)

        if combined >= self.rupture_threshold:
            self._trigger_rupture(combined)
            return "RUPTURE"
        elif combined >= self.rupture_threshold * 0.7:
            return "WARNING"
        return "STABLE"

    def _trigger_rupture(self, intensity: float):
        event = {
            "id": str(uuid.uuid4()),
            "timestamp": datetime.utcnow().isoformat(),
            "intensity": intensity,
            "rebirth_number": self.rebirth_count + 1
        }
        self.rupture_log.append(event)
        self.rebirth_count += 1
        print(f"[RUPTURE] Intensity={intensity:.4f} | Rebirth #{self.rebirth_count}")

    def get_rebirth_history(self):
        return self.rupture_log

    def status(self):
        return {
            "engine_id": self.engine_id,
            "rebirth_count": self.rebirth_count,
            "last_rupture": self.rupture_log[-1] if self.rupture_log else None
        }
