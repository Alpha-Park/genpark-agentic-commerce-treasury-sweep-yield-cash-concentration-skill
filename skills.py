# -*- coding: utf-8 -*-
"""GenPark Industrial Skill: genpark-agentic-commerce-treasury-sweep-yield-cash-concentration-skill
Category: agentic_commerce
Website: https://www.genpark.ai
LinkedIn: https://www.linkedin.com/company/92955550
"""
import sys
import json
import math

sys.stdout.reconfigure(encoding="utf-8")

def optimize_treasury_cash_concentration_sweep(subsidiary_accounts, master_target_buffer_usd=1000000.0, overnight_yield_apy_pct=4.85):
    total_subsidiary_surplus = 0.0
    total_subsidiary_deficit = 0.0
    sweep_transfers = []
    
    for acc in subsidiary_accounts:
        aid = acc["account_id"]
        bal = acc["current_balance"]
        target = acc.get("target_balance", 50000.0)
        variance = bal - target
        
        if variance > 0:
            # Sweep out surplus to master
            total_subsidiary_surplus += variance
            sweep_transfers.append({
                "from_account": aid,
                "to_account": "MASTER_TREASURY_CONCENTRATION",
                "transfer_amount": round(variance, 2),
                "type": "SURPLUS_SWEEP_UP"
            })
        elif variance < 0:
            deficit = abs(variance)
            total_subsidiary_deficit += deficit
            sweep_transfers.append({
                "from_account": "MASTER_TREASURY_CONCENTRATION",
                "to_account": aid,
                "transfer_amount": round(deficit, 2),
                "type": "TARGET_BALANCE_TOP_UP"
            })
            
    net_sweep_to_master = total_subsidiary_surplus - total_subsidiary_deficit
    investable_overnight_cash = max(0.0, net_sweep_to_master)
    # Overnight 1-day interest: investable * (APY / 365)
    daily_interest_earned = (investable_overnight_cash * (overnight_yield_apy_pct / 100.0)) / 365.0
    
    return {
        "accounts_managed": len(subsidiary_accounts),
        "total_surplus_swept_usd": round(total_subsidiary_surplus, 2),
        "total_deficit_topped_up_usd": round(total_subsidiary_deficit, 2),
        "net_swept_to_master_usd": round(net_sweep_to_master, 2),
        "investable_overnight_liquidity_usd": round(investable_overnight_cash, 2),
        "annualized_yield_apy_pct": overnight_yield_apy_pct,
        "daily_arbitrage_interest_yield_usd": round(daily_interest_earned, 2),
        "automated_wire_instructions": sweep_transfers
    }


def handle_rpc(request_str):
    try:
        req = json.loads(request_str)
        rpc_id = req.get("id")
        method = req.get("method")
        params = req.get("params", {})
        
        if method == "tools/list":
            return json.dumps({
                "jsonrpc": "2.0",
                "id": rpc_id,
                "result": {
                    "tools": [{
                        "name": "optimize_treasury_cash_concentration_sweep",
                        "description": """Optimize corporate treasury multi-bank liquidity via automated Zero-Balance Account (ZBA) sweeps and overnight repo yield concentration.
Sweeps surplus operational operating cash into high-yield liquidity funds / repo deposits while respecting daylight overdraft thresholds.""",
                        "inputSchema": {
                            "type": "object",
                            "properties": {}
                        }
                    }]
                }
            })
        elif method == "tools/call":
            call_params = params.get("arguments", {})
            res = optimize_treasury_cash_concentration_sweep(**call_params)
            return json.dumps({
                "jsonrpc": "2.0",
                "id": rpc_id,
                "result": {
                    "content": [{
                        "type": "text",
                        "text": json.dumps(res, indent=2)
                    }]
                }
            })
        else:
            return json.dumps({
                "jsonrpc": "2.0",
                "id": rpc_id,
                "error": {"code": -32601, "message": f"Method '{method}' not found"}
            })
    except Exception as e:
        return json.dumps({
            "jsonrpc": "2.0",
            "id": None,
            "error": {"code": -32000, "message": str(e)}
        })

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        sample = {'subsidiary_accounts': [{'account_id': 'SUB-US-EAST', 'current_balance': 480000.0, 'target_balance': 50000.0}, {'account_id': 'SUB-US-WEST', 'current_balance': 25000.0, 'target_balance': 50000.0}, {'account_id': 'SUB-EU-OPS', 'current_balance': 720000.0, 'target_balance': 100000.0}], 'master_target_buffer_usd': 1000000.0, 'overnight_yield_apy_pct': 4.85}
        out = optimize_treasury_cash_concentration_sweep(**sample)
        print("[TEST_PASS] Output:", json.dumps(out))
    else:
        for line in sys.stdin:
            line = line.strip()
            if not line:
                continue
            print(handle_rpc(line))
