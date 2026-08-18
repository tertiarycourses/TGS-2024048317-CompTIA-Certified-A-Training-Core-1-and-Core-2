# Lab 18 — Printer Installation, Configuration and the Laser Imaging Process

> **Course:** CompTIA Certified A+ Training (Core 1 and Core 2) (TGS-2024048317)  
> **Topic 03:** Hardware — Core 1, 25% of Core 1  
> **Exam objective:** Install and share a printer, configure its settings and security, and map each stage of the laser imaging process to the print defect its failure produces (Core 1 objectives 3.6 and 3.7).

## Goal

You install and share a printer, configure the settings users actually ask about, then learn the seven-step laser process in order — because knowing the order is exactly what converts a print defect into a named failed component.

## What you'll produce

A configured and shared printer, a printer settings reference, and a laser process defect map linking each stage to its symptom.

## Tools and equipment

Printer or printer emulator, Windows print management, laser printer reference diagram, PCL/PostScript drivers

## Safety

- Disconnect mains power and hold the power button for 15 seconds before working inside any machine.
- Wear an anti-static strap connected to an earthed point; hold boards and cards by their edges.
- **Never open a power supply unit or a CRT monitor** — both retain a lethal charge after being unplugged.
- Never puncture, compress or charge a swollen lithium battery; isolate it and follow hazardous disposal procedure.

## Step-by-step

1. Unbox and site the printer correctly: adequate clearance for paper paths and covers, a suitable power source and the right connection — USB, Ethernet or wireless.
2. Install the printer driver, choosing between PCL, developed by HP and most common, and PostScript, developed by Adobe and used in graphics and industrial work.
3. Add the printer in Windows and print a test page to confirm the driver and connection work end to end.

   ```bash
   control printers
   ```

4. Configure the default settings users ask about most: duplex printing, orientation, paper tray selection and print quality.
5. Share the printer and record the difference between a printer share, where a workstation shares its own printer and must stay on, and a print server, which is a dedicated always-on host.
6. Configure printer security: user authentication so only authorised staff may print, badging where supported, audit logging and secured or held print release.
7. Record the seven stages of the laser imaging process in order: processing, charging, exposing, developing, transferring, fusing and cleaning.
8. Map stage failures to defects: a scratched imaging drum produces vertical lines down every page, and a failed primary corona produces entirely blank or entirely black pages.
9. Continue the map: a failed fuser leaves toner that smudges when rubbed because it was never melted onto the paper, and failed cleaning produces repeated ghost images at the drum's circumference.
10. Record the maintenance kit contents — fuser unit, transfer roller, paper feed and separation rollers and pickup rollers — and note that the printer must be calibrated after fitting one.
11. Compare the other printer types on cost, speed and use: inkjet for affordable colour, impact for multi-part carbon forms, thermal for receipts, and 3D printers using FDM filament or SLA resin.
12. Record the safety rules: avoid inhaling toner, never use a normal vacuum on toner because it passes through the filter, and let the fuser cool before touching it as it operates above 180 degrees Celsius.

## Test it — verification

The printer prints a test page and is shared successfully, your defect map correctly links at least four print defects to the specific laser stage that failed, and the safety rules include the toner vacuum and hot fuser warnings.

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
