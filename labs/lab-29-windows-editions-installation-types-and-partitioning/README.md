# Lab 29 — Windows Editions, Installation Types and Partitioning

> **Course:** CompTIA Certified A+ Training (Core 1 and Core 2) (TGS-2024048317)  
> **Topic 06:** Operating Systems — Core 2, 28% of Core 2  
> **Exam objective:** Select the correct Windows edition and installation type for a requirement, and plan MBR or GPT partitioning to match the firmware mode (Core 2 objectives 1.1 and 1.9).

## Goal

You match Windows editions to requirements, choose the right installation type for each situation, and plan the partition scheme — the decision that determines whether the installer will even proceed, since UEFI Secure Boot requires GPT.

## What you'll produce

An edition selection matrix, four justified installation-type selections and a partition plan matched to the firmware mode.

## Tools and equipment

Windows installation media or reference, Disk Management, diskpart, msinfo32

## Safety

- Disconnect mains power and hold the power button for 15 seconds before working inside any machine.
- Wear an anti-static strap connected to an earthed point; hold boards and cards by their edges.
- **Never open a power supply unit or a CRT monitor** — both retain a lethal charge after being unplugged.
- Never puncture, compress or charge a swollen lithium battery; isolate it and follow hazardous disposal procedure.

## Step-by-step

1. Build the edition matrix with rows for Home, Pro, Pro for Workstations and Enterprise, and columns for domain join, BitLocker, Group Policy, Remote Desktop host and maximum RAM.
2. Record the decisive difference: Home cannot join a domain and has no BitLocker or Group Policy, which rules it out for almost every business deployment.
3. Compare the installation types — clean install, in-place upgrade, network deployment and cloning — on what each preserves, what it requires and how long it takes per machine.
4. Record the valid upgrade paths: Windows 7 and 8.1 upgrade in place to Windows 10, and Windows 10 upgrades in place to Windows 11 where the hardware requirements are met.
5. Record the Windows 11 hardware requirements that block many upgrades: TPM 2.0, UEFI with Secure Boot, a 64-bit supported processor, 4 GB RAM and 64 GB storage.
6. Record the pre-upgrade checklist: back up files and preferences, verify application and driver compatibility, verify hardware compatibility, and confirm the rollback window.
7. Compare MBR and GPT on maximum disk size, partition count and firmware requirement, and record that UEFI Secure Boot requires GPT while legacy BIOS uses MBR.
8. Confirm your own machine's firmware mode and Secure Boot state, since this determines which partition scheme is valid.

   ```bash
   msinfo32
   ```

9. Open Disk Management and record each disk's partition style, its volumes, their file systems and their free space.

   ```bash
   diskmgmt.msc
   ```

10. Inspect the same information from the command line, which is what you use when Windows will not boot into the GUI.

   ```bash
   diskpart /? && echo list disk | diskpart
   ```

11. Distinguish primary, extended and logical partitions under MBR, and record why the four-primary limit forces an extended partition when more volumes are needed.
12. Compare a full format, which checks every sector for bad sectors, against a quick format, which only rewrites the file system table, and state when each is appropriate.

## Test it — verification

Your edition matrix correctly identifies which editions support domain join and BitLocker, each installation-type selection is justified against its requirement, and the partition plan matches the firmware mode confirmed in msinfo32.

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
