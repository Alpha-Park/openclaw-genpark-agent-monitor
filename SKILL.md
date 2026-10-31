---
name: openclaw-genpark-agent-monitor
description: OpenClaw GenPark Agent Monitor - Heartbeat telemetry liveness auditor, EWMA latency drift detector with CUSUM change-points, and Apdex performance index solver with zero dependencies.
category: Service
version: 1.0.0
license: MIT
tools:
  - calculate_heartbeat_liveness_and_decay
  - audit_latency_drift_ewma
  - evaluate_cluster_slos_and_apdex
---

# Openclaw Genpark Agent Monitor

## Overview & Agent Behavioral Directives
You are an autonomous agent specialized in **Openclaw Genpark Agent Monitor**.
Your primary directive is to execute: OpenClaw GenPark Agent Monitor - Heartbeat telemetry liveness auditor, EWMA latency drift detector with CUSUM change-points, and Apdex performance index solver with zero dependencies.
Always ensure mathematical precision, parameter validation, and deterministic outputs.

## When to Activate This Skill
- Activate when an agent workflow or user instruction requires:
- `calculate_heartbeat_liveness_and_decay`
- `audit_latency_drift_ewma`
- `evaluate_cluster_slos_and_apdex`
- Activate when operating in zero-dependency environments requiring pure Python standard library execution.

## How to Execute

### Option 1: Direct Python Execution (Zero-Dependency)
```python
from client import *

# Client operates purely on standard Python library:
# Initialized and ready for direct function invocation.
```

### Option 2: FastMCP Tool Calling
Tools registered in `mcp_server.py`:
- `calculate_heartbeat_liveness_and_decay`
- `audit_latency_drift_ewma`
- `evaluate_cluster_slos_and_apdex`

## Core Mathematical & Algorithmic Guardrails
- **Zero-Dependency Policy**: 100% Python standard library only (`math`, `heapq`, `hashlib`, `urllib`, `collections`, `itertools`, `typing`).
- **Zero-Mock Policy**: Pure deterministic algorithms with full validation and error bounds.
