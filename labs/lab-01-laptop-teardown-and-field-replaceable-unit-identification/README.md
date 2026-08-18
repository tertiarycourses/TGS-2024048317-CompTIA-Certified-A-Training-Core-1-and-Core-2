# Lab 1 — Laptop Teardown and Field-Replaceable Unit Identification

> **Course:** CompTIA Certified A+ Training (Core 1 and Core 2) (TGS-2024048317)  
> **Topic 01:** Mobile Devices — Core 1, 13% of Core 1  
> **Exam objective:** Identify and safely replace laptop field-replaceable units — battery, RAM, storage, keyboard and wireless card — with correct ESD precautions (Core 1 objective 1.1).

## Goal

Working on a training laptop or a high-resolution teardown reference, you identify every field-replaceable unit, record the removal order, and document the anti-static precautions each step requires. You then build a replacement runbook a colleague could follow without supervision.

## What you'll produce

A completed FRU inventory table and a written replacement runbook for one component, with ESD precautions stated at every step.

## Tools and equipment

Training laptop or teardown reference, anti-static strap and mat, Phillips #00 screwdriver, plastic spudger, parts tray

## Safety

- Disconnect mains power and hold the power button for 15 seconds before working inside any machine.
- Wear an anti-static strap connected to an earthed point; hold boards and cards by their edges.
- **Never open a power supply unit or a CRT monitor** — both retain a lethal charge after being unplugged.
- Never puncture, compress or charge a swollen lithium battery; isolate it and follow hazardous disposal procedure.

## Step-by-step

1. Put on the anti-static strap and clip it to an unpainted metal point on the chassis. Confirm the mat is earthed before you touch any component.
2. Shut the laptop down completely — not sleep or hibernate — then disconnect the AC adapter and remove the external battery if the model has one.
3. Press and hold the power button for 15 seconds to drain residual charge from the capacitors before opening the case.
4. Remove the bottom cover screws into a parts tray, laying them out in the same pattern as the chassis so each screw returns to its own hole.
5. Locate and photograph each field-replaceable unit: battery, SODIMM slots, M.2 or 2.5-inch storage, wireless card, cooling fan and keyboard ribbon connector.
6. Disconnect the internal battery connector FIRST — before any other component — so the board is fully de-energised for the rest of the work.
7. Record for each FRU in your inventory table: component name, form factor, connector or socket type, removal order position, and the specific ESD or safety risk.
8. Note the two antenna leads on the wireless card and which is main and which is auxiliary, then photograph their routing before disturbing them.
9. Reassemble in exact reverse order, reconnecting the internal battery connector LAST, and confirm every screw is returned to its original hole.
10. Write a replacement runbook for one FRU of your choice with numbered steps, required tools, ESD precautions and a post-replacement verification test.

## Test it — verification

Your FRU inventory lists at least six components with form factor and socket type; the runbook states the internal battery is disconnected first and reconnected last; and the laptop powers on and completes POST after reassembly.

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
