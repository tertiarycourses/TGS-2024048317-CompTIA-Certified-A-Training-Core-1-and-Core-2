# Lab 6 Worksheet — IPv4 Subnetting and Address Planning with IP Calculator

**Name:** ______________________    **Date:** ______________

**Exam objective:** Calculate subnet masks, network and broadcast addresses, usable host ranges and CIDR notation, and design an address plan for a SOHO network (Core 1 objective 2.5).

## Record as you go

| Step | What you did | What you observed |
| --- | --- | --- |
| 1 | Open IP Calculator at https://alfredang.github.io/ipcalculator/ and select the IPv4 tab. |  |
| 2 | Enter 192.168.10.75/24 and record the network address, broadcast address, first and last usable host, netmask in dotted decimal, and the usable host count. |  |
| 3 | Change the prefix to /26 with the same address and record how the network address, broadcast address and usable host count change. |  |
| 4 | Verify the /26 result by hand: 32 minus 26 leaves 6 host bits, 2 to the power 6 is 64 addresses per block, minus 2 reserved gives 62 usable hosts. Confirm this matches the tool. |  |
| 5 | Enter 172.16.0.0/12 and 10.0.0.0/8 in turn, and confirm from the output that all three RFC 1918 private ranges are non-routable on the internet. |  |
| 6 | Enter 169.254.14.9/16 and record what this range signifies — an APIPA address assigned when no DHCP server answered. |  |
| 7 | Design a SOHO plan from the 192.168.20.0/24 block for four departments needing 50, 25, 10 and 5 hosts. Choose the smallest prefix that satisfies each requirement. |  |
| 8 | Verify each chosen prefix in IP Calculator: /26 gives 62 usable for the 50-host subnet, /27 gives 30 for the 25-host subnet, /28 gives 14 for the 10-host subnet and /29 gives 6 for the 5-host subnet. |  |
| 9 | Switch to the Batch tab, paste all four subnets one per line with a comment naming each department, and process them together. |  |
| 10 | Export the batch results to CSV using the export control, and keep the file as the address-plan deliverable. |  |
| 11 | Open the Killercoda Ubuntu playground and install ipcalc to cross-check your work with an independent tool. |  |
| 12 | Cross-check the first subnet on the command line and confirm the network, broadcast and host range match IP Calculator exactly. |  |

## Verification

**Success criterion:** Every subnet in your plan satisfies its host requirement with no wasted block larger than necessary, the hand calculation matches the IP Calculator output for the /26 case, ipcalc agrees with the browser tool, and the CSV export contains all four subnets.

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
