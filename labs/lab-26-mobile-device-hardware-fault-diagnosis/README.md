# Lab 26 — Mobile Device Hardware Fault Diagnosis

> **Course:** CompTIA Certified A+ Training (Core 1 and Core 2) (TGS-2024048317)  
> **Topic 05:** Hardware and Network Troubleshooting — Core 1, 28% of Core 1  
> **Exam objective:** Diagnose mobile device hardware faults including battery, charging, screen, digitizer, port and overheating problems, applying the correct safety response (Core 1 objective 5.5).

## Goal

Mobile faults carry a safety dimension that desktop faults do not: a swollen lithium battery is a fire and chemical hazard. You build the diagnostic map and, for each fault, record both the technical response and the safety response.

## What you'll produce

A mobile fault diagnostic map with a technical and a safety response for each of ten faults.

## Tools and equipment

Mobile device, charging cables, battery health screens, device settings

## Safety

- Disconnect mains power and hold the power button for 15 seconds before working inside any machine.
- Wear an anti-static strap connected to an earthed point; hold boards and cards by their edges.
- **Never open a power supply unit or a CRT monitor** — both retain a lethal charge after being unplugged.
- Never puncture, compress or charge a swollen lithium battery; isolate it and follow hazardous disposal procedure.

## Step-by-step

1. Record the safety rule that governs this entire lab: a swollen battery must never be punctured, compressed or charged. Power the device down, isolate it from flammable material and follow the organisation's hazardous disposal procedure.
2. Check battery health from the device's own settings, recording the maximum capacity percentage and the cycle count where the operating system exposes them.
3. Diagnose poor battery life by separating its causes: a genuinely degraded battery, background applications, a weak cellular signal forcing the radio to full transmit power, or high screen brightness.
4. Diagnose a swollen battery from its physical signs — a lifting screen, a bulging back cover or a device that no longer sits flat — and apply the safety response immediately.
5. Diagnose improper or intermittent charging by testing in a fixed order: substitute the cable, substitute the charger, inspect the port for lint and damage, then suspect the battery.
6. Record that a charging port packed with pocket lint is extremely common and is cleared with a wooden or plastic pick on a powered-off device — never a metal tool.
7. Diagnose a broken screen by distinguishing cracked glass with a working display, a working digitizer with a dead display, and a working display with a dead digitizer.
8. Diagnose digitizer failure as touch that is unresponsive, offset from where you press, or registering phantom touches, while the image remains perfect.
9. Diagnose overheating from its causes: sustained high load, a faulty charging circuit, an ambient heat source, or a failing battery — and record that persistent overheating with a swollen battery is an immediate safety stop.
10. Diagnose liquid damage, record that the device must be powered off and not charged, and note that visible corrosion means board-level damage requiring specialist repair.
11. Diagnose physically damaged ports and record the repair options in order of cost: port replacement by a specialist, board replacement, or device replacement.
12. Complete the map with poor or no connectivity, cursor drift requiring touch recalibration, and malware symptoms, giving a technical and a safety response for each.

## Test it — verification

Every fault in your map has both a technical and a safety response; the swollen battery entry forbids puncturing, compressing and charging; and the charging diagnosis substitutes cable and charger before the battery is suspected.

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
