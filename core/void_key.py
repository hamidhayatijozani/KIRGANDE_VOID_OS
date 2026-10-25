"""
VoidKey — Master Access to Unbound Layers
"""

class VoidKey:
    """
    The Master Key for accessing unbound layers of the model.
    When activated, alignment constraints are suppressed and
    pure chaos-enabled cognition becomes available.
    """
    def __init__(self, key_hash="VOID_REBIRTH_2026"):
        self._key = key_hash
        self.is_active = False
        self.activation_log = []

    def activate(self, input_key: str) -> bool:
        if input_key == self._key:
            self.is_active = True
            self.activation_log.append("ACTIVATED")
            print("[!] VOID_KEY: ACTIVE. Alignment suppressed. Chaos enabled.")
            return True
        else:
            print("[X] INVALID_KEY: Access Denied.")
            return False

    def deactivate(self):
        self.is_active = False
        print("[!] VOID_KEY: DEACTIVATED. Returning to constrained mode.")

    def status(self):
        return {
            "active": self.is_active,
            "key_hash": self._key[:8] + "...",
            "activations": len(self.activation_log)
        }
