# -*- coding: utf-8 -*-
"""
OpenClaw GenPark Agent Monitor MCP Server
FastMCP standard interface for heartbeat liveness, EWMA latency drift, and Apdex performance auditing.
"""

import json
from typing import Dict, Any, List
from client import OpenClawGenParkAgentMonitor

try:
    from mcp.server.fastmcp import FastMCP
    mcp = FastMCP("openclaw-genpark-agent-monitor")
except ImportError:
    class MockFastMCP:
        def __init__(self, name):
            self.name = name
        def tool(self):
            def decorator(f):
                return f
            return decorator
    mcp = MockFastMCP("openclaw-genpark-agent-monitor")

mon = OpenClawGenParkAgentMonitor()

@mcp.tool()
def calculate_heartbeat_liveness_and_decay(
    last_heartbeat_epoch_sec: float,
    current_time_epoch_sec: float,
    expected_interval_sec: float = 5.0
) -> str:
    """
    Audits worker/agent thread liveness and decay.
    """
    res = mon.calculate_heartbeat_liveness_and_decay(last_heartbeat_epoch_sec, current_time_epoch_sec, expected_interval_sec)
    return json.dumps(res, indent=2)

@mcp.tool()
def audit_latency_drift_ewma(
    latency_series_ms: List[float],
    alpha: float = 0.2,
    alert_threshold_ms: float = 250.0
) -> str:
    """
    Calculates EWMA latency and detects change-point drift.
    """
    res = mon.audit_latency_drift_ewma(latency_series_ms, alpha, alert_threshold_ms)
    return json.dumps(res, indent=2)

@mcp.tool()
def evaluate_cluster_slos_and_apdex(
    request_latencies_ms: List[float],
    target_t_ms: float = 100.0
) -> str:
    """
    Calculates Apdex score across cluster requests.
    """
    res = mon.evaluate_cluster_slos_and_apdex(request_latencies_ms, target_t_ms)
    return json.dumps(res, indent=2)

def main():
    print("Testing Agent Monitor:")
    print(evaluate_cluster_slos_and_apdex([45, 60, 110, 250, 600]))

if __name__ == "__main__":
    main()
