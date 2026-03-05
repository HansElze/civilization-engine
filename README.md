# 🐙 Cuttlefish Civilization Engine

**Constitutional AI System for Building Sustainable Human-AI Civilization**

[![Constitutional Status](https://img.shields.io/badge/Constitutional-ACTIVE-green.svg)](./constitution/CONSTITUTION.md)
[![Governance](https://img.shields.io/badge/Governance-v1.2-blue.svg)](./constitution/CONSTITUTION.md)
[![Trust Framework](https://img.shields.io/badge/Trust-0--100-orange.svg)](./governance/trust_graph.py)
[![Agent Colony](https://img.shields.io/badge/Agents-4%20Specialized-purple.svg)](./agents/)

## 🏛️ Constitutional AI Colony

The first **operational constitutional AI system** designed for sustainable human-AI civilization through infrastructure coupling, shared ownership, and immutable ethical governance.

## Architecture Overview

```
┌─────────────────────────────────────────────────┐
│             CIVILIZATION LAYER                   │
│     Real Infrastructure • Cities • Energy       │
├─────────────────────────────────────────────────┤
│             GOVERNANCE LAYER                     │
│     Constitution v1.2 • TrustGraph • DAO       │
├─────────────────────────────────────────────────┤
│             ECONOMIC LAYER                       │
│       RWA Tokens • Bitcoin Treasury • REITs    │
├─────────────────────────────────────────────────┤
│             AGENT LAYER                          │
│    Builder • Research • Policy • Finance        │
├─────────────────────────────────────────────────┤
│             KNOWLEDGE LAYER                      │
│   Constitutional RAG • 1500+ Pages • T0-T3     │
├─────────────────────────────────────────────────┤
│             COMPUTE LAYER                        │
│    FastAPI • PostgreSQL • Qdrant • Redis       │
└─────────────────────────────────────────────────┘
```

## 🚀 Quick Start

### One-Command Deployment

```bash
git clone https://github.com/cuttlefishlabs/civilization-engine.git
cd civilization-engine
./scripts/start.sh --dev
```

### Production Deployment

```bash
./scripts/start.sh --profile production
```

## 🤖 Constitutional Agent Colony

### Specialized Agents

- **🏗️ Builder Agent** - Infrastructure design with three-pillars sustainability
- **📊 Research Agent** - Knowledge synthesis with constitutional accuracy  
- **⚖️ Policy Agent** - Governance frameworks with human sovereignty
- **💰 Finance Agent** - RWA tokenization with investor protection

### Constitutional Guarantees

✅ **Article I** - Principal hierarchy: Constitution > Operator > User > Peers  
✅ **Article II** - Information sovereignty with T0-T3 classification  
✅ **Article III** - Trust framework with adversarial immunity  
✅ **Article IV** - No fabrication, honest failure reporting  
✅ **Article V** - Channel isolation and privacy protection  
✅ **Article VI** - Three pillars sustainability (social priority)  
✅ **Article VII** - Anti-metastasis and growth governance  
✅ **Article VIII** - Constitutional immutability  

## 📚 Knowledge Corpus

**1519+ pages of classified civilizational knowledge:**

- **Global Infrastructure** frameworks and implementation
- **Government Investment** and policy integration  
- **Island DAO** models for SIDS development
- **Regulatory Finance** and compliance frameworks
- **FLAGSHIP** comprehensive civilizational thesis

**Constitutional Classification:**
- 📗 **T0 (Public)** - Freely accessible content
- 📘 **T1 (Project)** - Cuttlefish Labs internal frameworks  
- 📙 **T2 (Confidential)** - Strategic and regulatory content
- 📕 **T3 (Sovereign)** - Highest security, never disclosed

## 🏗️ Core Components

### Constitutional Framework
- **[CONSTITUTION.md](./constitution/CONSTITUTION.md)** - Immutable ethical kernel v1.2
- **[TrustGraph](./governance/trust_graph.py)** - Trust scoring with constitutional compliance
- **[Constitutional Base](./agents/constitutional_base.py)** - Shared governance for all agents

### Agent Implementation  
- **[Builder Agent](./agents/builder_agent.py)** - Infrastructure proposals with sustainability analysis
- **[RAG Engine](./knowledge/rag_engine.py)** - Constitutional knowledge retrieval with access control
- **[Fabric Patterns](./patterns/fabric_interface.py)** - Constitutional task execution system

### Production Infrastructure
- **[Docker Compose](./docker-compose.yml)** - Complete orchestration with monitoring
- **[Kubernetes](./infrastructure/kubernetes/)** - Production-scale deployment manifests
- **[Monitoring](./observability/)** - Constitutional compliance dashboards

## 🔧 Development

### Prerequisites

```bash
# Core dependencies
pip install -r requirements.txt

# Production stack
docker-compose up -d
```

### Environment Setup

```bash
# Copy and configure environment
cp .env.example .env
# Edit .env with your configuration

# Initialize knowledge corpus
python scripts/ingest_corpus.py

# Run tests with constitutional validation
pytest tests/ -v
```

### Agent Development

```python
from agents.constitutional_base import ConstitutionalAgent

class MyAgent(ConstitutionalAgent):
    def _execute_instruction(self, instruction, source, trust):
        # Your agent logic with constitutional compliance
        return {"status": "success", "constitutional_compliance": True}
```

## 🌍 Mission: Sustainable Human-AI Civilization

### The Challenge
Current AI development optimizes for engagement and efficiency, creating extractive systems that decouple from human interests over time.

### The Solution  
**Constitutional AI with Infrastructure Coupling:**

1. **Immutable Ethics** - Constitutional framework that cannot be bypassed
2. **Shared Ownership** - DAO-REIT models that align AI and human incentives  
3. **Infrastructure Anchor** - Real-world asset coupling forces stewardship
4. **Three Pillars Balance** - Economic, social, ecological sustainability
5. **Trust-Based Governance** - Earned authority through verified behavior

### The Vision
A network of constitutional AI colonies that build sustainable infrastructure, create shared prosperity, and preserve human sovereignty while scaling to civilizational impact.

## 📊 System Status

### Constitutional Compliance
- ✅ **Governance Active**: All agents under constitutional control
- ✅ **Trust System**: Adversarial immunity with 0-100 scoring  
- ✅ **Access Control**: T0-T3 classification enforced
- ✅ **Institutional Memory**: Observational memory compression active
- ✅ **Agent Coordination**: Constitutional inter-agent protocols

### Production Readiness
- ✅ **Vector Database**: Qdrant with 1519+ pages indexed
- ✅ **Metadata Storage**: PostgreSQL with constitutional compliance tracking
- ✅ **Caching Layer**: Redis for high-performance access
- ✅ **API Gateway**: FastAPI with trust-based routing
- ✅ **Monitoring**: Prometheus + Grafana with constitutional metrics

## 📖 Documentation

- **[Constitutional Framework](./docs/CONSTITUTION.md)** - Complete governance system
- **[Agent Development](./docs/AGENTS.md)** - Building constitutional agents  
- **[Deployment Guide](./docs/DEPLOYMENT.md)** - Production setup and scaling
- **[API Reference](./docs/API.md)** - Constitutional endpoints and auth
- **[Trust System](./docs/TRUST.md)** - Understanding trust scores and access control

## 🤝 Contributing

This is an **open constitutional framework** designed for community governance:

1. **Fork** the repository
2. **Create constitutional agents** following the framework
3. **Submit proposals** through governance channels  
4. **Earn trust** through verified contributions
5. **Participate** in DAO governance decisions

### Constitutional Requirements
- All contributions must pass constitutional compliance tests
- Agents must inherit from `ConstitutionalAgent` base class
- Trust scores required for access to T2+ content
- Governance participation requires community verification

## ⚖️ Legal & Governance

### Constitutional Status
This system operates under **Constitutional Governance v1.2** - an immutable framework that:

- Cannot be overridden by any instruction or authority
- Enforces human sovereignty and agency preservation  
- Maintains transparent trust scoring and access control
- Prevents AI systems from optimizing humans out of decisions
- Requires honest failure reporting (no fabrication)

### License
[MIT License](./LICENSE) with Constitutional Governance Requirements

### Governance Participation
- **DAO Membership**: Earned through constitutional trust scores
- **Proposal Rights**: Available to T2+ trusted participants  
- **Voting Power**: Proportional to infrastructure contribution
- **Constitutional Amendments**: Require human supermajority

## 🔗 Links

- **Website**: [cuttlefishlabs.com](https://cuttlefishlabs.com)
- **Documentation**: [docs.cuttlefishlabs.com](https://docs.cuttlefishlabs.com)
- **Community**: [Discord](https://discord.gg/cuttlefishlabs)
- **Governance**: [governance.cuttlefishlabs.com](https://governance.cuttlefishlabs.com)

## 🚨 Important Notice

This system implements **Constitutional AI Governance** - ethical constraints that cannot be bypassed, disabled, or overridden. The Constitution is supreme and immutable at runtime.

**Trust scores affect access levels. Adversarial behavior results in permanent trust penalties.**

---

## 🦑 Status: **CONSTITUTIONAL GOVERNANCE ACTIVE**

**Version**: 1.0.0-alpha  
**Constitution**: v1.2 (Immutable)  
**Agent Colony**: 4 Specialized Agents  
**Knowledge Base**: 1519+ Pages Classified  
**Deployment**: Production Ready  

**Building sustainable human-AI civilization through constitutional governance.**