# Lab 33 Worksheet — File Systems, Permissions and Share Configuration

**Name:** ______________________    **Date:** ______________

**Exam objective:** Compare NTFS, FAT32 and exFAT, and configure NTFS and share permissions correctly, applying the most-restrictive rule (Core 2 objectives 1.9 and 2.5).

## Record as you go

| Step | What you did | What you observed |
| --- | --- | --- |
| 1 | Build the comparison table for NTFS, FAT32 and exFAT with columns for maximum file size, maximum volume size, permissions support, encryption, journaling and compatibility. |  |
| 2 | Record the decisive limits: FAT32 cannot hold a file larger than 4 GB, exFAT removes that limit but has no permissions, and NTFS supports permissions, encryption, compression and journaling. |  |
| 3 | Record which file system to choose for a USB drive shared with macOS, an internal Windows system drive, and a drive holding files larger than 4 GB. |  |
| 4 | Confirm the file system on your own volumes. |  |
| 5 | Create a test folder structure for the permissions exercise. |  |
| 6 | Display the current NTFS permissions and identify which are inherited from the parent folder. |  |
| 7 | Grant a specific user read-only NTFS permission on the folder and confirm the change. |  |
| 8 | Record the standard NTFS permission levels in increasing order: Read, Read and Execute, List Folder Contents, Write, Modify and Full Control. |  |
| 9 | Explain inheritance: child files and folders inherit permissions from the parent unless inheritance is explicitly broken, and record why breaking inheritance must be deliberate. |  |
| 10 | Share the folder over the network and set a share permission that differs from the NTFS permission. |  |
| 11 | State the effective permission for a user with Full Control at the share level and Read at the NTFS level, and confirm the most-restrictive rule gives Read. |  |
| 12 | Record that NTFS permissions apply both locally and over the network while share permissions apply only over the network, then remove the share and clean up. |  |

## Verification

**Success criterion:** Your comparison table states the 4 GB FAT32 file size limit and identifies which file systems support permissions; icacls confirms the granted permission; and you correctly state that Share Full Control combined with NTFS Read yields an effective permission of Read.

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
