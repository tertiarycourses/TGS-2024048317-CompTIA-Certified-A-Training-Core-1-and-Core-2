# Lab 36 — macOS Tools and Cross-Platform File System Compatibility

> **Course:** CompTIA Certified A+ Training (Core 1 and Core 2) (TGS-2024048317)  
> **Topic 06:** Operating Systems — Core 2, 28% of Core 2  
> **Exam objective:** Identify macOS features and utilities and resolve cross-platform file system compatibility between Windows, macOS and Linux (Core 2 objectives 1.10 and 1.9).

## Goal

You map the macOS toolset to its Windows equivalent, which is how a technician supporting a mixed fleet actually thinks, then solve the file system compatibility problem that causes most cross-platform support tickets.

## What you'll produce

A macOS-to-Windows tool equivalence table and a solved cross-platform file system compatibility matrix.

## Tools and equipment

macOS device or reference material, Windows PC, file system documentation

## Safety

- Disconnect mains power and hold the power button for 15 seconds before working inside any machine.
- Wear an anti-static strap connected to an earthed point; hold boards and cards by their edges.
- **Never open a power supply unit or a CRT monitor** — both retain a lethal charge after being unplugged.
- Never puncture, compress or charge a swollen lithium battery; isolate it and follow hazardous disposal procedure.

## Step-by-step

1. Build the equivalence table mapping each macOS tool to its Windows counterpart, since knowing one gives you the other.
2. Map Time Machine to File History and Windows Backup, and record that Time Machine performs versioned incremental backups to an external or network volume.
3. Map Disk Utility to Disk Management, and record that Disk Utility also provides First Aid, which repairs permissions and directory structure.
4. Map FileVault to BitLocker as the full-disk encryption feature, and Keychain to Credential Manager as the stored credential vault.
5. Map Mission Control to Task View, Spotlight to Windows Search, Finder to File Explorer and Terminal to Command Prompt or PowerShell.
6. Record Gatekeeper's role: it controls which applications may run based on their signature, and note that installing from outside the App Store requires explicitly allowing it.
7. Record the macOS software sources in order of trust: the App Store, a signed vendor installer, and an unsigned application which Gatekeeper blocks by default.
8. Record the macOS best practices from the objectives: scheduled Time Machine backups, current OS and application updates, and antivirus where organisational policy requires it.
9. Build the file system compatibility matrix with rows for NTFS, FAT32, exFAT, HFS+, APFS and ext4 and columns for Windows, macOS and Linux read and write support.
10. Record the critical compatibility fact: macOS reads NTFS but cannot write to it without third-party software, which is the cause of most cross-platform ticket escalations.
11. Solve the scenario of an external drive that must be read and written by Windows and macOS with files larger than 4 GB, and justify exFAT as the only correct answer.
12. Solve the scenario of a drive that must work with Windows, macOS and a digital camera, and justify FAT32 while stating its 4 GB limitation explicitly.

## Test it — verification

Your equivalence table maps at least eight macOS tools to their Windows counterparts; the compatibility matrix correctly shows macOS as read-only for NTFS; and both scenarios name a file system and justify it against the stated constraints.

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
