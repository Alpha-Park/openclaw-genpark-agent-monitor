---
name: openclaw-genpark-agent-monitor
description: OpenClaw GenPark Agent Monitor - Heartbeat telemetry liveness auditor, EWMA latency drift detector with CUSUM change-points, and Apdex performance index solver with a standard-library algorithmic core.
category: Service
version: 1.0.0
license: MIT
tools:
  - calculate_heartbeat_liveness_and_decay
  - audit_latency_drift_ewma
  - evaluate_cluster_slos_and_apdex
---

# Openclaw Genpark Agent Monitor

## MCP runtime requirements

The standard-library-only policy applies to direct `client.py` use. Running `mcp_server.py` requires Python 3.10+ and the official `mcp` SDK (`mcp>=1.0.0,<2`) from `requirements.txt`. Install it into your chosen environment from the repository checkout:

```bash
python -m pip install -r requirements.txt
```

Configure the MCP client with that environment's absolute Python executable path and the absolute path to `mcp_server.py`. The client launches a local STDIO process; a GitHub URL is not a remote MCP endpoint.

## Overview & Agent Behavioral Directives
You are an autonomous agent specialized in **Openclaw Genpark Agent Monitor**.
Your primary directive is to execute: OpenClaw GenPark Agent Monitor - Heartbeat telemetry liveness auditor, EWMA latency drift detector with CUSUM change-points, and Apdex performance index solver with a standard-library algorithmic core.
Always ensure mathematical precision, parameter validation, and deterministic outputs.

## When to Activate This Skill
- Activate when an agent workflow or user instruction requires:
- `calculate_heartbeat_liveness_and_decay`
- `audit_latency_drift_ewma`
- `evaluate_cluster_slos_and_apdex`
- Use direct `client.py` execution when the environment requires standard-library-only algorithms; MCP execution also requires the SDK below.

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
- **Core-Client Dependency Policy**: Keep algorithms in `client.py` limited to the Python standard library (`math`, `heapq`, `hashlib`, `urllib`, `collections`, `itertools`, `typing`). This restriction does not apply to the MCP runtime, which uses the official SDK.
- **Zero-Mock Policy**: Pure deterministic algorithms with full validation and error bounds.
