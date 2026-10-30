# -*- coding: utf-8 -*-
from client import OpenClawGenParkAgentMonitor

mon = OpenClawGenParkAgentMonitor()

# 1. Heartbeat Telemetry Liveness
live = mon.calculate_heartbeat_liveness_and_decay(last_heartbeat_epoch_sec=1730000000.0, current_time_epoch_sec=1730000008.5, expected_interval_sec=5.0)
print(f"Liveness Check: IsAlive={live['is_alive']} ({live['agent_liveness_status']}, Health: {live['health_score']})")

# 2. EWMA Latency Drift
latencies = [95.0, 105.0, 120.0, 150.0, 210.0, 290.0, 340.0]
drift = mon.audit_latency_drift_ewma(latencies, alpha=0.3, alert_threshold_ms=250.0)
print()
print(f"Latency Drift: EWMA={drift['current_ewma_ms']}ms (Delta={drift['drift_delta_ms']}ms, {drift['performance_regime']}, Alert={drift['drift_alert_triggered']})")

# 3. Apdex Performance Index
requests = [40.0, 55.0, 80.0, 95.0, 120.0, 180.0, 450.0]
apdex = mon.evaluate_cluster_slos_and_apdex(requests, target_t_ms=100.0)
print()
print(f"Apdex Score: {apdex['apdex_score']} ({apdex['apdex_rating']}, Satisfied={apdex['satisfied_count']}, Tolerating={apdex['tolerating_count']}, Frustrated={apdex['frustrated_count']})")
