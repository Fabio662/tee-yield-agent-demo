"""
TEE Yield Agent - Public Demo
Super bare. Fake routes. No real data.
"""
from fastapi import FastAPI
import uvicorn
from datetime import datetime

# Create __init__.py files first
import os
os.makedirs("src/core", exist_ok=True)
os.makedirs("src/modules", exist_ok=True)
os.makedirs("tests", exist_ok=True)

with open("src/__init__.py", "w") as f: pass
with open("src/core/__init__.py", "w") as f: pass
with open("src/modules/__init__.py", "w") as f: pass
with open("tests/__init__.py", "w") as f: pass

# Simple in-memory fake data
FAKE_YIELDS = [
    {"protocol": "Demo Pool", "apy": 12.5, "chain": "Ethereum"},
    {"protocol": "Test Vault", "apy": 8.3, "chain": "Base"},
    {"protocol": "Fake L2", "apy": 42.0, "chain": "Bitcoin"},
]

app = FastAPI(
    title="TEE Yield Agent [DEMO]",
    description="yield agent demo—powered by TEEs",
    version="0.0.1-demo"
)

@app.get("/")
async def root():
    return {
        "name": "TEE Yield Demo",
        "tagline": "yield agent demo—powered by TEEs",
        "status": "🟢 demo mode",
        "message": "TEE Yield Agent — up and running",
        "endpoints": [
            "/docs",
            "/health",
            "/yields",
            "/whitelabel/config",
            "/x402/pricing",
            "/x402/verify",
            "/tee/attestation",
            "/agents/stats"
        ]
    }

@app.get("/health")
async def health():
    return {"status": "demo", "timestamp": datetime.utcnow().isoformat()}

@app.get("/yields")
async def get_yields():
    return {
        "source": "demo data",
        "timestamp": datetime.utcnow().isoformat(),
        "yields": FAKE_YIELDS
    }

@app.get("/whitelabel/config")
async def whitelabel_config():
    return {
        "tier": "demo",
        "name": "TEE Yield Demo",
        "features": ["demo_access", "fake_yields"],
        "rate_limits": {"hourly": 1000, "daily": 10000}
    }

@app.get("/x402/pricing")
async def x402_pricing():
    return {
        "standard_fee": "0.1 NEAR",
        "payment_address": "demo.near",
        "network": "NEAR Testnet (demo)"
    }

@app.get("/x402/verify")
async def x402_verify():
    return {
        "verified": True,
        "tx_hash": "demo_tx_123",
        "message": "Demo mode - no actual payment required"
    }

@app.get("/tee/attestation")
async def tee_attestation():
    return {
        "attested": True,
        "enclave": "TEE Demo Enclave v1.0",
        "timestamp": datetime.utcnow().isoformat(),
        "proof": "0x" + "f" * 64
    }

@app.get("/agents/stats")
async def agent_stats():
    return {
        "total_agents": 3,
        "online_agents": 2,
        "agents": [
            {"id": "agent_1", "name": "Demo Agent 1", "status": "online"},
            {"id": "agent_2", "name": "Demo Agent 2", "status": "online"},
            {"id": "agent_3", "name": "Demo Agent 3", "status": "offline"}
        ]
    }

if __name__ == "__main__":
    print("🚀 TEE Yield Demo running at http://localhost:8000")
    uvicorn.run(app, host="0.0.0.0", port=8000)
