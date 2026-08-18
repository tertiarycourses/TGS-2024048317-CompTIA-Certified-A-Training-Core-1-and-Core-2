# Lab 45 — Windows OS Symptom Diagnosis and Recovery Tools

> **Course:** CompTIA Certified A+ Training (Core 1 and Core 2) (TGS-2024048317)  
> **Topic 08:** Software Troubleshooting — Core 2, 23% of Core 2  
> **Exam objective:** Diagnose common Windows symptoms and select the correct recovery tool, escalating from least to most destructive (Core 2 objectives 3.1 and 3.2).

## Goal

Windows recovery tools differ in what they destroy, so choosing correctly is what separates a fixed machine from a rebuilt one. You build the escalation ladder, then map each Windows symptom to the lowest rung that will actually resolve it.

## What you'll produce

A recovery tool escalation ladder and a symptom-to-tool map covering ten Windows symptoms.

## Tools and equipment

Windows PC, System Restore, Windows Recovery Environment, Event Viewer, msconfig, sfc, DISM

## Safety

- Disconnect mains power and hold the power button for 15 seconds before working inside any machine.
- Wear an anti-static strap connected to an earthed point; hold boards and cards by their edges.
- **Never open a power supply unit or a CRT monitor** — both retain a lethal charge after being unplugged.
- Never puncture, compress or charge a swollen lithium battery; isolate it and follow hazardous disposal procedure.

## Step-by-step

1. Build the escalation ladder from least to most destructive: reboot, restart the service, roll back the driver or update, System Restore, sfc and DISM, Startup Repair, Reset keeping files, Reset removing everything, then reimage.
2. Record the guiding rule: always start at the lowest rung that could plausibly resolve the symptom, because every rung up costs the user more time and more data risk.
3. Record what System Restore does and does not do: it rolls back system files, drivers and the registry, but it does not restore or remove personal files.
4. Verify System Restore is enabled and list the available restore points, since a machine with protection disabled has no restore points at all.

   ```bash
   powershell -Command "Get-ComputerRestorePoint | Select-Object CreationTime,Description"
   ```

5. Diagnose a blue screen of death: record the stop code, identify what changed immediately before it, then roll back the most recent driver or update and test memory.
6. Diagnose sluggish performance using Task Manager and Resource Monitor to identify which of CPU, memory, disk or network is saturated before treating anything.

   ```bash
   resmon
   ```

7. Diagnose frequent shutdowns by separating the causes: overheating, a failing power supply, corrupt system files or a failing driver, and give the test that distinguishes them.
8. Diagnose applications crashing by checking Event Viewer's Application log for the faulting module, then repairing or reinstalling the application.

   ```bash
   eventvwr.msc
   ```

9. Diagnose 'no OS found' by checking boot order, removing bootable USB devices, confirming the disk is detected, then repairing the boot record from the recovery environment.
10. Diagnose a slow profile load by examining startup applications, and record that a roaming profile that has grown large is a common cause in a domain environment.

   ```bash
   msconfig
   ```

11. Diagnose USB controller resource warnings, and record that too many devices on one bus is resolved by redistributing devices across controllers.
12. Record how to access the Windows Recovery Environment — three failed boots trigger it automatically, or hold Shift while selecting Restart — and list the tools it provides.

## Test it — verification

Your ladder orders all ten recovery options from least to most destructive; the symptom map assigns each of ten symptoms to a specific rung with justification; and you correctly state that System Restore does not affect personal files.

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
