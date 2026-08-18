# Lab 24 — Storage and RAID Fault Diagnosis with S.M.A.R.T.

> **Course:** CompTIA Certified A+ Training (Core 1 and Core 2) (TGS-2024048317)  
> **Topic 05:** Hardware and Network Troubleshooting — Core 1, 28% of Core 1  
> **Exam objective:** Diagnose storage faults using S.M.A.R.T. data, symptom analysis and RAID status, and choose the correct recovery action for each RAID level (Core 1 objective 5.3).

## Goal

Storage faults are the ones where a wrong move destroys the data permanently, so the order of actions matters more than in any other troubleshooting lab. You read S.M.A.R.T. attributes, interpret the warning signs, and decide the recovery action per RAID level.

## What you'll produce

A S.M.A.R.T. attribute interpretation record, a storage symptom map and a RAID recovery decision table.

## Tools and equipment

Training PC, Killercoda Ubuntu Playground, smartctl, chkdsk, Disk Management, wmic

### Browser tools used in this lab

- **Killercoda Ubuntu Playground** — <https://killercoda.com/playgrounds/scenario/ubuntu>

![Killercoda Ubuntu Playground interface map](../../courseware/assets/tool-killercoda.png)

*Killercoda Ubuntu Playground — the panels and fields this lab uses.*

## Safety

- Disconnect mains power and hold the power button for 15 seconds before working inside any machine.
- Wear an anti-static strap connected to an earthed point; hold boards and cards by their edges.
- **Never open a power supply unit or a CRT monitor** — both retain a lethal charge after being unplugged.
- Never puncture, compress or charge a swollen lithium battery; isolate it and follow hazardous disposal procedure.

## Step-by-step

1. Record the first rule of storage troubleshooting: if the data matters and the drive is failing, back it up before you do anything else. Diagnostics can be the final straw for a dying drive.
2. Check drive health on Windows using the built-in interface and record the status reported for each physical disk.

   ```bash
   wmic diskdrive get model,status,size
   ```

3. Open Disk Management and record each volume's file system, capacity, free space and status.

   ```bash
   diskmgmt.msc
   ```

4. Open the Killercoda Ubuntu playground and install the S.M.A.R.T. monitoring tools to read raw drive attributes.

   ```bash
   apt-get update -qq && apt-get install -y smartmontools
   ```

5. List the block devices available so you know which device names to query.

   ```bash
   lsblk -o NAME,SIZE,TYPE,MOUNTPOINT
   ```

6. Read the S.M.A.R.T. attributes for a device and record the overall health self-assessment result.

   ```bash
   smartctl -H /dev/sda || echo 'Virtual device - review the attribute reference instead'
   ```

7. Record the S.M.A.R.T. attributes that matter most: reallocated sector count, current pending sector count, offline uncorrectable and read error rate — any non-zero value on the first three is a replace signal.
8. Record the correct response to a S.M.A.R.T. warning: back up immediately and replace the drive. S.M.A.R.T. reports a drive that is already failing, not one that might fail eventually.
9. Map the audible and behavioural symptoms: clicking or grinding means imminent mechanical failure, and extended read and write times or falling IOPS mean the drive is retrying failing sectors.
10. Map 'bootable device not found' to its three causes: wrong boot order in firmware, a dead drive, or a corrupt boot record — and give the test that distinguishes them.
11. Build the RAID recovery table: RAID 1, 5 and 10 survive one disk failure and rebuild after replacement, while RAID 0 has no redundancy so any failure means a full restore from backup.
12. Record the RAID rebuild warning: a rebuild puts every remaining disk under sustained full load, which is exactly when a second ageing disk in the same batch tends to fail — so verify the backup before starting one.

## Test it — verification

Your record names at least four S.M.A.R.T. attributes and states the correct action for a non-zero reallocated sector count; the recovery table gives a distinct action for all four RAID levels; and the rebuild risk is stated explicitly.

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
