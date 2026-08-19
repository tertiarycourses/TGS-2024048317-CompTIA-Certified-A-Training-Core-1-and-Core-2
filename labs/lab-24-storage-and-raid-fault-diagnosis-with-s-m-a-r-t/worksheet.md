# Lab 24 Worksheet — Storage and RAID Fault Diagnosis with S.M.A.R.T.

**Name:** ______________________    **Date:** ______________

**Exam objective:** Diagnose storage faults using S.M.A.R.T. data, symptom analysis and RAID status, and choose the correct recovery action for each RAID level (Core 1 objective 5.3).

## Record as you go

| Step | What you did | What you observed |
| --- | --- | --- |
| 1 | Record the first rule of storage troubleshooting: if the data matters and the drive is failing, back it up before you do anything else. Diagnostics can be the final straw for a dying drive. |  |
| 2 | Check drive health on Windows using the built-in interface and record the status reported for each physical disk. |  |
| 3 | Open Disk Management and record each volume's file system, capacity, free space and status. |  |
| 4 | Open the Killercoda Ubuntu playground and install the S.M.A.R.T. monitoring tools to read raw drive attributes. |  |
| 5 | List the block devices available so you know which device names to query. |  |
| 6 | Read the S.M.A.R.T. attributes for a device and record the overall health self-assessment result. |  |
| 7 | Record the S.M.A.R.T. attributes that matter most: reallocated sector count, current pending sector count, offline uncorrectable and read error rate — any non-zero value on the first three is a replace signal. |  |
| 8 | Record the correct response to a S.M.A.R.T. warning: back up immediately and replace the drive. S.M.A.R.T. reports a drive that is already failing, not one that might fail eventually. |  |
| 9 | Map the audible and behavioural symptoms: clicking or grinding means imminent mechanical failure, and extended read and write times or falling IOPS mean the drive is retrying failing sectors. |  |
| 10 | Map 'bootable device not found' to its three causes: wrong boot order in firmware, a dead drive, or a corrupt boot record — and give the test that distinguishes them. |  |
| 11 | Build the RAID recovery table: RAID 1, 5 and 10 survive one disk failure and rebuild after replacement, while RAID 0 has no redundancy so any failure means a full restore from backup. |  |
| 12 | Record the RAID rebuild warning: a rebuild puts every remaining disk under sustained full load, which is exactly when a second ageing disk in the same batch tends to fail — so verify the backup before starting one. |  |

## Verification

**Success criterion:** Your record names at least four S.M.A.R.T. attributes and states the correct action for a non-zero reallocated sector count; the recovery table gives a distinct action for all four RAID levels; and the rebuild risk is stated explicitly.

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
