# Lab 13 — RAM Identification, Installation and Channel Configuration

> **Course:** CompTIA Certified A+ Training (Core 1 and Core 2) (TGS-2024048317)  
> **Topic 03:** Hardware — Core 1, 25% of Core 1  
> **Exam objective:** Identify RAM types and form factors, install modules correctly and configure dual-channel operation, verifying the result in firmware and the OS (Core 1 objective 3.3).

## Goal

You identify memory by its physical keying and label, install modules into the correct slots for dual-channel operation, and then verify from both firmware and the operating system that the configuration took effect. You also read a module label the way a technician ordering a replacement must.

## What you'll produce

A RAM specification decode, a verified dual-channel installation and a memory upgrade recommendation for a stated workload.

## Tools and equipment

Training PC or laptop, DIMM and SODIMM modules, anti-static strap, Task Manager, CPU-Z or equivalent

## Safety

- Disconnect mains power and hold the power button for 15 seconds before working inside any machine.
- Wear an anti-static strap connected to an earthed point; hold boards and cards by their edges.
- **Never open a power supply unit or a CRT monitor** — both retain a lethal charge after being unplugged.
- Never puncture, compress or charge a swollen lithium battery; isolate it and follow hazardous disposal procedure.

## Step-by-step

1. Put on the anti-static strap, power down the machine, disconnect it from the mains and hold the power button for 15 seconds to discharge.
2. Remove a memory module by pressing the retaining clips outward at both ends simultaneously, then lift the module by its edges without touching the gold contacts.
3. Read the module label and decode every field: capacity, DDR generation, speed rating, CAS latency and whether it is ECC or non-ECC.
4. Identify the form factor: a full-length DIMM for desktops and servers, or a shorter SODIMM for laptops and small-form-factor systems.
5. Locate the notch in the module's contact edge and confirm it aligns with the key in the slot — DDR3, DDR4 and DDR5 are keyed differently and cannot be interchanged.
6. Consult the motherboard manual or its silkscreen to identify which slot pairs form the dual-channel banks, typically slots 1 and 3 or the colour-matched pair.
7. Install two matched modules into the correct channel pair, pressing straight down at both ends until the retaining clips snap closed by themselves.
8. Boot into BIOS/UEFI and record the total memory detected, the operating speed and whether the system reports single or dual channel.
9. Boot into Windows, open Task Manager, go to Performance then Memory, and record total capacity, speed, form factor, slots used and hardware reserved.

   ```bash
   taskmgr
   ```

10. Compare the reported speed against the module's rated speed and explain any difference — a module rated above the chipset's supported speed runs at the lower rate unless XMP is enabled.
11. Explain what ECC memory does, that it makes a system more stable rather than faster, and why it requires explicit CPU and motherboard support.
12. Write a memory upgrade recommendation for a stated workload, naming the capacity, generation, speed and slot configuration, and justify it against the chipset's maximum.

## Test it — verification

The system POSTs and reports the full installed capacity, Task Manager confirms the correct speed and slot usage, dual channel is confirmed in firmware, and your upgrade recommendation names a specific module that the chipset actually supports.

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
