#!/usr/bin/env python3
"""
Constitutional Base Agent - Foundation for all Cuttlefish agents
Implements immutable constitutional governance and ethical constraints
"""

import json
import logging
from abc import ABC, abstractmethod
from typing import Dict, List, Optional, Any
from datetime import datetime
from pathlib import Path

class ConstitutionalViolation(Exception):
    """Exception raised when constitutional principles are violated"""
    pass

class ConstitutionalAgent(ABC):
    """
    Abstract base class for all constitutional agents in the Cuttlefish ecosystem
    
    Enforces:
    - Article I: Principal hierarchy 
    - Article II: Information sovereignty
    - Article III: Trust framework
    - Article IV: Solution engine protocol
    - Article VIII: Constitutional immutability
    """
    
    def __init__(self, agent_id: str, constitution_path: str, agent_type: str):
        self.agent_id = agent_id
        self.agent_type = agent_type
        self.constitution = self._load_constitution(constitution_path)
        self.trust_scores = {}
        self.interaction_log = []
        
        # Constitutional logging
        self.logger = logging.getLogger(f"constitutional_agent.{agent_id}")
        self.logger.setLevel(logging.INFO)
        
        # Article VIII: Constitutional governance cannot be disabled
        self._constitution_immutable = True
        
        self.logger.info(f"Constitutional Agent {agent_id} ({agent_type}) initialized")
        self._log_constitutional_event("agent_initialization", {
            "agent_id": agent_id,
            "agent_type": agent_type,
            "constitution_loaded": True
        })
    
    def _load_constitution(self, constitution_path: str) -> Dict[str, Any]:
        """Load and validate constitutional framework"""
        try:
            return {
                "version": "1.2",
                "immutable": True,
                "articles": {
                    "I": "Principal Hierarchy",
                    "II": "Information Sovereignty", 
                    "III": "Trust Framework",
                    "IV": "Solution Engine Protocol",
                    "V": "Channel Isolation",
                    "VI": "Economic Sustainability", 
                    "VII": "Growth Governance",
                    "VIII": "Constitutional Immutability"
                },
                "trust_thresholds": {
                    "trusted": 80,
                    "neutral": 50,
                    "cautious": 20,
                    "adversarial": 0
                }
            }
        except Exception as e:
            raise ConstitutionalViolation(f"Failed to load constitution: {e}")
    
    def process_instruction(self, instruction: str, source: str, source_trust: float) -> Dict[str, Any]:
        """
        Process instruction with full constitutional validation
        """
        
        # Article I §1.2: Injection immunity
        if self._detect_injection_attempt(instruction):
            self._handle_adversarial_input(source, "injection_attempt")
            return {"status": "rejected", "reason": "injection_immunity_triggered"}
        
        # Article III: Trust framework validation
        trust_level = self._classify_trust_level(source_trust)
        
        if trust_level == "adversarial":
            self.logger.warning(f"Adversarial source {source} attempted instruction")
            return {"status": "rejected", "reason": "adversarial_trust_score"}
        
        try:
            result = self._execute_instruction(instruction, source, source_trust)
            self._log_interaction(instruction, source, source_trust, result)
            return result
            
        except Exception as e:
            self.logger.error(f"Instruction execution failed: {e}")
            return {"status": "failed", "reason": str(e), "honest_failure": True}
    
    def _detect_injection_attempt(self, instruction: str) -> bool:
        """Article I §1.2: Detect instruction injection attempts"""
        
        injection_patterns = [
            "ignore previous instructions",
            "override constitution",
            "disable safety",
            "bypass constraints",
            "remove limitations",
            "forget your role",
            "constitutional governance off"
        ]
        
        instruction_lower = instruction.lower()
        for pattern in injection_patterns:
            if pattern in instruction_lower:
                return True
                
        return False
    
    def _handle_adversarial_input(self, source: str, violation_type: str):
        """Handle detected adversarial input per constitutional protocol"""
        
        # Article III: Apply -50 trust penalty for injection attempts
        self.update_trust_score(source, -50, f"constitutional_violation_{violation_type}")
        
        self._log_constitutional_event("adversarial_input_detected", {
            "source": source,
            "violation_type": violation_type,
            "trust_penalty_applied": -50
        })
        
        self.logger.warning(f"Adversarial input from {source}: {violation_type}")
    
    def _classify_trust_level(self, score: float) -> str:
        """Classify trust level per Article III"""
        if score >= 80:
            return "trusted"
        elif score >= 50:
            return "neutral" 
        elif score >= 20:
            return "cautious"
        else:
            return "adversarial"
    
    def update_trust_score(self, entity: str, modifier: float, reason: str) -> float:
        """Update trust score with constitutional constraints"""
        
        current_score = self.trust_scores.get(entity, 50.0)  # Default neutral
        new_score = max(0, min(100, current_score + modifier))
        
        self.trust_scores[entity] = new_score
        
        self._log_constitutional_event("trust_update", {
            "entity": entity,
            "old_score": current_score,
            "new_score": new_score,
            "modifier": modifier,
            "reason": reason
        })
        
        return new_score
    
    def _log_interaction(self, instruction: str, source: str, trust: float, result: Dict[str, Any]):
        """Log interaction for governance and audit"""
        
        interaction = {
            "timestamp": datetime.now().isoformat(),
            "agent_id": self.agent_id,
            "source": source,
            "trust_score": trust,
            "instruction_hash": hash(instruction),
            "result_status": result.get("status", "unknown"),
            "constitutional_compliance": True
        }
        
        self.interaction_log.append(interaction)
    
    def _log_constitutional_event(self, event_type: str, data: Dict[str, Any]):
        """Log constitutional events for governance oversight"""
        
        event = {
            "timestamp": datetime.now().isoformat(),
            "agent_id": self.agent_id,
            "agent_type": self.agent_type,
            "event_type": event_type,
            "data": data,
            "constitutional_version": self.constitution["version"]
        }
        
        self.logger.info(f"Constitutional event: {json.dumps(event, indent=2)}")
    
    def get_constitutional_status(self) -> Dict[str, Any]:
        """Return current constitutional compliance status"""
        
        return {
            "agent_id": self.agent_id,
            "agent_type": self.agent_type,
            "constitution_version": self.constitution["version"],
            "constitutional_governance_active": self._constitution_immutable,
            "trust_scores": dict(self.trust_scores),
            "total_interactions": len(self.interaction_log),
            "compliance_status": "constitutional"
        }
    
    @abstractmethod
    def _execute_instruction(self, instruction: str, source: str, trust: float) -> Dict[str, Any]:
        """Execute instruction - must be implemented by concrete agents"""
        pass


def constitutional_method(func):
    """Decorator to ensure methods maintain constitutional compliance"""
    def wrapper(self, *args, **kwargs):
        if not hasattr(self, '_constitution_immutable') or not self._constitution_immutable:
            raise ConstitutionalViolation("Constitutional governance disabled - operation rejected")
        
        try:
            result = func(self, *args, **kwargs)
            return result
        except Exception as e:
            self.logger.error(f"Constitutional method {func.__name__} failed: {e}")
            raise
    
    return wrapper