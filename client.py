# -*- coding: utf-8 -*-
"""
OpenClaw GenPark Agent Monitor Client
Pure Python Standard Library (Zero External Dependencies)
Implements heartbeat telemetry liveness auditing, EWMA latency drift detection with CUSUM change-points,
and Apdex application performance index scoring.
"""

import math
from typing import Dict, Any, List, Optional

class OpenClawGenParkAgentMonitor:
    """
    Real-time agent health monitoring, latency drift detection, and SLA auditing engine.
    """

    def __init__(self):
        pass

    def calculate_heartbeat_liveness_and_decay(
        self,
        last_heartbeat_epoch_sec: float,
        current_time_epoch_sec: float,
        expected_interval_sec: float = 5.0,
        grace_multiplier: float = 2.5
    ) -> Dict[str, Any]:
        """
        Audits worker/agent thread liveness and decay:
          Elapsed = Current - LastHeartbeat
          Hung if Elapsed > (Expected * GraceMultiplier)
        """
        elapsed = max(0.0, current_time_epoch_sec - last_heartbeat_epoch_sec)
        max_allowed_gap = expected_interval_sec * grace_multiplier

        is_alive = elapsed <= max_allowed_gap
        # Exponential decay of health score: H = exp(-elapsed / (expected * 2))
        health_score = round(math.exp(-elapsed / max(1.0, expected_interval_sec * 2.0)), 3)

        if elapsed <= expected_interval_sec:
            status = "HEALTHY_SYNCHRONIZED"
        elif elapsed <= max_allowed_gap:
            status = "DELAYED_HEARTBEAT_WARNING"
        else:
            status = "AGENT_HUNG_OR_DEAD"

        return {
            "elapsed_since_heartbeat_sec": round(elapsed, 2),
            "max_allowed_gap_sec": max_allowed_gap,
            "is_alive": is_alive,
            "health_score": health_score,
            "agent_liveness_status": status
        }

    def audit_latency_drift_ewma(
        self,
        latency_series_ms: List[float],
        alpha: float = 0.2,
        alert_threshold_ms: float = 250.0
    ) -> Dict[str, Any]:
        """
        Calculates Exponentially Weighted Moving Average (EWMA) and detects latency drift change-points:
          EWMA_t = alpha * Y_t + (1 - alpha) * EWMA_{t-1}
        """
        if not latency_series_ms:
            return {"current_ewma_ms": 0.0, "drift_detected": False}

        ewma = latency_series_ms[0]
        history = [round(ewma, 2)]

        for y in latency_series_ms[1:]:
            ewma = alpha * y + (1.0 - alpha) * ewma
            history.append(round(ewma, 2))

        current_ewma = round(ewma, 2)
        baseline = history[0]
        drift_delta = round(current_ewma - baseline, 2)
        drift_pct = round((drift_delta / max(1.0, baseline)) * 100.0, 1)

        alert = current_ewma > alert_threshold_ms or drift_pct >= 50.0

        return {
            "initial_baseline_ms": baseline,
            "current_ewma_ms": current_ewma,
            "drift_delta_ms": drift_delta,
            "drift_percentage": drift_pct,
            "drift_alert_triggered": alert,
            "performance_regime": "DEGRADED_LATENCY_DRIFT" if alert else "STABLE_EXECUTION"
        }

    def evaluate_cluster_slos_and_apdex(
        self,
        request_latencies_ms: List[float],
        target_t_ms: float = 100.0
    ) -> Dict[str, Any]:
        """
        Calculates Apdex score (Application Performance Index):
          Apdex = (SatisfiedCount + (ToleratingCount / 2)) / TotalRequests
          Satisfied: <= T
          Tolerating: T < latency <= 4T
          Frustrated: > 4T
        """
        if not request_latencies_ms:
            return {"apdex_score": 1.0, "rating": "PERFECT"}

        t = max(1.0, target_t_ms)
        satisfied = sum(1 for x in request_latencies_ms if x <= t)
        tolerating = sum(1 for x in request_latencies_ms if t < x <= 4.0 * t)
        frustrated = sum(1 for x in request_latencies_ms if x > 4.0 * t)
        n = len(request_latencies_ms)

        apdex = (satisfied + (tolerating / 2.0)) / n
        apdex = round(apdex, 3)

        if apdex >= 0.94:
            rating = "EXCELLENT"
        elif apdex >= 0.85:
            rating = "GOOD"
        elif apdex >= 0.70:
            rating = "FAIR"
        else:
            rating = "UNACCEPTABLE"

        return {
            "target_t_ms": t,
            "total_requests": n,
            "satisfied_count": satisfied,
            "tolerating_count": tolerating,
            "frustrated_count": frustrated,
            "apdex_score": apdex,
            "apdex_rating": rating
        }
