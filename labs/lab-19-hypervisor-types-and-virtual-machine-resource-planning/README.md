# Lab 19 — Hypervisor Types and Virtual Machine Resource Planning

> **Course:** CompTIA Certified A+ Training (Core 1 and Core 2) (TGS-2024048317)  
> **Topic 04:** Virtualization and Cloud Computing — Core 1, 11% of Core 1  
> **Exam objective:** Distinguish Type 1 from Type 2 hypervisors, plan virtual machine resource allocation and identify the firmware prerequisite for virtualization (Core 1 objective 4.2).

## Goal

You compare the two hypervisor types on where they run and what they are for, verify that hardware virtualization support is enabled, then plan resource allocation for several VMs on one host — the calculation that decides whether a host performs or crawls.

## What you'll produce

A hypervisor comparison table, a verified virtualization-enabled host and a resource allocation plan for four VMs.

## Tools and equipment

Windows host, Task Manager, systeminfo, BIOS/UEFI, VirtualBox or Hyper-V, hypervisor references

## Safety

- Disconnect mains power and hold the power button for 15 seconds before working inside any machine.
- Wear an anti-static strap connected to an earthed point; hold boards and cards by their edges.
- **Never open a power supply unit or a CRT monitor** — both retain a lethal charge after being unplugged.
- Never puncture, compress or charge a swollen lithium battery; isolate it and follow hazardous disposal procedure.

## Step-by-step

1. Build the comparison table with rows for Type 1 and Type 2 and columns for where it runs, examples, typical use, performance and management overhead.
2. Record that a Type 1 bare-metal hypervisor such as VMware ESXi, Microsoft Hyper-V Server or Citrix Hypervisor runs directly on hardware with no host OS beneath it.
3. Record that a Type 2 hosted hypervisor such as VirtualBox, VMware Workstation or Parallels runs as an application on top of a desktop operating system.
4. Explain why Type 1 performs better — there is no host operating system competing for CPU and memory or adding a scheduling layer.
5. Check whether hardware virtualization support is enabled on your host, since no 64-bit guest will start without it.

   ```bash
   systeminfo | findstr /C:"Hyper-V"
   ```

6. Confirm the same from Task Manager by opening Performance then CPU and reading the Virtualization field.

   ```bash
   taskmgr
   ```

7. If virtualization is disabled, record the exact BIOS/UEFI menu path where Intel VT-x or AMD-V is enabled, and note that this is the single most common cause of a VM refusing to start.
8. Record the host's total physical resources: CPU cores and logical processors, total RAM, and free disk space.

   ```bash
   systeminfo | findstr /C:"Total Physical Memory" /C:"Processor"
   ```

9. Plan four VMs — a Windows desktop, a Linux server, a Windows server and a test machine — assigning vCPU, RAM and disk to each based on the guest OS minimum plus a working margin.
10. Sum the planned RAM across all four VMs and confirm the total leaves at least 4 GB for the host, since over-committing RAM is the fastest way to bring a host to a halt.
11. Explain the difference between a thick-provisioned disk, which claims all its space immediately, and a thin-provisioned disk, which grows as it fills, and state the risk of over-committing thin disks.
12. Explain what a snapshot does, why it is not a backup, and why leaving snapshots in place for weeks degrades performance and consumes disk.

## Test it — verification

Virtualization support is confirmed enabled on the host, your allocation plan's total RAM leaves at least 4 GB for the host, and every VM is allocated at or above its guest OS minimum with the margin stated.

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
