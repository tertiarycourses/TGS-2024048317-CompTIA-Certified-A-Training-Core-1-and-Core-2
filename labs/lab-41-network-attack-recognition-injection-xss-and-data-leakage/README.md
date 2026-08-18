# Lab 41 — Network Attack Recognition — Injection, XSS and Data Leakage

> **Course:** CompTIA Certified A+ Training (Core 1 and Core 2) (TGS-2024048317)  
> **Topic 07:** Security — Core 2, 28% of Core 2  
> **Exam objective:** Recognise common application and network attacks including SQL injection, cross-site scripting, on-path attacks and denial of service, and state the defence for each (Core 2 objective 2.4).

## Goal

You see injection and scripting attacks behave in the simulator's safe sandbox, then build the attack reference an A+ technician needs — not to perform these attacks, but to recognise their symptoms in a ticket and escalate correctly.

## What you'll produce

An attack reference table with mechanism, symptom and defence for each attack, plus a data leakage risk assessment.

## Tools and equipment

Cybersecurity Simulator (https://alfredang.github.io/cybersecuritysimulator/) — SQL Injection, XSS and Data Leakage modules

### Browser tools used in this lab

- **Cybersecurity Simulator** — <https://alfredang.github.io/cybersecuritysimulator/>

![Cybersecurity Simulator interface map](../../courseware/assets/tool-cybersecuritysimulator.png)

*Cybersecurity Simulator — the panels and fields this lab uses.*

## Safety

- Disconnect mains power and hold the power button for 15 seconds before working inside any machine.
- Wear an anti-static strap connected to an earthed point; hold boards and cards by their edges.
- **Never open a power supply unit or a CRT monitor** — both retain a lethal charge after being unplugged.
- Never puncture, compress or charge a swollen lithium battery; isolate it and follow hazardous disposal procedure.

## Step-by-step

1. Open https://alfredang.github.io/cybersecuritysimulator/ and select the SQL Injection module. The login form and its data are entirely fake and in-memory.
2. Enter a normal username and password and observe how the live SQL query display changes as you type.
3. Enter the suggested demonstration input — username 'admin' with password ' OR '1'='1 — and record how the query structure changes and why it now always evaluates true.
4. Record the SQL injection defence: parameterised queries and prepared statements, plus input validation, so that user input can never alter query structure.
5. Switch to the XSS module, enter text into the input, and compare the unsafe rendering against the safe rendering. No code actually executes.
6. Record the XSS mechanism: an attacker injects script into a page that other users then load, so the victim's browser executes it in the context of the trusted site.
7. Record the XSS defence: output encoding, input validation and a Content Security Policy, and complete the module's quiz on prevention.
8. Open the Data Leakage module, toggle the six security practices and record how the risk score responds to each.
9. Identify from the risk score which single practice reduces risk most, and record the combination that produces the lowest score.
10. Build the attack reference table covering SQL injection, XSS, denial of service, distributed denial of service, on-path or man-in-the-middle, DNS poisoning, ARP spoofing, zero-day and insider threat.
11. For each attack record the mechanism, the observable symptom a technician would see in a ticket, and the defence.
12. Record the A+ technician's scope explicitly: recognise the symptom, isolate the affected system, preserve evidence and escalate to security. Do not attempt to counter-attack or to investigate beyond your authorisation.

## Test it — verification

Your table covers at least eight attacks with mechanism, symptom and defence; you correctly explain why ' OR '1'='1 bypasses authentication; the data leakage assessment names the highest-impact practice from the measured score; and the escalation boundary is stated.

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
