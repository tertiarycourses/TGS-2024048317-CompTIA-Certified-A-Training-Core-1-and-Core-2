# Lab 17 — Power Supply Sizing, Connectors and Safety

> **Course:** CompTIA Certified A+ Training (Core 1 and Core 2) (TGS-2024048317)  
> **Topic 03:** Hardware — Core 1, 25% of Core 1  
> **Exam objective:** Select a power supply by wattage, form factor, efficiency and connector complement, and apply electrical safety rules when working with power (Core 1 objectives 3.5 and 4.5).

## Goal

You calculate the wattage a build actually requires, select a supply with the right connectors and headroom, and record the safety rules that apply. The safety section is not optional background — a power supply retains a lethal charge after disconnection.

## What you'll produce

A power budget calculation, a justified PSU selection with connector checklist, and a written electrical safety procedure.

## Tools and equipment

PSU samples or specification sheets, PSU wattage calculator, training PC, multimeter (demonstration only)

## Safety

- Disconnect mains power and hold the power button for 15 seconds before working inside any machine.
- Wear an anti-static strap connected to an earthed point; hold boards and cards by their edges.
- **Never open a power supply unit or a CRT monitor** — both retain a lethal charge after being unplugged.
- Never puncture, compress or charge a swollen lithium battery; isolate it and follow hazardous disposal procedure.

## Step-by-step

1. Record the absolute safety rule first: never open a power supply unit. Its capacitors hold a lethal charge long after it is unplugged, and there are no user-serviceable parts inside.
2. Record the second safety rule: disconnect the mains lead and hold the power button for 15 seconds before working inside any machine.
3. Build the power budget by listing each component with its typical and peak draw: CPU, GPU, motherboard, each drive, each fan and any PCIe card.
4. Sum the peak figures to get total system draw, then add 30 percent headroom for capacitor ageing, transient spikes and future upgrades.
5. Record the connector complement your build requires: 24-pin ATX for the board, 4 or 8-pin EPS for the CPU, 6 or 8-pin PCIe for the graphics card, SATA power for each drive and Molex for legacy devices.
6. Match the form factor to the case: ATX for standard and micro-ATX cases, SFX for Mini-ITX and small-form-factor builds.
7. Compare the 80 PLUS efficiency tiers from Bronze through Titanium, and explain that a higher tier wastes less power as heat and runs cooler and quieter.
8. Explain the difference between a modular, semi-modular and non-modular supply, and why modular improves airflow in a small case.
9. Record the standard voltage rails — plus 12 V, plus 5 V and plus 3.3 V — and note that the 12 V rail carries the CPU and GPU load and is the one that matters most.
10. Observe a demonstration of testing a supply with a multimeter or a PSU tester, and record the acceptable tolerance of plus or minus 5 percent on each rail.
11. List the symptoms of a failing power supply: no power at all, random shutdowns under load, a burning smell, a fan that does not spin and repeated POST failures.
12. Write the final selection with its wattage, form factor, efficiency tier and connector list, and justify the wattage against your calculated budget plus headroom.

## Test it — verification

Your power budget sums every component and adds stated headroom, the selected supply provides every connector the build requires, and the safety procedure explicitly forbids opening the PSU and requires discharge before internal work.

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
