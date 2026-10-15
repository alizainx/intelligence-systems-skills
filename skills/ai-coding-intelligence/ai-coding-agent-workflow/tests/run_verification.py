#!/usr/bin/env python3
"""
Verifies the Mandatory 7-Stage AI Coding Agent Discipline State Machine:
UNDERSTAND -> PLAN -> IMPLEMENT -> COMPILE -> TEST -> VERIFY -> REVIEW
Forbids declaring a task COMPLETE if COMPILE, TEST, or VERIFY was skipped or failed!
"""
MANDATORY_STAGES = ("UNDERSTAND", "PLAN", "IMPLEMENT", "COMPILE", "TEST", "VERIFY", "REVIEW")

class CodingWorkflowGate:
    def __init__(self) -> None:
        self.completed_stages: list[str] = []
        self.stage_evidence: dict[str, str] = {}

    def record_stage(self, stage: str, passed: bool, evidence_log: str) -> None:
        if stage not in MANDATORY_STAGES:
            raise ValueError(f"Unknown stage: {stage}")
        expected_idx = len(self.completed_stages)
        if MANDATORY_STAGES[expected_idx] != stage:
            raise RuntimeError(f"Workflow order violation: expected {MANDATORY_STAGES[expected_idx]}, got {stage}")
        if not passed or not evidence_log.strip():
            raise RuntimeError(f"Stage {stage} failed or lacked tool execution evidence")
        self.completed_stages.append(stage)
        self.stage_evidence[stage] = evidence_log

    def can_declare_complete(self) -> bool:
        return tuple(self.completed_stages) == MANDATORY_STAGES

wf = CodingWorkflowGate()
for st in MANDATORY_STAGES[:3]:
    wf.record_stage(st, True, f"{st} done")
assert not wf.can_declare_complete()  # Cannot stop after IMPLEMENT without COMPILE, TEST, VERIFY, REVIEW!

skipped_caught = False
try:
    wf.record_stage("REVIEW", True, "skipped compile and test")
except RuntimeError:
    skipped_caught = True
assert skipped_caught

for st in MANDATORY_STAGES[3:]:
    wf.record_stage(st, True, f"{st} exit=0")
assert wf.can_declare_complete()
print("AI CODING AGENT 7-STAGE WORKFLOW GATE (UNDERSTAND->...->REVIEW) VERIFIED")
