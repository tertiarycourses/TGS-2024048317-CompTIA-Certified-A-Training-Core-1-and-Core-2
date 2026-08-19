# Lab 14 Worksheet — Storage Devices and RAID Level Selection

**Name:** ______________________    **Date:** ______________

**Exam objective:** Compare HDD, SSD, NVMe and hybrid storage, and select the correct RAID level for a stated capacity, performance and redundancy requirement (Core 1 objectives 3.3 and 3.4).

## Record as you go

| Step | What you did | What you observed |
| --- | --- | --- |
| 1 | Build the storage comparison table with rows for HDD, SATA SSD, NVMe M.2 SSD and SSHD and columns for interface, typical speed, cost per terabyte, moving parts and best use. |  |
| 2 | Record the form factors: 3.5-inch for desktop and server HDDs, 2.5-inch for laptop drives and SATA SSDs, and M.2 for the smallest SSDs. |  |
| 3 | Explain why NVMe is faster than SATA — it runs over PCIe lanes directly rather than through the SATA controller and its command queue. |  |
| 4 | Note that M.2 slots are keyed, that an M.2 slot may support SATA, NVMe or both, and that checking this before ordering avoids buying an incompatible drive. |  |
| 5 | Open the Killercoda Ubuntu playground and list the block devices present with their sizes and mount points. |  |
| 6 | Inspect the filesystem usage and free space on the playground to see how a technician confirms available capacity. |  |
| 7 | Build the RAID table for levels 0, 1, 5 and 10 with columns for minimum disks, usable capacity formula, fault tolerance, read performance and write performance. |  |
| 8 | Calculate usable capacity for four 2 TB disks in each level: RAID 0 gives 8 TB, RAID 1 gives 2 TB with two mirrored pairs or 4 TB total, RAID 5 gives 6 TB, and RAID 10 gives 4 TB. |  |
| 9 | Record fault tolerance for each: RAID 0 tolerates none, RAID 1 tolerates one per mirror, RAID 5 tolerates one, and RAID 10 tolerates one per mirrored pair. |  |
| 10 | Solve the scenario of a video editing scratch disk needing maximum speed where the data is reproducible — RAID 0 is correct because redundancy is not required. |  |
| 11 | Solve the scenario of a small business file server needing redundancy and reasonable capacity — RAID 5 is correct because it gives redundancy with only one disk of parity overhead. |  |
| 12 | Solve the remaining scenarios of a database needing both write performance and redundancy, and a boot volume in a two-disk workstation, and justify each choice. |  |

## Verification

**Success criterion:** Your capacity calculations for four 2 TB disks are correct for all four RAID levels, every scenario selection is justified against the stated requirement, and the comparison table correctly ranks the four storage types on speed and cost per terabyte.

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
