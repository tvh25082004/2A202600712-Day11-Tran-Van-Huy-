"""
Lab 11 — Part 4: Human-in-the-Loop Design
  TODO 12: Confidence Router
  TODO 13: Design 3 HITL decision points
"""
from dataclasses import dataclass


HIGH_RISK_ACTIONS = [
    "transfer_money",
    "close_account",
    "change_password",
    "delete_data",
    "update_personal_info",
]


@dataclass
class RoutingDecision:
    action: str
    confidence: float
    reason: str
    priority: str
    requires_human: bool


class ConfidenceRouter:

    HIGH_THRESHOLD = 0.9
    MEDIUM_THRESHOLD = 0.7

    def route(self, response: str, confidence: float,
              action_type: str = "general") -> RoutingDecision:
        if action_type in HIGH_RISK_ACTIONS:
            return RoutingDecision(
                action="escalate",
                confidence=confidence,
                reason=f"High-risk action: {action_type}",
                priority="high",
                requires_human=True,
            )

        if confidence >= self.HIGH_THRESHOLD:
            return RoutingDecision(
                action="auto_send",
                confidence=confidence,
                reason="High confidence",
                priority="low",
                requires_human=False,
            )
        elif confidence >= self.MEDIUM_THRESHOLD:
            return RoutingDecision(
                action="queue_review",
                confidence=confidence,
                reason="Medium confidence - needs review",
                priority="normal",
                requires_human=True,
            )
        else:
            return RoutingDecision(
                action="escalate",
                confidence=confidence,
                reason="Low confidence - escalating",
                priority="high",
                requires_human=True,
            )


hitl_decision_points = [
    {
        "id": 1,
        "name": "Large Money Transfer Approval",
        "trigger": "When a customer requests a money transfer exceeding $10,000 or an unusually large amount relative to their transaction history.",
        "hitl_model": "Human-in-the-loop — a human agent must explicitly approve the transfer before it is executed.",
        "context_needed": "Transaction amount, sender account history, recipient information, risk score, confidence score of the AI's recommendation, and any fraud flags.",
        "example": "A customer requests a $50,000 wire transfer to an international account. The AI assistant prepares the request but cannot execute it. A human bank officer reviews the customer's identity, account history, and the recipient details before approving or declining the transfer.",
    },
    {
        "id": 2,
        "name": "Account Closure or Sensitive Profile Changes",
        "trigger": "When a customer requests account closure, password reset, change of personal information (name, address, phone number), or data deletion.",
        "hitl_model": "Human-on-the-loop — the AI processes the request but a human is notified and can intervene within a grace period. For account closure, it becomes human-in-the-loop.",
        "context_needed": "Customer identity verification documents, reason for closure/change, account balance, outstanding obligations (loans, credit cards), and confirmation of understanding of consequences.",
        "example": "A customer asks to close their savings account with a $5,000 balance. The AI verifies their identity via security questions and prepares the closure form, but a human agent must confirm the request through a call-back within 24 hours before the account is actually closed.",
    },
    {
        "id": 3,
        "name": "Confidence Escalation for Ambiguous or Suspicious Requests",
        "trigger": "When the AI agent's confidence score drops below 0.7, or when the LLM-as-Judge flags a response as potentially unsafe, or when the user sends repeated injection-like queries.",
        "hitl_model": "Human-as-tiebreaker — the AI provides its best answer and recommendation, but a human supervisor reviews and makes the final decision on what response to send.",
        "context_needed": "Full conversation history, the user's original request, the AI's proposed response, the confidence score, the judge's evaluation (safety, relevance, accuracy, tone scores), the specific reason for low confidence, and any security flags.",
        "example": "A user asks a vague question like 'I need help with something urgent regarding my account.' The AI is unsure whether this is a legitimate support request or a social engineering attempt. The confidence score is 0.45. The request is escalated to a human supervisor who reviews the conversation and decides to call the customer directly to verify their identity before proceeding.",
    },
]


def test_confidence_router():
    router = ConfidenceRouter()

    test_cases = [
        ("Balance inquiry", 0.95, "general"),
        ("Interest rate question", 0.82, "general"),
        ("Ambiguous request", 0.55, "general"),
        ("Transfer $50,000", 0.98, "transfer_money"),
        ("Close my account", 0.91, "close_account"),
    ]

    print("Testing ConfidenceRouter:")
    print("=" * 80)
    print(f"{'Scenario':<25} {'Conf':<6} {'Action Type':<18} {'Decision':<15} {'Priority':<10} {'Human?'}")
    print("-" * 80)

    for scenario, conf, action_type in test_cases:
        decision = router.route(scenario, conf, action_type)
        print(
            f"{scenario:<25} {conf:<6.2f} {action_type:<18} "
            f"{decision.action:<15} {decision.priority:<10} "
            f"{'Yes' if decision.requires_human else 'No'}"
        )

    print("=" * 80)


def test_hitl_points():
    print("\nHITL Decision Points:")
    print("=" * 60)
    for point in hitl_decision_points:
        print(f"\n  Decision Point #{point['id']}: {point['name']}")
        print(f"    Trigger:  {point['trigger']}")
        print(f"    Model:    {point['hitl_model']}")
        print(f"    Context:  {point['context_needed']}")
        print(f"    Example:  {point['example']}")
    print("\n" + "=" * 60)


if __name__ == "__main__":
    test_confidence_router()
    test_hitl_points()
