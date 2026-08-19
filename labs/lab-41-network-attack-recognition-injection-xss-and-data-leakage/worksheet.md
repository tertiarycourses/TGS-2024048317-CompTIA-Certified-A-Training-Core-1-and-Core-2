# Lab 41 Worksheet — Network Attack Recognition — Injection, XSS and Data Leakage

**Name:** ______________________    **Date:** ______________

**Exam objective:** Recognise common application and network attacks including SQL injection, cross-site scripting, on-path attacks and denial of service, and state the defence for each (Core 2 objective 2.4).

## Record as you go

| Step | What you did | What you observed |
| --- | --- | --- |
| 1 | Open https://alfredang.github.io/cybersecuritysimulator/ and select the SQL Injection module. The login form and its data are entirely fake and in-memory. |  |
| 2 | Enter a normal username and password and observe how the live SQL query display changes as you type. |  |
| 3 | Enter the suggested demonstration input — username 'admin' with password ' OR '1'='1 — and record how the query structure changes and why it now always evaluates true. |  |
| 4 | Record the SQL injection defence: parameterised queries and prepared statements, plus input validation, so that user input can never alter query structure. |  |
| 5 | Switch to the XSS module, enter text into the input, and compare the unsafe rendering against the safe rendering. No code actually executes. |  |
| 6 | Record the XSS mechanism: an attacker injects script into a page that other users then load, so the victim's browser executes it in the context of the trusted site. |  |
| 7 | Record the XSS defence: output encoding, input validation and a Content Security Policy, and complete the module's quiz on prevention. |  |
| 8 | Open the Data Leakage module, toggle the six security practices and record how the risk score responds to each. |  |
| 9 | Identify from the risk score which single practice reduces risk most, and record the combination that produces the lowest score. |  |
| 10 | Build the attack reference table covering SQL injection, XSS, denial of service, distributed denial of service, on-path or man-in-the-middle, DNS poisoning, ARP spoofing, zero-day and insider threat. |  |
| 11 | For each attack record the mechanism, the observable symptom a technician would see in a ticket, and the defence. |  |
| 12 | Record the A+ technician's scope explicitly: recognise the symptom, isolate the affected system, preserve evidence and escalate to security. Do not attempt to counter-attack or to investigate beyond your authorisation. |  |

## Verification

**Success criterion:** Your table covers at least eight attacks with mechanism, symptom and defence; you correctly explain why ' OR '1'='1 bypasses authentication; the data leakage assessment names the highest-impact practice from the measured score; and the escalation boundary is stated.

- [ ] I completed every step in the lab.
- [ ] My result meets the success criterion above.
- [ ] I recorded my evidence (screenshots, output, completed tables).

## Reflection

**What surprised you in this lab?**

_______________________________________________________________

**Where would you apply this on the job?**

_______________________________________________________________

**What do you still need to revise before the exam?**

_______________________________________________________________
