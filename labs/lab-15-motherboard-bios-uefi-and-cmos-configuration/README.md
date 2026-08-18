# Lab 15 — Motherboard, BIOS/UEFI and CMOS Configuration

> **Course:** CompTIA Certified A+ Training (Core 1 and Core 2) (TGS-2024048317)  
> **Topic 03:** Hardware — Core 1, 25% of Core 1  
> **Exam objective:** Identify motherboard form factors, expansion slots and headers, and configure BIOS/UEFI settings including boot order, virtualization support, Secure Boot and TPM (Core 1 objectives 3.4 and 3.5).

## Goal

You map a motherboard component by component, then enter firmware and configure the settings that matter in support work — boot order, virtualization support, Secure Boot and the TPM — recording where each lives so you can find it again on an unfamiliar board.

## What you'll produce

An annotated motherboard map and a documented BIOS/UEFI configuration record with the menu path for each setting.

## Tools and equipment

Training PC, motherboard reference or physical board, BIOS/UEFI setup utility, msinfo32

## Safety

- Disconnect mains power and hold the power button for 15 seconds before working inside any machine.
- Wear an anti-static strap connected to an earthed point; hold boards and cards by their edges.
- **Never open a power supply unit or a CRT monitor** — both retain a lethal charge after being unplugged.
- Never puncture, compress or charge a swollen lithium battery; isolate it and follow hazardous disposal procedure.

## Step-by-step

1. Identify the form factor from the board's dimensions and mounting holes: ATX at 305 by 244 mm, micro-ATX at 244 by 244 mm, or Mini-ITX at 170 by 170 mm.
2. Locate and label the CPU socket, and record its type — LGA where the pins are on the board, or PGA where the pins are on the processor.
3. Locate the memory slots, count them, and record their colour pairing which indicates the dual-channel banks.
4. Locate the expansion slots and record each as PCIe x16, x8, x4 or x1, noting that a shorter card fits a longer slot but not the reverse.
5. Locate the storage connectors — SATA ports and M.2 slots — and record how many of each the board provides.
6. Locate the power connectors: the 24-pin ATX for the board and the 4 or 8-pin EPS for the CPU, and note that omitting the EPS connector is a common no-boot cause.
7. Locate the front-panel header, the CMOS battery and the clear-CMOS jumper, and record the procedure for resetting firmware to defaults.
8. Enter BIOS/UEFI by pressing Delete or F2 during POST and record which key this board uses.
9. Record the current boot order, then change it to boot from USB first and record the exact menu path where this setting lives.
10. Find and enable hardware virtualization support — Intel VT-x or AMD-V — and record the menu path, since this is required before any 64-bit VM will start.
11. Locate the Secure Boot and TPM settings, record their current state, and note that BitLocker requires the TPM to be enabled.
12. Save and exit, boot into Windows, and confirm the firmware mode and Secure Boot state from system information.

   ```bash
   msinfo32
   ```


## Test it — verification

msinfo32 reports the expected BIOS mode and Secure Boot state, virtualization support is enabled and confirmed, and your configuration record gives the exact menu path for boot order, virtualization, Secure Boot and TPM.

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
