# Lab 31 Worksheet — Windows Networking and Repair Commands

**Name:** ______________________    **Date:** ______________

**Exam objective:** Use Windows networking and repair commands to diagnose connectivity and repair system file corruption (Core 2 objective 1.2).

## Record as you go

| Step | What you did | What you observed |
| --- | --- | --- |
| 1 | Display the full network configuration and record the IP address, subnet mask, default gateway, DNS servers, DHCP server and MAC address. |  |
| 2 | Release and renew the DHCP lease, recording the address before and after to confirm the DHCP server responded. |  |
| 3 | Display and then clear the DNS resolver cache, and record when clearing it is the correct fix — after a DNS record changes but the old answer is still cached. |  |
| 4 | Test the loopback address first to confirm the TCP/IP stack itself is working before testing anything external. |  |
| 5 | Test the default gateway to separate a local network fault from an internet fault. |  |
| 6 | Test an external IP address and then an external name, and record that success on the IP but failure on the name isolates the fault to DNS. |  |
| 7 | Trace the route to a destination and identify where latency increases sharply or where the path stops. |  |
| 8 | Query DNS directly and record the resolver used and the addresses returned. |  |
| 9 | List active connections with the owning process ID so you can identify what is actually using the network. |  |
| 10 | Run the system file checker to scan and repair protected system files, and record the result it reports. |  |
| 11 | Repair the component store that sfc itself depends on, and record why DISM must be run first when sfc reports it cannot fix the files. |  |
| 12 | Check the disk for file system errors, and record the difference between /f which fixes errors and /r which also locates bad sectors and takes far longer. |  |

## Verification

**Success criterion:** Every command produces output you have interpreted in writing; ipconfig /all output identifies all six required fields; you correctly state that ping to IP succeeding while ping to name fails means DNS; and the sfc result is recorded with its meaning.

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
