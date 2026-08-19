# Lab 19 Worksheet — Hypervisor Types and Virtual Machine Resource Planning

**Name:** ______________________    **Date:** ______________

**Exam objective:** Distinguish Type 1 from Type 2 hypervisors, plan virtual machine resource allocation and identify the firmware prerequisite for virtualization (Core 1 objective 4.2).

## Record as you go

| Step | What you did | What you observed |
| --- | --- | --- |
| 1 | Build the comparison table with rows for Type 1 and Type 2 and columns for where it runs, examples, typical use, performance and management overhead. |  |
| 2 | Record that a Type 1 bare-metal hypervisor such as VMware ESXi, Microsoft Hyper-V Server or Citrix Hypervisor runs directly on hardware with no host OS beneath it. |  |
| 3 | Record that a Type 2 hosted hypervisor such as VirtualBox, VMware Workstation or Parallels runs as an application on top of a desktop operating system. |  |
| 4 | Explain why Type 1 performs better — there is no host operating system competing for CPU and memory or adding a scheduling layer. |  |
| 5 | Check whether hardware virtualization support is enabled on your host, since no 64-bit guest will start without it. |  |
| 6 | Confirm the same from Task Manager by opening Performance then CPU and reading the Virtualization field. |  |
| 7 | If virtualization is disabled, record the exact BIOS/UEFI menu path where Intel VT-x or AMD-V is enabled, and note that this is the single most common cause of a VM refusing to start. |  |
| 8 | Record the host's total physical resources: CPU cores and logical processors, total RAM, and free disk space. |  |
| 9 | Plan four VMs — a Windows desktop, a Linux server, a Windows server and a test machine — assigning vCPU, RAM and disk to each based on the guest OS minimum plus a working margin. |  |
| 10 | Sum the planned RAM across all four VMs and confirm the total leaves at least 4 GB for the host, since over-committing RAM is the fastest way to bring a host to a halt. |  |
| 11 | Explain the difference between a thick-provisioned disk, which claims all its space immediately, and a thin-provisioned disk, which grows as it fills, and state the risk of over-committing thin disks. |  |
| 12 | Explain what a snapshot does, why it is not a backup, and why leaving snapshots in place for weeks degrades performance and consumes disk. |  |

## Verification

**Success criterion:** Virtualization support is confirmed enabled on the host, your allocation plan's total RAM leaves at least 4 GB for the host, and every VM is allocated at or above its guest OS minimum with the margin stated.

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
