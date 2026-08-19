# Lab 13 Worksheet — RAM Identification, Installation and Channel Configuration

**Name:** ______________________    **Date:** ______________

**Exam objective:** Identify RAM types and form factors, install modules correctly and configure dual-channel operation, verifying the result in firmware and the OS (Core 1 objective 3.3).

## Record as you go

| Step | What you did | What you observed |
| --- | --- | --- |
| 1 | Put on the anti-static strap, power down the machine, disconnect it from the mains and hold the power button for 15 seconds to discharge. |  |
| 2 | Remove a memory module by pressing the retaining clips outward at both ends simultaneously, then lift the module by its edges without touching the gold contacts. |  |
| 3 | Read the module label and decode every field: capacity, DDR generation, speed rating, CAS latency and whether it is ECC or non-ECC. |  |
| 4 | Identify the form factor: a full-length DIMM for desktops and servers, or a shorter SODIMM for laptops and small-form-factor systems. |  |
| 5 | Locate the notch in the module's contact edge and confirm it aligns with the key in the slot — DDR3, DDR4 and DDR5 are keyed differently and cannot be interchanged. |  |
| 6 | Consult the motherboard manual or its silkscreen to identify which slot pairs form the dual-channel banks, typically slots 1 and 3 or the colour-matched pair. |  |
| 7 | Install two matched modules into the correct channel pair, pressing straight down at both ends until the retaining clips snap closed by themselves. |  |
| 8 | Boot into BIOS/UEFI and record the total memory detected, the operating speed and whether the system reports single or dual channel. |  |
| 9 | Boot into Windows, open Task Manager, go to Performance then Memory, and record total capacity, speed, form factor, slots used and hardware reserved. |  |
| 10 | Compare the reported speed against the module's rated speed and explain any difference — a module rated above the chipset's supported speed runs at the lower rate unless XMP is enabled. |  |
| 11 | Explain what ECC memory does, that it makes a system more stable rather than faster, and why it requires explicit CPU and motherboard support. |  |
| 12 | Write a memory upgrade recommendation for a stated workload, naming the capacity, generation, speed and slot configuration, and justify it against the chipset's maximum. |  |

## Verification

**Success criterion:** The system POSTs and reports the full installed capacity, Task Manager confirms the correct speed and slot usage, dual channel is confirmed in firmware, and your upgrade recommendation names a specific module that the chipset actually supports.

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
