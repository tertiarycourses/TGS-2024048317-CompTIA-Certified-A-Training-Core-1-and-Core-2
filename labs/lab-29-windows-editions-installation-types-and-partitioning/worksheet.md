# Lab 29 Worksheet — Windows Editions, Installation Types and Partitioning

**Name:** ______________________    **Date:** ______________

**Exam objective:** Select the correct Windows edition and installation type for a requirement, and plan MBR or GPT partitioning to match the firmware mode (Core 2 objectives 1.1 and 1.9).

## Record as you go

| Step | What you did | What you observed |
| --- | --- | --- |
| 1 | Build the edition matrix with rows for Home, Pro, Pro for Workstations and Enterprise, and columns for domain join, BitLocker, Group Policy, Remote Desktop host and maximum RAM. |  |
| 2 | Record the decisive difference: Home cannot join a domain and has no BitLocker or Group Policy, which rules it out for almost every business deployment. |  |
| 3 | Compare the installation types — clean install, in-place upgrade, network deployment and cloning — on what each preserves, what it requires and how long it takes per machine. |  |
| 4 | Record the valid upgrade paths: Windows 7 and 8.1 upgrade in place to Windows 10, and Windows 10 upgrades in place to Windows 11 where the hardware requirements are met. |  |
| 5 | Record the Windows 11 hardware requirements that block many upgrades: TPM 2.0, UEFI with Secure Boot, a 64-bit supported processor, 4 GB RAM and 64 GB storage. |  |
| 6 | Record the pre-upgrade checklist: back up files and preferences, verify application and driver compatibility, verify hardware compatibility, and confirm the rollback window. |  |
| 7 | Compare MBR and GPT on maximum disk size, partition count and firmware requirement, and record that UEFI Secure Boot requires GPT while legacy BIOS uses MBR. |  |
| 8 | Confirm your own machine's firmware mode and Secure Boot state, since this determines which partition scheme is valid. |  |
| 9 | Open Disk Management and record each disk's partition style, its volumes, their file systems and their free space. |  |
| 10 | Inspect the same information from the command line, which is what you use when Windows will not boot into the GUI. |  |
| 11 | Distinguish primary, extended and logical partitions under MBR, and record why the four-primary limit forces an extended partition when more volumes are needed. |  |
| 12 | Compare a full format, which checks every sector for bad sectors, against a quick format, which only rewrites the file system table, and state when each is appropriate. |  |

## Verification

**Success criterion:** Your edition matrix correctly identifies which editions support domain join and BitLocker, each installation-type selection is justified against its requirement, and the partition plan matches the firmware mode confirmed in msinfo32.

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
