# Lab 36 Worksheet — macOS Tools and Cross-Platform File System Compatibility

**Name:** ______________________    **Date:** ______________

**Exam objective:** Identify macOS features and utilities and resolve cross-platform file system compatibility between Windows, macOS and Linux (Core 2 objectives 1.10 and 1.9).

## Record as you go

| Step | What you did | What you observed |
| --- | --- | --- |
| 1 | Build the equivalence table mapping each macOS tool to its Windows counterpart, since knowing one gives you the other. |  |
| 2 | Map Time Machine to File History and Windows Backup, and record that Time Machine performs versioned incremental backups to an external or network volume. |  |
| 3 | Map Disk Utility to Disk Management, and record that Disk Utility also provides First Aid, which repairs permissions and directory structure. |  |
| 4 | Map FileVault to BitLocker as the full-disk encryption feature, and Keychain to Credential Manager as the stored credential vault. |  |
| 5 | Map Mission Control to Task View, Spotlight to Windows Search, Finder to File Explorer and Terminal to Command Prompt or PowerShell. |  |
| 6 | Record Gatekeeper's role: it controls which applications may run based on their signature, and note that installing from outside the App Store requires explicitly allowing it. |  |
| 7 | Record the macOS software sources in order of trust: the App Store, a signed vendor installer, and an unsigned application which Gatekeeper blocks by default. |  |
| 8 | Record the macOS best practices from the objectives: scheduled Time Machine backups, current OS and application updates, and antivirus where organisational policy requires it. |  |
| 9 | Build the file system compatibility matrix with rows for NTFS, FAT32, exFAT, HFS+, APFS and ext4 and columns for Windows, macOS and Linux read and write support. |  |
| 10 | Record the critical compatibility fact: macOS reads NTFS but cannot write to it without third-party software, which is the cause of most cross-platform ticket escalations. |  |
| 11 | Solve the scenario of an external drive that must be read and written by Windows and macOS with files larger than 4 GB, and justify exFAT as the only correct answer. |  |
| 12 | Solve the scenario of a drive that must work with Windows, macOS and a digital camera, and justify FAT32 while stating its 4 GB limitation explicitly. |  |

## Verification

**Success criterion:** Your equivalence table maps at least eight macOS tools to their Windows counterparts; the compatibility matrix correctly shows macOS as read-only for NTFS; and both scenarios name a file system and justify it against the stated constraints.

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
