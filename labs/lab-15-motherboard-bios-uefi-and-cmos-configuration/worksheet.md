# Lab 15 Worksheet — Motherboard, BIOS/UEFI and CMOS Configuration

**Name:** ______________________    **Date:** ______________

**Exam objective:** Identify motherboard form factors, expansion slots and headers, and configure BIOS/UEFI settings including boot order, virtualization support, Secure Boot and TPM (Core 1 objectives 3.4 and 3.5).

## Record as you go

| Step | What you did | What you observed |
| --- | --- | --- |
| 1 | Identify the form factor from the board's dimensions and mounting holes: ATX at 305 by 244 mm, micro-ATX at 244 by 244 mm, or Mini-ITX at 170 by 170 mm. |  |
| 2 | Locate and label the CPU socket, and record its type — LGA where the pins are on the board, or PGA where the pins are on the processor. |  |
| 3 | Locate the memory slots, count them, and record their colour pairing which indicates the dual-channel banks. |  |
| 4 | Locate the expansion slots and record each as PCIe x16, x8, x4 or x1, noting that a shorter card fits a longer slot but not the reverse. |  |
| 5 | Locate the storage connectors — SATA ports and M.2 slots — and record how many of each the board provides. |  |
| 6 | Locate the power connectors: the 24-pin ATX for the board and the 4 or 8-pin EPS for the CPU, and note that omitting the EPS connector is a common no-boot cause. |  |
| 7 | Locate the front-panel header, the CMOS battery and the clear-CMOS jumper, and record the procedure for resetting firmware to defaults. |  |
| 8 | Enter BIOS/UEFI by pressing Delete or F2 during POST and record which key this board uses. |  |
| 9 | Record the current boot order, then change it to boot from USB first and record the exact menu path where this setting lives. |  |
| 10 | Find and enable hardware virtualization support — Intel VT-x or AMD-V — and record the menu path, since this is required before any 64-bit VM will start. |  |
| 11 | Locate the Secure Boot and TPM settings, record their current state, and note that BitLocker requires the TPM to be enabled. |  |
| 12 | Save and exit, boot into Windows, and confirm the firmware mode and Secure Boot state from system information. |  |

## Verification

**Success criterion:** msinfo32 reports the expected BIOS mode and Secure Boot state, virtualization support is enabled and confirmed, and your configuration record gives the exact menu path for boot order, virtualization, Secure Boot and TPM.

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
