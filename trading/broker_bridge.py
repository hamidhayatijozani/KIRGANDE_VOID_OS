"""
Broker Bridge
Conceptual connector to cTrader Open API.
"""

from typing import Optional, Dict, Any
from datetime import datetime

class BrokerBridge:
    """
    Lightweight abstraction over cTrader connectivity.
    Real implementation would use ctrader-open-api.
    """

    def __init__(self, account_id: Optional[str] = None, demo: bool = True):
        self.account_id = account_id or "DEMO_VOID"
        self.demo = demo
        self.connected = False
        self.last_heartbeat = None

    def connect(self) -> bool:
        """Simulate connection."""
        self.connected = True
        self.last_heartbeat = datetime.utcnow().isoformat()
        print(f"[BRIDGE] Connected to {'DEMO' if self.demo else 'LIVE'} account: {self.account_id}")
        return True

    def disconnect(self):
        self.connected = False
        print("[BRIDGE] Disconnected.")

    def place_order(self, symbol: str, side: str, volume: float, 
                    stop_loss: Optional[float] = None, 
                    take_profit: Optional[float] = None) -> Dict[str, Any]:
        if not self.connected:
            raise RuntimeError("Not connected to broker")

        order = {
            "symbol": symbol,
            "side": side.upper(),
            "volume": volume,
            "sl": stop_loss,
            "tp": take_profit,
            "timestamp": datetime.utcnow().isoformat(),
            "status": "SIMULATED"
        }
        print(f"[ORDER] {order['side']} {volume} {symbol}")
        return order

    def status(self):
        return {
            "connected": self.connected,
            "account": self.account_id,
            "demo": self.demo,
            "last_heartbeat": self.last_heartbeat
        }
