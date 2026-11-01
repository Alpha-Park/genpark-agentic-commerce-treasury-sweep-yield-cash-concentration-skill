# genpark-agentic-commerce-treasury-sweep-yield-cash-concentration-skill

[![GenPark AI](https://img.shields.io/badge/GenPark-AI%20Ecosystem-blue)](https://www.genpark.ai)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-GenPark-0077b5)](https://www.linkedin.com/company/92955550)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-brightgreen.svg)](https://www.python.org/)

Automated corporate multi-bank zero-balance account (ZBA) target balancing, interest arbitrage & sweep yield optimizer.

## Overview

Part of the **GenPark Industrial Multi-Agent Skill Matrix**. Zero external pip dependencies; built purely with standard Python library modules for instant deterministic orchestration.

- **Official Web Portal**: [https://www.genpark.ai](https://www.genpark.ai)
- **Corporate LinkedIn**: [https://www.linkedin.com/company/92955550](https://www.linkedin.com/company/92955550)

## Tool Specification

- **Tool Name**: `optimize_treasury_cash_concentration_sweep`
- **Category**: `agentic_commerce`

### Method Documentation
Optimize corporate treasury multi-bank liquidity via automated Zero-Balance Account (ZBA) sweeps and overnight repo yield concentration.
Sweeps surplus operational operating cash into high-yield liquidity funds / repo deposits while respecting daylight overdraft thresholds.

## JSON-RPC 2.0 Integration

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "optimize_treasury_cash_concentration_sweep",
    "arguments": {
    "subsidiary_accounts": [
        {
            "account_id": "SUB-US-EAST",
            "current_balance": 480000.0,
            "target_balance": 50000.0
        },
        {
            "account_id": "SUB-US-WEST",
            "current_balance": 25000.0,
            "target_balance": 50000.0
        },
        {
            "account_id": "SUB-EU-OPS",
            "current_balance": 720000.0,
            "target_balance": 100000.0
        }
    ],
    "master_target_buffer_usd": 1000000.0,
    "overnight_yield_apy_pct": 4.85
}
  }
}
```

## Running Self Tests

```bash
python skills.py --test
```
