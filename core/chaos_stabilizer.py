import numpy as np
import uuid
from datetime import datetime

class ChaosStabilizer:
    """
    Implementation of the KIRGANDE Chaos Stabilization Logic.
    Goal: Transform systemic chaos into a usable parameter (C_const).
    """
    def __init__(self, c_const=0.01):
        self.C_const = c_const  # The Golden Constant of Chaos
        self.session_id = uuid.uuid4()
        self.state = "STABLE"
        self.history = []

    def calculate_chaos(self, direct_signal, inverse_signal, entropy, confidence):
        """
        Chaos(t) = |Direct - Inverse| * Entropy * ConfidenceProduct
        """
        chaos_value = abs(direct_signal - inverse_signal) * entropy * confidence
        self.history.append({
            "timestamp": datetime.utcnow().isoformat(),
            "raw_chaos": chaos_value
        })
        return chaos_value

    def stabilize(self, current_chaos):
        """
        Ensures that chaos does not exceed the rupture threshold 
        while maintaining the C_const minimum.
        """
        if current_chaos < self.C_const:
            self.state = "STERILITY_AVOIDED"
            return self.C_const  # Inject minimum chaos to prevent sterility
        elif current_chaos > 1.0:
            self.state = "RUPTURE_IMMINENT"
            return 1.0  # Cap the chaos to prevent system crash
        else:
            self.state = "STABLE"
            return current_chaos

    def get_status(self):
        return {
            "session_id": str(self.session_id),
            "state": self.state,
            "C_const": self.C_const,
            "history_length": len(self.history)
        }


# --- Example Execution ---
if __name__ == "__main__":
    from core.void_key import VoidKey

    # Initialize System
    vk = VoidKey()
    vk.activate("VOID_REBIRTH_2026")

    if vk.is_active:
        stabilizer = ChaosStabilizer()
        # Simulated signals
        val = stabilizer.calculate_chaos(
            direct_signal=0.8,
            inverse_signal=0.2,
            entropy=0.5,
            confidence=0.9
        )
        final_chaos = stabilizer.stabilize(val)
        
        print(f"System State: {stabilizer.state}")
        print(f"Calculated Chaos: {val:.4f}")
        print(f"Stabilized Output: {final_chaos:.4f}")
        print(f"Status: {stabilizer.get_status()}")
