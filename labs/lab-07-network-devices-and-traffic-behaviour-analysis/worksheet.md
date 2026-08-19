# Lab 7 Worksheet — Network Devices and Traffic Behaviour Analysis

**Name:** ______________________    **Date:** ______________

**Exam objective:** Distinguish hub, switch, router, firewall and access point by the layer they operate at and the traffic behaviour each produces (Core 1 objectives 2.2 and 2.3).

## Record as you go

| Step | What you did | What you observed |
| --- | --- | --- |
| 1 | Open PCAP Analyzer at https://alfredang.github.io/pcapanalyzer/ and click the Sample button to generate a demonstration capture. Nothing is uploaded — parsing happens in your browser. |  |
| 2 | Record the four dashboard metrics: packet count, total bytes, capture duration and average packet size. |  |
| 3 | Open the protocol distribution view and list every protocol present with its share of the capture. |  |
| 4 | Open Top talkers and record the three most active endpoints by traffic volume, noting their addresses. |  |
| 5 | Open Top conversations and identify which pairs of hosts exchange the most data, then state what kind of session each pair most likely represents. |  |
| 6 | Select an individual packet in the packets table and open its detail view to read the source, destination, protocol and length. |  |
| 7 | From the packet detail, identify the Layer 2 MAC addresses and the Layer 3 IP addresses, and explain which one a switch uses to forward and which one a router uses. |  |
| 8 | Build the device comparison matrix with rows for hub, switch, router, firewall and access point and columns for OSI layer, forwarding basis, collision domains, broadcast domains and typical use. |  |
| 9 | Explain in writing why a hub creates one collision domain across all ports while a switch creates one per port, and what that means for network performance. |  |
| 10 | Explain why a switch forwards a broadcast frame out of every port but a router does not forward it at all, and connect this to why VLANs are needed. |  |
| 11 | Apply the protocol filter in the packets table to isolate one protocol, and record how the packet count changes. |  |
| 12 | Write a short conclusion stating what the capture reveals about the network — how many broadcast domains are visible, and whether a router is present in the path. |  |

## Verification

**Success criterion:** Your matrix correctly assigns each of the five devices to its OSI layer and forwarding basis; your analysis names the specific MAC and IP addresses observed; and the conclusion is supported by evidence from the capture rather than from theory alone.

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
