# Lab 23 — POST, Boot and Power Fault Diagnosis

> **Course:** CompTIA Certified A+ Training (Core 1 and Core 2) (TGS-2024048317)  
> **Topic 05:** Hardware and Network Troubleshooting — Core 1, 28% of Core 1  
> **Exam objective:** Diagnose no-power, no-POST and no-boot faults using beep codes, diagnostic LEDs and a systematic elimination sequence (Core 1 objective 5.2).

## Goal

A machine that will not start gives you almost no information, so you need a fixed elimination sequence rather than guesswork. You build that sequence, learn to read the signals the board does give — beep codes and LEDs — and separate the three distinct failure classes.

## What you'll produce

A three-branch diagnostic flowchart for no-power, no-POST and no-boot, plus a beep code and LED reference.

## Tools and equipment

Training PC, motherboard manual, POST diagnostic references, PSU tester or multimeter

## Safety

- Disconnect mains power and hold the power button for 15 seconds before working inside any machine.
- Wear an anti-static strap connected to an earthed point; hold boards and cards by their edges.
- **Never open a power supply unit or a CRT monitor** — both retain a lethal charge after being unplugged.
- Never puncture, compress or charge a swollen lithium battery; isolate it and follow hazardous disposal procedure.

## Step-by-step

1. Separate the three failure classes precisely, because they have different causes: no power means nothing happens at all, no POST means fans spin but nothing appears on screen, and no boot means POST completes but the OS does not load.
2. Build the no-power branch: check the wall socket and the mains lead, check the PSU switch, check the case power switch header, test or substitute the PSU, then suspect the motherboard.
3. Build the no-POST branch: listen for beep codes, read diagnostic LEDs or the POST code display, reseat RAM, reseat the graphics card, disconnect all non-essential devices, then clear CMOS.
4. Record the beep code principle: patterns are manufacturer-specific and must be read from that board's manual, but a repeating pattern most commonly indicates RAM or graphics.
5. Record the reseating principle: reseating RAM and expansion cards costs nothing and resolves a large share of no-POST faults caused by vibration, thermal cycling or transport.
6. Build the no-boot branch: check the boot order, remove any bootable USB device, confirm the drive is detected in firmware, then repair the boot record from the recovery environment.
7. Record the minimum configuration test: strip the system to CPU, one RAM stick, integrated graphics and the PSU. If it POSTs, add components back one at a time until the fault returns.
8. Map the remaining hardware symptoms to causes: a burning smell means shut down and unplug immediately, a grinding noise means a failing fan or drive, and capacitor swelling means the board must be replaced.
9. Record that an inaccurate system date and time that resets on every boot means the CMOS battery is dead, and that this is a two-dollar part rather than a board fault.
10. Record the intermittent shutdown checklist: overheating, a failing PSU, a loose power connector, or a short from a misplaced standoff behind the board.
11. Record the sluggish performance checklist: insufficient RAM, a failing or nearly full disk, thermal throttling, malware, or too many startup applications.
12. Assemble the three branches into one flowchart with a clear entry question that routes a technician to the correct branch within two questions.

## Test it — verification

Your flowchart routes to the correct branch from the entry symptom in no more than two questions, each branch orders its checks from cheapest and least invasive to most, and the minimum configuration test is included in the no-POST branch.

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
