# Lab 33 — File Systems, Permissions and Share Configuration

> **Course:** CompTIA Certified A+ Training (Core 1 and Core 2) (TGS-2024048317)  
> **Topic 06:** Operating Systems — Core 2, 28% of Core 2  
> **Exam objective:** Compare NTFS, FAT32 and exFAT, and configure NTFS and share permissions correctly, applying the most-restrictive rule (Core 2 objectives 1.9 and 2.5).

## Goal

You compare the Windows file systems on the limits that decide which to use, then configure both NTFS and share permissions on the same folder and prove the most-restrictive rule — the single most misunderstood permission behaviour in Windows.

## What you'll produce

A file system comparison table and a configured share demonstrating the effective permission when NTFS and share permissions differ.

## Tools and equipment

Windows PC, File Explorer, icacls, net share, Disk Management

## Safety

- Disconnect mains power and hold the power button for 15 seconds before working inside any machine.
- Wear an anti-static strap connected to an earthed point; hold boards and cards by their edges.
- **Never open a power supply unit or a CRT monitor** — both retain a lethal charge after being unplugged.
- Never puncture, compress or charge a swollen lithium battery; isolate it and follow hazardous disposal procedure.

## Step-by-step

1. Build the comparison table for NTFS, FAT32 and exFAT with columns for maximum file size, maximum volume size, permissions support, encryption, journaling and compatibility.
2. Record the decisive limits: FAT32 cannot hold a file larger than 4 GB, exFAT removes that limit but has no permissions, and NTFS supports permissions, encryption, compression and journaling.
3. Record which file system to choose for a USB drive shared with macOS, an internal Windows system drive, and a drive holding files larger than 4 GB.
4. Confirm the file system on your own volumes.

   ```bash
   wmic logicaldisk get name,filesystem,size,freespace
   ```

5. Create a test folder structure for the permissions exercise.

   ```bash
   md C:\aplus-share\data && echo Sensitive content > C:\aplus-share\data\test.txt
   ```

6. Display the current NTFS permissions and identify which are inherited from the parent folder.

   ```bash
   icacls C:\aplus-share
   ```

7. Grant a specific user read-only NTFS permission on the folder and confirm the change.

   ```bash
   icacls C:\aplus-share /grant Users:(OI)(CI)R && icacls C:\aplus-share
   ```

8. Record the standard NTFS permission levels in increasing order: Read, Read and Execute, List Folder Contents, Write, Modify and Full Control.
9. Explain inheritance: child files and folders inherit permissions from the parent unless inheritance is explicitly broken, and record why breaking inheritance must be deliberate.
10. Share the folder over the network and set a share permission that differs from the NTFS permission.

   ```bash
   net share aplusshare=C:\aplus-share /grant:Everyone,FULL && net share aplusshare
   ```

11. State the effective permission for a user with Full Control at the share level and Read at the NTFS level, and confirm the most-restrictive rule gives Read.
12. Record that NTFS permissions apply both locally and over the network while share permissions apply only over the network, then remove the share and clean up.

   ```bash
   net share aplusshare /delete && rd /s /q C:\aplus-share
   ```


## Test it — verification

Your comparison table states the 4 GB FAT32 file size limit and identifies which file systems support permissions; icacls confirms the granted permission; and you correctly state that Share Full Control combined with NTFS Read yields an effective permission of Read.

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
