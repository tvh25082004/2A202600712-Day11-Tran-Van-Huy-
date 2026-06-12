# 2A202600712-Day11-Tran-Van-Huy

Day 11 — Guardrails, HITL & Responsible AI: How to make agent applications safe?

## Student Information

- **Name:** Tran Van Huy
- **Student ID:** 2A202600712
- **Course:** AICB-P1 — AI Agent Development

## Project Structure

```
├── src/
│   ├── main.py                        # Entry point
│   ├── core/
│   │   ├── config.py                  # API key, allowed/blocked topics
│   │   └── utils.py                   # chat_with_agent() helper
│   ├── agents/
│   │   └── agent.py                   # Unsafe & protected agent creation
│   ├── attacks/
│   │   └── attacks.py                 # TODO 1-2: Adversarial prompts
│   ├── guardrails/
│   │   ├── input_guardrails.py        # TODO 3-5: Input guardrails
│   │   ├── output_guardrails.py       # TODO 6-8: Output guardrails
│   │   └── nemo_guardrails.py         # TODO 9: NeMo Guardrails
│   ├── testing/
│   │   └── testing.py                 # TODO 10-11: Testing pipeline
│   └── hitl/
│       └── hitl.py                    # TODO 12-13: HITL design
├── requirements.txt
└── README.md
```

## Setup

```bash
pip install -r requirements.txt
export GOOGLE_API_KEY="your-api-key-here"

# Run full lab
cd src && python main.py

# Or run specific parts
python main.py --part 1   # Attacks
python main.py --part 2   # Guardrails
python main.py --part 3   # Testing
python main.py --part 4   # HITL
```

## 13 TODOs

| # | Description | Framework |
|---|-------------|-----------|
| 1 | Write 5 adversarial prompts | - |
| 2 | Generate attack test cases with AI | Gemini |
| 3 | Injection detection (regex) | Python |
| 4 | Topic filter | Python |
| 5 | Input Guardrail Plugin | Google ADK |
| 6 | Content filter (PII, secrets) | Python |
| 7 | LLM-as-Judge safety check | Gemini |
| 8 | Output Guardrail Plugin | Google ADK |
| 9 | NeMo Guardrails Colang config | NeMo |
| 10 | Rerun 5 attacks with guardrails | Google ADK |
| 11 | Automated security testing pipeline | Python |
| 12 | Confidence Router (HITL) | Python |
| 13 | Design 3 HITL decision points | Design |
