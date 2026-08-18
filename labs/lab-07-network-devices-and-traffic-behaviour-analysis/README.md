# Lab 7 — Network Devices and Traffic Behaviour Analysis

> **Course:** CompTIA Certified A+ Training (Core 1 and Core 2) (TGS-2024048317)  
> **Topic 02:** Networking — Core 1, 23% of Core 1  
> **Exam objective:** Distinguish hub, switch, router, firewall and access point by the layer they operate at and the traffic behaviour each produces (Core 1 objectives 2.2 and 2.3).

## Goal

Rather than reading device descriptions, you infer device behaviour from captured traffic. Using PCAP Analyzer you examine a capture, identify the MAC and IP conversations, and reason about which device forwarded each frame and why.

## What you'll produce

A device comparison matrix and a written traffic analysis identifying the forwarding decision at each layer.

## Tools and equipment

PCAP Analyzer (https://alfredang.github.io/pcapanalyzer/), device reference diagrams

### Browser tools used in this lab

- **PCAP Analyzer** — <https://alfredang.github.io/pcapanalyzer/>

![PCAP Analyzer interface map](../../courseware/assets/tool-pcapanalyzer.png)

*PCAP Analyzer — the panels and fields this lab uses.*

## Safety

- Disconnect mains power and hold the power button for 15 seconds before working inside any machine.
- Wear an anti-static strap connected to an earthed point; hold boards and cards by their edges.
- **Never open a power supply unit or a CRT monitor** — both retain a lethal charge after being unplugged.
- Never puncture, compress or charge a swollen lithium battery; isolate it and follow hazardous disposal procedure.

## Step-by-step

1. Open PCAP Analyzer at https://alfredang.github.io/pcapanalyzer/ and click the Sample button to generate a demonstration capture. Nothing is uploaded — parsing happens in your browser.
2. Record the four dashboard metrics: packet count, total bytes, capture duration and average packet size.
3. Open the protocol distribution view and list every protocol present with its share of the capture.
4. Open Top talkers and record the three most active endpoints by traffic volume, noting their addresses.
5. Open Top conversations and identify which pairs of hosts exchange the most data, then state what kind of session each pair most likely represents.
6. Select an individual packet in the packets table and open its detail view to read the source, destination, protocol and length.
7. From the packet detail, identify the Layer 2 MAC addresses and the Layer 3 IP addresses, and explain which one a switch uses to forward and which one a router uses.
8. Build the device comparison matrix with rows for hub, switch, router, firewall and access point and columns for OSI layer, forwarding basis, collision domains, broadcast domains and typical use.
9. Explain in writing why a hub creates one collision domain across all ports while a switch creates one per port, and what that means for network performance.
10. Explain why a switch forwards a broadcast frame out of every port but a router does not forward it at all, and connect this to why VLANs are needed.
11. Apply the protocol filter in the packets table to isolate one protocol, and record how the packet count changes.
12. Write a short conclusion stating what the capture reveals about the network — how many broadcast domains are visible, and whether a router is present in the path.

## Test it — verification

Your matrix correctly assigns each of the five devices to its OSI layer and forwarding basis; your analysis names the specific MAC and IP addresses observed; and the conclusion is supported by evidence from the capture rather than from theory alone.

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
