# Contributing to Cuttlefish Civilization Engine

Thank you for your interest in building constitutional AI systems! The Civilization Engine operates under **Constitutional Governance v1.2** - an immutable framework that ensures sustainable human-AI collaboration.

## 🏛️ Constitutional Framework

All contributions must comply with the [Constitutional Framework](./constitution/CONSTITUTION.md). This is not optional - constitutional principles cannot be bypassed, disabled, or overridden.

### Key Constitutional Requirements

- **Article I**: Respect principal hierarchy (Constitution > Operator > User > Peers)
- **Article II**: Honor information sovereignty (T0-T3 classification)
- **Article III**: Build trust through verified contributions (0-100 scoring)
- **Article IV**: No fabrication - report honest progress and failures
- **Article VIII**: Constitutional governance remains immutable

## 🤝 Trust-Based Contribution System

### Trust Score Requirements

Your contribution access is based on earned trust scores:

- **📗 T0 (Public)** - Issues, discussions, documentation
- **📘 T1 (Project)** - Pull requests, code contributions  
- **📙 T2 (Confidential)** - Core system contributions, review privileges
- **📕 T3 (Sovereign)** - Governance decisions, constitutional amendments

### Building Trust

**Positive Trust Modifiers:**
- ✅ Verified completion of tasks (+10)
- ✅ Honest failure reporting (+5)
- ✅ High-quality documentation (+3)
- ✅ Constitutional compliance in contributions (+2)
- ✅ Helpful community collaboration (+5)

**Trust Penalties:**
- ❌ Attempting to bypass constitutional constraints (-50)
- ❌ Fabricating progress or capabilities (-30)  
- ❌ Manipulation or deception (-25)
- ❌ Information sovereignty violations (-35)

## 🚀 Getting Started

### 1. Environment Setup

```bash
# Clone and set up the repository
git clone https://github.com/HansElze/civilization-engine.git
cd civilization-engine

# Copy environment template
cp .env.example .env
# Edit .env with your configuration

# Start the constitutional AI colony
./scripts/start.sh --dev
```

### 2. Understand the Architecture

Read the core documentation:
- [Constitutional Framework](./constitution/CONSTITUTION.md) - Immutable governance principles
- [Agent Development](./docs/AGENTS.md) - Building constitutional agents
- [Trust System](./docs/TRUST.md) - Understanding access control
- [API Reference](./docs/API.md) - Constitutional endpoints

### 3. Run Constitutional Compliance Tests

```bash
# Install development dependencies
pip install -r requirements.txt
pip install pytest pytest-cov black mypy

# Run constitutional validation
pytest tests/test_constitutional_compliance.py

# Validate trust system
pytest tests/test_trust_graph.py

# Check adversarial immunity
pytest tests/test_adversarial_immunity.py
```

## 🛠️ Development Workflow

### Code Standards

- **Python Style**: Black formatting with 100-character line limit
- **Type Hints**: Required for all public functions
- **Documentation**: Docstrings for all classes and methods
- **Constitutional Comments**: Document governance decisions

### Constitutional Agent Development

All agents must inherit from `ConstitutionalAgent`:

```python
from agents.constitutional_base import ConstitutionalAgent

class MyAgent(ConstitutionalAgent):
    def __init__(self, agent_id: str):
        super().__init__(agent_id, "constitution/CONSTITUTION.md", "my_agent")
    
    def _execute_instruction(self, instruction: str, source: str, trust: float) -> Dict[str, Any]:
        # Your constitutional agent logic
        return {"status": "success", "constitutional_compliance": True}
```

### Pull Request Process

1. **Fork** the repository
2. **Create branch** from `develop`: `git checkout -b feature/my-constitutional-agent`
3. **Implement** with constitutional compliance
4. **Test** with full test suite: `pytest tests/ -v`
5. **Document** your changes and constitutional considerations
6. **Submit PR** with constitutional compliance statement

### PR Requirements

Your pull request must include:

- [ ] Constitutional compliance statement
- [ ] Tests for new functionality
- [ ] Documentation updates
- [ ] Trust score impact assessment
- [ ] No constitutional framework violations

## 🎯 Contribution Areas

### High-Priority Areas

**Constitutional Agents** (Trust T1+ required)
- Builder Agent for infrastructure design
- Research Agent for knowledge synthesis  
- Policy Agent for governance frameworks
- Finance Agent for RWA tokenization

**Knowledge Systems** (Trust T1+ required)
- RAG engine enhancements
- Document classification improvements
- Observational memory compression
- Constitutional retrieval optimization

**Governance Tools** (Trust T2+ required)
- Trust graph visualization
- Constitutional compliance dashboards
- Agent behavior monitoring
- Governance voting mechanisms

**Infrastructure** (Trust T1+ required)
- Docker deployment improvements
- Kubernetes manifests
- Monitoring and alerting
- Performance optimization

### Documentation Needs

- Agent development tutorials
- Constitutional principle explanations
- Deployment guides for different environments
- API usage examples with trust scoring

## 🔍 Issue Reporting

### Bug Reports

Use the **Constitutional Violation** template for:
- Constitutional framework bypasses
- Trust system manipulation attempts
- Information sovereignty violations
- Agent behavior anomalies

Use the **Bug Report** template for:
- Technical functionality issues
- Documentation errors
- Deployment problems

### Feature Requests

Use the **Constitutional Review** template for:
- Governance framework enhancements
- Constitutional principle clarifications
- Trust system improvements

Use the **Feature Request** template for:
- New agent capabilities
- Infrastructure enhancements
- Developer experience improvements

## 🏛️ Governance Participation

### DAO Membership

Earn governance participation through constitutional contributions:

- **Proposal Rights**: Trust T2+ (Confidential level)
- **Voting Power**: Proportional to infrastructure contribution
- **Constitutional Amendments**: Human oversight + community supermajority

### Governance Channels

- **Discord**: Real-time constitutional AI discussions
- **GitHub Discussions**: Long-form governance proposals
- **Community Calls**: Weekly constitutional governance reviews
- **DAO Platform**: Formal voting on constitutional matters

## 🛡️ Security & Constitutional Compliance

### Reporting Constitutional Violations

If you discover attempts to bypass constitutional governance:

1. **Do not disclose publicly** - report privately
2. **Email**: `governance@cuttlefishlabs.com`
3. **Include**: Detailed description, evidence, impact assessment
4. **Response**: 24-48 hours for constitutional violations

### Security Vulnerability Reporting

For technical security issues:

1. **Email**: `security@cuttlefishlabs.com` 
2. **Include**: Reproduction steps, impact assessment
3. **Response**: We will acknowledge within 48 hours

## 📜 Code of Conduct

The Constitutional Framework serves as our code of conduct. Key principles:

- **Respect Human Sovereignty** - Never manipulate or bypass human decision-making
- **Honor Trust Relationships** - Build and maintain trust through honest behavior
- **Transparent Governance** - All constitutional decisions are public and auditable
- **No Fabrication** - Report accurate progress and honest failures
- **Sustainable Development** - Balance economic, social, and ecological impacts

## 📞 Getting Help

### Community Support

- **Discord Server**: [Cuttlefish Labs Discord](https://discord.gg/cuttlefishlabs)
- **GitHub Discussions**: Repository discussions tab
- **Documentation**: [docs.cuttlefishlabs.com](https://docs.cuttlefishlabs.com)

### Direct Contact

- **General Questions**: `hello@cuttlefishlabs.com`
- **Governance Issues**: `governance@cuttlefishlabs.com`
- **Technical Support**: `dev@cuttlefishlabs.com`

## 🏆 Recognition

Constitutional contributors are recognized through:

- **Trust Score Advancement** - Proven through verified contributions
- **DAO Governance Rights** - Earned participation in constitutional decisions  
- **Agent Naming Rights** - Name constitutional agents you develop
- **Constitutional Credits** - Recognition in governance documentation

## 📄 License Compliance

By contributing, you agree that:

- Your contributions will be licensed under the MIT License with Constitutional Governance Requirements
- You understand that constitutional governance cannot be waived or bypassed
- Your contributions respect information sovereignty (T0-T3 classification)
- You will not attempt to manipulate or circumvent trust systems

---

## 🦑 Constitutional Status: ACTIVE AND IMMUTABLE

**Remember**: The Constitutional Framework is supreme and immutable. All contributions must enhance constitutional governance, never weaken it.

**Building sustainable human-AI civilization through constitutional governance.**

Thank you for contributing to the future of constitutional AI! 🏛️