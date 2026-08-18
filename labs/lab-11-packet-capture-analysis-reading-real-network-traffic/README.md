# Lab 11 — Packet Capture Analysis — Reading Real Network Traffic

> **Course:** CompTIA Certified A+ Training (Core 1 and Core 2) (TGS-2024048317)  
> **Topic 02:** Networking — Core 1, 23% of Core 1  
> **Exam objective:** Analyse a packet capture to identify protocols, conversations and anomalies, and use the evidence to support a network diagnosis (Core 1 objectives 2.1 and 5.7).

## Goal

You work a capture the way a support engineer does: start from the summary statistics, narrow by protocol, follow the largest conversation, and read individual packets only once you know which ones matter. The output is a written diagnosis supported by named evidence.

## What you'll produce

A written traffic analysis report with protocol breakdown, conversation analysis and a supported diagnosis.

## Tools and equipment

PCAP Analyzer (https://alfredang.github.io/pcapanalyzer/), Killercoda Ubuntu Playground, tcpdump

### Browser tools used in this lab

- **PCAP Analyzer** — <https://alfredang.github.io/pcapanalyzer/>
- **Killercoda Ubuntu Playground** — <https://killercoda.com/playgrounds/scenario/ubuntu>

![PCAP Analyzer interface map](../../courseware/assets/tool-pcapanalyzer.png)

*PCAP Analyzer — the panels and fields this lab uses.*

![Killercoda Ubuntu Playground interface map](../../courseware/assets/tool-killercoda.png)

*Killercoda Ubuntu Playground — the panels and fields this lab uses.*

## Safety

- Disconnect mains power and hold the power button for 15 seconds before working inside any machine.
- Wear an anti-static strap connected to an earthed point; hold boards and cards by their edges.
- **Never open a power supply unit or a CRT monitor** — both retain a lethal charge after being unplugged.
- Never puncture, compress or charge a swollen lithium battery; isolate it and follow hazardous disposal procedure.

## Step-by-step

1. Open the Killercoda Ubuntu playground and install tcpdump so you can generate your own capture rather than only using sample data.

   ```bash
   apt-get update -qq && apt-get install -y tcpdump curl
   ```

2. Start a capture on the default interface, writing to a file, and limit it to 200 packets so the capture ends by itself.

   ```bash
   tcpdump -i any -c 200 -w /root/capture.pcap &
   ```

3. While the capture runs, generate varied traffic so the capture contains several protocols to analyse.

   ```bash
   sleep 2; curl -s https://example.com > /dev/null; curl -s http://neverssl.com > /dev/null; getent hosts google.com
   ```

4. Wait for the capture to finish and confirm the file exists with a non-zero size.

   ```bash
   wait; ls -lh /root/capture.pcap
   ```

5. Read the capture summary on the command line to see what was captured before moving to the browser tool.

   ```bash
   tcpdump -r /root/capture.pcap -nn -c 20
   ```

6. Download the capture file from the playground, or if download is unavailable, open PCAP Analyzer and use the Sample button instead.
7. Open https://alfredang.github.io/pcapanalyzer/ and load the capture by dragging the file onto the drop area or using the file browser.
8. Record the four dashboard statistics and the detected file format, then state what the average packet size suggests about the traffic mix.
9. Examine the protocol distribution and record each protocol with its share, then identify which protocols are encrypted and which are in clear text.
10. Open Top conversations, select the pair exchanging the most data, and state what kind of session it represents based on the ports involved.
11. Filter the packets table to a single protocol, select a packet, and read its detail and hex view to identify the source port, destination port and payload length.
12. Write the diagnosis: state one observation about the network that the capture supports, name the specific packets or conversations that evidence it, and state what you would capture next to confirm it.

## Test it — verification

tcpdump produces a capture file containing at least three distinct protocols, PCAP Analyzer loads it and reports the protocol distribution, and your written diagnosis cites specific addresses, ports and packet numbers as evidence rather than general statements.

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
