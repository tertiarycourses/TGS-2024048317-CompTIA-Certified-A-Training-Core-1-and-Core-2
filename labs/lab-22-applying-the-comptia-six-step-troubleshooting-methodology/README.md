# Lab 22 — Applying the CompTIA Six-Step Troubleshooting Methodology

> **Course:** CompTIA Certified A+ Training (Core 1 and Core 2) (TGS-2024048317)  
> **Topic 05:** Hardware and Network Troubleshooting — Core 1, 28% of Core 1  
> **Exam objective:** Apply the CompTIA six-step troubleshooting methodology in order to a real fault, documenting each step (Core 1 objective 5.1).

## Goal

The methodology is examinable in order and is the framework every other troubleshooting lab in this course hangs from. You apply all six steps to a fault, writing the evidence at each step, and produce the documentation that step six actually requires.

## What you'll produce

A completed six-step troubleshooting record for one fault, with evidence and a preventive measure at each step.

## Tools and equipment

Training PC with an injected fault, ticketing template, Killercoda Ubuntu Playground

### Browser tools used in this lab

- **Killercoda Ubuntu Playground** — <https://killercoda.com/playgrounds/scenario/ubuntu>

![Killercoda Ubuntu Playground interface map](../../courseware/assets/tool-killercoda.png)

*Killercoda Ubuntu Playground — the panels and fields this lab uses.*

## Safety

- Disconnect mains power and hold the power button for 15 seconds before working inside any machine.
- Wear an anti-static strap connected to an earthed point; hold boards and cards by their edges.
- **Never open a power supply unit or a CRT monitor** — both retain a lethal charge after being unplugged.
- Never puncture, compress or charge a swollen lithium battery; isolate it and follow hazardous disposal procedure.

## Step-by-step

1. Write the six steps in order before you start, because the order itself is examinable: identify the problem; establish a theory of probable cause; test the theory; establish a plan of action and implement it; verify full functionality and implement preventive measures; document findings, actions and outcomes.
2. Step 1 — identify the problem. Interview the user with open questions: what exactly happens, when did it start, what changed, and can you reproduce it on demand.
3. Step 1 continued — always ask what changed, because most faults follow a recent change: a new driver, an update, a moved cable or new software.
4. Step 1 continued — back up user data before making any change, so that your troubleshooting can never be the cause of data loss.
5. Step 2 — establish a theory of probable cause, questioning the obvious first and listing at least three candidate causes ranked by likelihood.
6. Step 3 — test the theory. Design a test that will disprove the theory if it is wrong, not merely one that confirms what you already believe.
7. Step 3 continued — if the theory is not confirmed, establish a new theory or escalate. Record that escalation is a legitimate step in the methodology, not a failure.
8. Step 4 — establish a plan of action, referring to vendor documentation, and state the rollback position before you implement anything.
9. Step 5 — verify full system functionality, testing not only the reported fault but the functions around it that your change might have affected.
10. Step 5 continued — implement preventive measures so the same fault does not recur, and state the specific measure you applied.
11. Step 6 — document findings, actions and outcomes in the ticket, in language a colleague could follow without speaking to you.
12. Practise the discipline on the Killercoda playground by diagnosing a deliberately broken DNS configuration through all six steps and recording your evidence.

   ```bash
   cp /etc/resolv.conf /root/resolv.backup && echo 'nameserver 192.0.2.1' > /etc/resolv.conf && (dig +short +time=2 +tries=1 google.com || echo 'STEP 1: resolution FAILS - symptom confirmed') && cp /root/resolv.backup /etc/resolv.conf && dig +short google.com
   ```


## Test it — verification

Your record contains all six steps in the correct order, each with written evidence; a rollback position is stated before implementation; a specific preventive measure is named; and the DNS exercise shows the fault reproduced and then resolved.

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
