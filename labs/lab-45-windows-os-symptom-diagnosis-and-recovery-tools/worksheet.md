# Lab 45 Worksheet — Windows OS Symptom Diagnosis and Recovery Tools

**Name:** ______________________    **Date:** ______________

**Exam objective:** Diagnose common Windows symptoms and select the correct recovery tool, escalating from least to most destructive (Core 2 objectives 3.1 and 3.2).

## Record as you go

| Step | What you did | What you observed |
| --- | --- | --- |
| 1 | Build the escalation ladder from least to most destructive: reboot, restart the service, roll back the driver or update, System Restore, sfc and DISM, Startup Repair, Reset keeping files, Reset removing everything, then reimage. |  |
| 2 | Record the guiding rule: always start at the lowest rung that could plausibly resolve the symptom, because every rung up costs the user more time and more data risk. |  |
| 3 | Record what System Restore does and does not do: it rolls back system files, drivers and the registry, but it does not restore or remove personal files. |  |
| 4 | Verify System Restore is enabled and list the available restore points, since a machine with protection disabled has no restore points at all. |  |
| 5 | Diagnose a blue screen of death: record the stop code, identify what changed immediately before it, then roll back the most recent driver or update and test memory. |  |
| 6 | Diagnose sluggish performance using Task Manager and Resource Monitor to identify which of CPU, memory, disk or network is saturated before treating anything. |  |
| 7 | Diagnose frequent shutdowns by separating the causes: overheating, a failing power supply, corrupt system files or a failing driver, and give the test that distinguishes them. |  |
| 8 | Diagnose applications crashing by checking Event Viewer's Application log for the faulting module, then repairing or reinstalling the application. |  |
| 9 | Diagnose 'no OS found' by checking boot order, removing bootable USB devices, confirming the disk is detected, then repairing the boot record from the recovery environment. |  |
| 10 | Diagnose a slow profile load by examining startup applications, and record that a roaming profile that has grown large is a common cause in a domain environment. |  |
| 11 | Diagnose USB controller resource warnings, and record that too many devices on one bus is resolved by redistributing devices across controllers. |  |
| 12 | Record how to access the Windows Recovery Environment — three failed boots trigger it automatically, or hold Shift while selecting Restart — and list the tools it provides. |  |

## Verification

**Success criterion:** Your ladder orders all ten recovery options from least to most destructive; the symptom map assigns each of ten symptoms to a specific rung with justification; and you correctly state that System Restore does not affect personal files.

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
