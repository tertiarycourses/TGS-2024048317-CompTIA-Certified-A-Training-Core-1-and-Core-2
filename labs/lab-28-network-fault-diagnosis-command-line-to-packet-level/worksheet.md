# Lab 28 Worksheet — Network Fault Diagnosis — Command Line to Packet Level

**Name:** ______________________    **Date:** ______________

**Exam objective:** Diagnose network faults by working the layers in order, from physical connectivity through addressing and DNS to application behaviour (Core 1 objective 5.7).

## Record as you go

| Step | What you did | What you observed |
| --- | --- | --- |
| 1 | Build the diagnostic sequence bottom-up: physical link, IP addressing, default gateway, DNS resolution, then the application itself. Testing out of order produces misleading results. |  |
| 2 | Open the Killercoda Ubuntu playground and install the diagnostic tool set. |  |
| 3 | Layer 1 — confirm the interface is physically up and has carrier, since every layer above depends on it. |  |
| 4 | Layer 2 and 3 — record the interface addresses and identify whether the address is valid, or an APIPA 169.254 address meaning DHCP failed. |  |
| 5 | Verify the address and mask in IP Calculator at https://alfredang.github.io/ipcalculator/ and confirm the host sits inside its own subnet's usable range. |  |
| 6 | Layer 3 — confirm a default route exists, then test reachability to the gateway. No default route means no traffic can leave the subnet. |  |
| 7 | Test reachability beyond the gateway by IP address, which isolates routing from DNS entirely. |  |
| 8 | Layer 7 — test DNS resolution separately, because a machine that pings an IP but not a name has a DNS fault and nothing else. |  |
| 9 | Trace the path to identify where latency is introduced or where the path stops. |  |
| 10 | Check active connections and listening sockets to confirm the application layer is actually working. |  |
| 11 | Capture traffic and analyse it in PCAP Analyzer when the commands are inconclusive, since the packets show what the tools only summarise. |  |
| 12 | Build the symptom map for APIPA address, no default gateway, pings IP but not name, high latency, jitter degrading VoIP, port flapping, intermittent wireless and limited connectivity — giving the layer, the test and the fix for each. |  |

## Verification

**Success criterion:** Every command in the sequence runs successfully on the playground, the sequence tests layers strictly bottom-up, IP Calculator confirms the host address sits within its usable range, and the symptom map assigns a layer and a specific test to all eight faults.

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
