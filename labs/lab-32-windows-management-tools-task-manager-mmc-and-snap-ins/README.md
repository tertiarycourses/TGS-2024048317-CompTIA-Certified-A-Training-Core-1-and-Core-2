# Lab 32 — Windows Management Tools — Task Manager, MMC and Snap-ins

> **Course:** CompTIA Certified A+ Training (Core 1 and Core 2) (TGS-2024048317)  
> **Topic 06:** Operating Systems — Core 2, 28% of Core 2  
> **Exam objective:** Use Task Manager, the Microsoft Management Console and its snap-ins to diagnose performance, inspect logs and manage devices, disks, users and tasks (Core 2 objectives 1.3 and 1.4).

## Goal

You work through every Windows administrative tool named in the Core 2 objectives, launching each by its executable name — because in an exam and on a locked-down machine you need the name, not the Start menu path.

## What you'll produce

A tool reference table with the launch command and primary use for each, plus a performance triage record from Task Manager.

## Tools and equipment

Windows PC, Task Manager, MMC snap-ins, Control Panel, Windows Settings

## Safety

- Disconnect mains power and hold the power button for 15 seconds before working inside any machine.
- Wear an anti-static strap connected to an earthed point; hold boards and cards by their edges.
- **Never open a power supply unit or a CRT monitor** — both retain a lethal charge after being unplugged.
- Never puncture, compress or charge a swollen lithium battery; isolate it and follow hazardous disposal procedure.

## Step-by-step

1. Open Task Manager and record what each tab tells you: Processes, Performance, App history, Startup, Users, Details and Services.

   ```bash
   taskmgr
   ```

2. Perform a performance triage: sort Processes by CPU, then by memory, then by disk, and record the top consumer in each category.
3. Open the Startup tab, record every high-impact startup item, and state which you would disable to improve boot time and why.
4. Open Event Viewer and examine the System and Application logs, filtering to errors and critical events from the last 24 hours.

   ```bash
   eventvwr.msc
   ```

5. Record the three main Windows log categories and what each contains: System for operating system events, Security for audit events, and Application for software events.
6. Open Disk Management and record each volume with its file system, capacity, free space and status.

   ```bash
   diskmgmt.msc
   ```

7. Open Device Manager and identify any device showing a warning triangle or an unknown device, and record how you would resolve it.

   ```bash
   devmgmt.msc
   ```

8. Open Task Scheduler and examine a scheduled task's trigger, action and conditions, then record how you would create a nightly backup task.

   ```bash
   taskschd.msc
   ```

9. Open Local Users and Groups, list the local accounts and their group memberships, and record which accounts hold administrative rights.

   ```bash
   lusrmgr.msc
   ```

10. Open Performance Monitor, add a counter for processor time and available memory, and record the values observed over one minute.

   ```bash
   perfmon.msc
   ```

11. Open System Configuration and record what each tab controls, then explain when a diagnostic startup is the correct troubleshooting step.

   ```bash
   msconfig
   ```

12. Build the reference table listing every tool with its launch command and its primary use, and add cleanmgr, dfrgui, regedit and resmon to complete it.

   ```bash
   cleanmgr && dfrgui && resmon
   ```


## Test it — verification

Your table lists at least twelve tools with the correct launch command for each; the Task Manager triage names the top CPU, memory and disk consumer; and the Event Viewer record cites at least one real error with its source and event ID.

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
