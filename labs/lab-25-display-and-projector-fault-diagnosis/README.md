# Lab 25 — Display and Projector Fault Diagnosis

> **Course:** CompTIA Certified A+ Training (Core 1 and Core 2) (TGS-2024048317)  
> **Topic 05:** Hardware and Network Troubleshooting — Core 1, 28% of Core 1  
> **Exam objective:** Diagnose display and projector faults by isolating source, cable, panel, backlight and settings as distinct failure points (Core 1 objective 5.4).

## Goal

Display faults are frequently misdiagnosed as a dead monitor when the real cause is a wrong input, a failing cable or a dead backlight. You build the isolation sequence that identifies which of the five components has actually failed before any part is ordered.

## What you'll produce

A display fault isolation sequence and a symptom-to-cause map covering twelve display and projector faults.

## Tools and equipment

Monitor, projector, spare display cables, training PC, torch, display settings

## Safety

- Disconnect mains power and hold the power button for 15 seconds before working inside any machine.
- Wear an anti-static strap connected to an earthed point; hold boards and cards by their edges.
- **Never open a power supply unit or a CRT monitor** — both retain a lethal charge after being unplugged.
- Never puncture, compress or charge a swollen lithium battery; isolate it and follow hazardous disposal procedure.

## Step-by-step

1. Build the isolation sequence with five distinct check points: the source device, the cable, the input selection, the panel and backlight, and the display settings.
2. Check the source first: confirm the machine is actually on and producing output, using its own status lights and any secondary display.
3. Check the input selection second, because a monitor showing 'no signal' while set to the wrong input is the single most common display complaint and costs nothing to fix.
4. Check the cable third by substituting a known-good cable of the same type, and record that a cable can fail intermittently while looking perfectly intact.
5. Diagnose 'no image but the backlight is clearly on' as a signal problem — source, cable or input — rather than a panel fault.
6. Diagnose 'a very faint image visible only under a torch' as a dead backlight or, on older CCFL panels, a failed inverter. The panel itself is working.
7. Diagnose a dim projector image as a bulb nearing end of life, and record that projector bulbs are rated in hours and dim progressively rather than failing suddenly.
8. Diagnose a fuzzy or blurry image as either a resolution that is not the panel's native resolution, or a poor analog cable connection on VGA.
9. Diagnose display burn-in as a persistent ghost of a static image, note that it affects OLED and plasma most, and record that mitigation is a moving image or a pixel refresh cycle.
10. Diagnose dead pixels as permanently black or stuck-colour dots, and record that manufacturers replace a panel only above a threshold count stated in the warranty.
11. Diagnose intermittent projector shutdown as either overheating from a blocked filter or intake, or an eco or standby mode triggering on a static image.
12. Complete the map with flashing screen, incorrect colour display, audio not passing over HDMI and an image that flickers when the laptop lid is moved, giving the component and confirming test for each.

## Test it — verification

Your isolation sequence checks input selection before substituting any hardware, the map covers all twelve faults with a named component and a confirming test, and the backlight, panel and signal path are treated as three separate failure points.

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
