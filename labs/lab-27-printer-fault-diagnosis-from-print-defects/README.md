# Lab 27 — Printer Fault Diagnosis from Print Defects

> **Course:** CompTIA Certified A+ Training (Core 1 and Core 2) (TGS-2024048317)  
> **Topic 05:** Hardware and Network Troubleshooting — Core 1, 28% of Core 1  
> **Exam objective:** Diagnose printer faults by reading the physical defect on the page and mapping it to the failed component in the print process (Core 1 objective 5.6).

## Goal

A printed page is diagnostic evidence: the defect's pattern tells you which component failed and often where in the paper path. You build the defect-to-component map, then work through paper handling, connectivity and driver faults that produce no defect at all.

## What you'll produce

A print defect diagnostic map covering twelve defects, plus a paper-path and connectivity fault checklist.

## Tools and equipment

Laser and inkjet printers or reference defect images, maintenance kit reference, print management console

## Safety

- Disconnect mains power and hold the power button for 15 seconds before working inside any machine.
- Wear an anti-static strap connected to an earthed point; hold boards and cards by their edges.
- **Never open a power supply unit or a CRT monitor** — both retain a lethal charge after being unplugged.
- Never puncture, compress or charge a swollen lithium battery; isolate it and follow hazardous disposal procedure.

## Step-by-step

1. Record the diagnostic principle: the pattern of the defect identifies the component, and a repeating defect's spacing identifies which rotating part by its circumference.
2. Diagnose vertical lines running down every page on a laser printer as a scratched imaging drum, and record that the fix is drum or cartridge replacement.
3. Diagnose toner that smudges or wipes off the page as a failed fuser — the toner was placed correctly but never melted onto the paper.
4. Diagnose repeated ghost or echo images as a drum that is not being cleaned between cycles, and record that replacing the toner cartridge usually resolves it.
5. Diagnose faded print as low toner or ink, and record the field workaround of gently rocking a laser cartridge to redistribute remaining toner.
6. Diagnose garbled or nonsense output as the wrong print driver language — a PostScript driver sending to a PCL-only printer, or a corrupt driver.
7. Diagnose entirely blank or entirely black pages as a primary corona or charging failure, since the drum is either never charged or never discharged.
8. Diagnose paper jams by location: the pickup area points at worn pickup rollers or separation pads, the fuser area points at the fuser or wrong paper weight.
9. Diagnose multi-page misfeeds as worn separation pads or paper that is damp, curled or of the wrong weight for the tray.
10. Diagnose incorrect colour output on an inkjet by checking cartridge seating, checking for third-party ink, running head cleaning and running a colour calibration.
11. Diagnose incorrect paper size or orientation as an application, driver or tray configuration mismatch rather than a hardware fault, and record all three places to check.
12. Build the connectivity checklist for a printer that prints nothing at all: check the print queue for stalled jobs, restart the print spooler, verify network reachability and confirm the correct printer is selected.

   ```bash
   net stop spooler && net start spooler
   ```


## Test it — verification

Your map covers all twelve defects with a named component and a corrective action; the fuser, drum and corona faults are correctly distinguished; and the connectivity checklist includes clearing the queue and restarting the spooler.

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
