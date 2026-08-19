# Lab 23 Worksheet — POST, Boot and Power Fault Diagnosis

**Name:** ______________________    **Date:** ______________

**Exam objective:** Diagnose no-power, no-POST and no-boot faults using beep codes, diagnostic LEDs and a systematic elimination sequence (Core 1 objective 5.2).

## Record as you go

| Step | What you did | What you observed |
| --- | --- | --- |
| 1 | Separate the three failure classes precisely, because they have different causes: no power means nothing happens at all, no POST means fans spin but nothing appears on screen, and no boot means POST completes but the OS does not load. |  |
| 2 | Build the no-power branch: check the wall socket and the mains lead, check the PSU switch, check the case power switch header, test or substitute the PSU, then suspect the motherboard. |  |
| 3 | Build the no-POST branch: listen for beep codes, read diagnostic LEDs or the POST code display, reseat RAM, reseat the graphics card, disconnect all non-essential devices, then clear CMOS. |  |
| 4 | Record the beep code principle: patterns are manufacturer-specific and must be read from that board's manual, but a repeating pattern most commonly indicates RAM or graphics. |  |
| 5 | Record the reseating principle: reseating RAM and expansion cards costs nothing and resolves a large share of no-POST faults caused by vibration, thermal cycling or transport. |  |
| 6 | Build the no-boot branch: check the boot order, remove any bootable USB device, confirm the drive is detected in firmware, then repair the boot record from the recovery environment. |  |
| 7 | Record the minimum configuration test: strip the system to CPU, one RAM stick, integrated graphics and the PSU. If it POSTs, add components back one at a time until the fault returns. |  |
| 8 | Map the remaining hardware symptoms to causes: a burning smell means shut down and unplug immediately, a grinding noise means a failing fan or drive, and capacitor swelling means the board must be replaced. |  |
| 9 | Record that an inaccurate system date and time that resets on every boot means the CMOS battery is dead, and that this is a two-dollar part rather than a board fault. |  |
| 10 | Record the intermittent shutdown checklist: overheating, a failing PSU, a loose power connector, or a short from a misplaced standoff behind the board. |  |
| 11 | Record the sluggish performance checklist: insufficient RAM, a failing or nearly full disk, thermal throttling, malware, or too many startup applications. |  |
| 12 | Assemble the three branches into one flowchart with a clear entry question that routes a technician to the correct branch within two questions. |  |

## Verification

**Success criterion:** Your flowchart routes to the correct branch from the entry symptom in no more than two questions, each branch orders its checks from cheapest and least invasive to most, and the minimum configuration test is included in the no-POST branch.

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
