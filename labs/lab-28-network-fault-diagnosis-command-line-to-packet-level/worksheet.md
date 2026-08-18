# Lab 28 Worksheet — Network Fault Diagnosis — Command Line to Packet Level

**Name:** ______________________    **Date:** ______________

**Exam objective:** Diagnose network faults by working the layers in order, from physical connectivity through addressing and DNS to application behaviour (Core 1 objective 5.7).

## Record as you go

| Step | What you did | What you observed |
| --- | --- | --- |
| 1 | Build the diagnostic sequence bottom-up: physical link, IP addressi... |  |
| 2 | Open the Killercoda Ubuntu playground and install the diagnostic to... |  |
| 3 | Layer 1 — confirm the interface is physically up and has carrier, s... |  |
| 4 | Layer 2 and 3 — record the interface addresses and identify whether... |  |
| 5 | Verify the address and mask in IP Calculator at https://alfredang.g... |  |
| 6 | Layer 3 — confirm a default route exists, then test reachability to... |  |
| 7 | Test reachability beyond the gateway by IP address, which isolates ... |  |
| 8 | Layer 7 — test DNS resolution separately, because a machine that pi... |  |
| 9 | Trace the path to identify where latency is introduced or where the... |  |
| 10 | Check active connections and listening sockets to confirm the appli... |  |
| 11 | Capture traffic and analyse it in PCAP Analyzer when the commands a... |  |
| 12 | Build the symptom map for APIPA address, no default gateway, pings ... |  |

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
