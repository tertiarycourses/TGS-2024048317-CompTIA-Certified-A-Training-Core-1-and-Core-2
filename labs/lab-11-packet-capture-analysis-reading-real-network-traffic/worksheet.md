# Lab 11 Worksheet — Packet Capture Analysis — Reading Real Network Traffic

**Name:** ______________________    **Date:** ______________

**Exam objective:** Analyse a packet capture to identify protocols, conversations and anomalies, and use the evidence to support a network diagnosis (Core 1 objectives 2.1 and 5.7).

## Record as you go

| Step | What you did | What you observed |
| --- | --- | --- |
| 1 | Open the Killercoda Ubuntu playground and install tcpdump so you can generate your own capture rather than only using sample data. |  |
| 2 | Start a capture on the default interface, writing to a file, and limit it to 200 packets so the capture ends by itself. |  |
| 3 | While the capture runs, generate varied traffic so the capture contains several protocols to analyse. |  |
| 4 | Wait for the capture to finish and confirm the file exists with a non-zero size. |  |
| 5 | Read the capture summary on the command line to see what was captured before moving to the browser tool. |  |
| 6 | Download the capture file from the playground, or if download is unavailable, open PCAP Analyzer and use the Sample button instead. |  |
| 7 | Open https://alfredang.github.io/pcapanalyzer/ and load the capture by dragging the file onto the drop area or using the file browser. |  |
| 8 | Record the four dashboard statistics and the detected file format, then state what the average packet size suggests about the traffic mix. |  |
| 9 | Examine the protocol distribution and record each protocol with its share, then identify which protocols are encrypted and which are in clear text. |  |
| 10 | Open Top conversations, select the pair exchanging the most data, and state what kind of session it represents based on the ports involved. |  |
| 11 | Filter the packets table to a single protocol, select a packet, and read its detail and hex view to identify the source port, destination port and payload length. |  |
| 12 | Write the diagnosis: state one observation about the network that the capture supports, name the specific packets or conversations that evidence it, and state what you would capture next to confirm it. |  |

## Verification

**Success criterion:** tcpdump produces a capture file containing at least three distinct protocols, PCAP Analyzer loads it and reports the protocol distribution, and your written diagnosis cites specific addresses, ports and packet numbers as evidence rather than general statements.

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
