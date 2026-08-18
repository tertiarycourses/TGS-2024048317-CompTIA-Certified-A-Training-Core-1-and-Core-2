# Lab 14 — Storage Devices and RAID Level Selection

> **Course:** CompTIA Certified A+ Training (Core 1 and Core 2) (TGS-2024048317)  
> **Topic 03:** Hardware — Core 1, 25% of Core 1  
> **Exam objective:** Compare HDD, SSD, NVMe and hybrid storage, and select the correct RAID level for a stated capacity, performance and redundancy requirement (Core 1 objectives 3.3 and 3.4).

## Goal

You compare storage technologies on the trade-offs that decide real purchases, then work a set of RAID selection scenarios where the wrong level means either lost data or wasted money. You finish by calculating usable capacity and fault tolerance for each level.

## What you'll produce

A storage comparison table, a RAID capacity and fault-tolerance calculation sheet, and four justified RAID selections.

## Tools and equipment

Storage device samples or references, Killercoda Ubuntu Playground, lsblk, RAID reference diagrams

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

1. Build the storage comparison table with rows for HDD, SATA SSD, NVMe M.2 SSD and SSHD and columns for interface, typical speed, cost per terabyte, moving parts and best use.
2. Record the form factors: 3.5-inch for desktop and server HDDs, 2.5-inch for laptop drives and SATA SSDs, and M.2 for the smallest SSDs.
3. Explain why NVMe is faster than SATA — it runs over PCIe lanes directly rather than through the SATA controller and its command queue.
4. Note that M.2 slots are keyed, that an M.2 slot may support SATA, NVMe or both, and that checking this before ordering avoids buying an incompatible drive.
5. Open the Killercoda Ubuntu playground and list the block devices present with their sizes and mount points.

   ```bash
   lsblk -o NAME,SIZE,TYPE,MOUNTPOINT,FSTYPE
   ```

6. Inspect the filesystem usage and free space on the playground to see how a technician confirms available capacity.

   ```bash
   df -hT
   ```

7. Build the RAID table for levels 0, 1, 5 and 10 with columns for minimum disks, usable capacity formula, fault tolerance, read performance and write performance.
8. Calculate usable capacity for four 2 TB disks in each level: RAID 0 gives 8 TB, RAID 1 gives 2 TB with two mirrored pairs or 4 TB total, RAID 5 gives 6 TB, and RAID 10 gives 4 TB.
9. Record fault tolerance for each: RAID 0 tolerates none, RAID 1 tolerates one per mirror, RAID 5 tolerates one, and RAID 10 tolerates one per mirrored pair.
10. Solve the scenario of a video editing scratch disk needing maximum speed where the data is reproducible — RAID 0 is correct because redundancy is not required.
11. Solve the scenario of a small business file server needing redundancy and reasonable capacity — RAID 5 is correct because it gives redundancy with only one disk of parity overhead.
12. Solve the remaining scenarios of a database needing both write performance and redundancy, and a boot volume in a two-disk workstation, and justify each choice.

## Test it — verification

Your capacity calculations for four 2 TB disks are correct for all four RAID levels, every scenario selection is justified against the stated requirement, and the comparison table correctly ranks the four storage types on speed and cost per terabyte.

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
