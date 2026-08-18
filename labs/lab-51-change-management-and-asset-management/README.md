# Lab 51 — Change Management and Asset Management

> **Course:** CompTIA Certified A+ Training (Core 1 and Core 2) (TGS-2024048317)  
> **Topic 09:** Operational Procedures — Core 2, 21% of Core 2  
> **Exam objective:** Prepare a change request with risk analysis, rollback plan and approval path, and maintain an asset register through the procurement life cycle (Core 2 objectives 4.2 and 4.1).

## Goal

Change management is what stops a well-intentioned fix becoming an outage. You prepare a complete change request for a real change, then build the asset register that tells you what you actually own before you change any of it.

## What you'll produce

A complete change request with risk analysis and rollback plan, plus an asset register covering the procurement life cycle.

## Tools and equipment

Change request template, asset register template, organisational policy reference

## Safety

- Disconnect mains power and hold the power button for 15 seconds before working inside any machine.
- Wear an anti-static strap connected to an earthed point; hold boards and cards by their edges.
- **Never open a power supply unit or a CRT monitor** — both retain a lethal charge after being unplugged.
- Never puncture, compress or charge a swollen lithium battery; isolate it and follow hazardous disposal procedure.

## Step-by-step

1. List the required change request fields: purpose, scope, affected systems and users, risk analysis, risk level, change plan, rollback plan, scheduled date and time, approval and post-change review.
2. Write the purpose for the change scenario: deploying a critical security patch to 50 workstations after a vulnerability disclosure.
3. Define the scope precisely, naming which systems and users are affected and, equally importantly, which are explicitly out of scope.
4. Perform the risk analysis: what could go wrong, how likely it is, what the impact would be, and what mitigation reduces it. Assign an overall risk level with justification.
5. Record why sandbox testing precedes production: a patch validated on a representative test machine catches the incompatibility before it reaches 50 users.
6. Write the rollback plan with specific steps, and record the rule that a change with no viable rollback needs a much stronger justification to proceed.
7. Schedule the change in a maintenance window that minimises business impact, and state who must be notified and how far in advance.
8. Identify the approver and record why the person implementing a change should not be the person approving it.
9. Define the post-change review: how you confirm success, how long you monitor, and what condition would trigger the rollback.
10. Build the asset register with columns for asset tag, type, make and model, serial number, assigned user, location, purchase date, warranty expiry and licence status.
11. Record the procurement life cycle stages: requisition, approval, purchase, receipt and tagging, deployment, maintenance, and end-of-life disposal.
12. Record why asset tags and barcodes matter operationally: they make audit possible, they support warranty claims, and they identify a device recovered after loss or theft.

## Test it — verification

Your change request contains all ten fields with a risk level that is justified rather than asserted; the rollback plan has specific steps; the approver is separate from the implementer; and the asset register covers all seven life cycle stages.

## Troubleshooting this lab

| Symptom | What to check |
| --- | --- |
| A command returns "command not found" | Re-run the `apt-get install` step at the start of the lab — the playground starts with a minimal package set. |
| The Killercoda terminal has reset | The playground times out when idle. Reopen it and re-run the setup commands from step 1. |
| A browser tool will not load | Check the URL against `labs/tools.md`. All four tools run entirely client-side and need no login. |
| Output differs from the guide | Record what you actually observed — your environment differs from the reference, and explaining the difference is part of the exercise. |

## Review questions

1. State the exam objective this lab maps to, in your own words.
2. Which single step in this lab would you perform first on a real support call, and why?
3. What evidence would you attach to a support ticket to show this work was completed correctly?
4. Name one thing that would make this procedure fail, and how you would recognise it.

## Record your evidence

Complete [worksheet.md](worksheet.md) as you work through this lab and keep it — the Practical Performance assessment mirrors these tasks.

---

[← Labs index](../README.md)  ·  [Learner Guide](../../LG-CompTIA-Certified-A-Training-Core-1-and-Core-2.md)  ·  [Course page](https://www.tertiarycourses.com.sg/wsq-comptia-certified-a-training-core-1-and-core-2.html)
