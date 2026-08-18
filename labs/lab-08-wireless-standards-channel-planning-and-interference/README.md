# Lab 8 — Wireless Standards, Channel Planning and Interference

> **Course:** CompTIA Certified A+ Training (Core 1 and Core 2) (TGS-2024048317)  
> **Topic 02:** Networking — Core 1, 23% of Core 1  
> **Exam objective:** Compare 802.11 standards and frequency bands, and design a channel plan that avoids co-channel and adjacent-channel interference (Core 1 objective 2.3).

## Goal

You compare the 2.4 GHz and 5 GHz bands on the criteria that decide real deployments, then design a channel plan for a three-access-point office and justify every channel choice against the non-overlapping channel constraint.

## What you'll produce

An 802.11 standards comparison table and a justified three-AP channel plan with a coverage sketch.

## Tools and equipment

Wi-Fi analyser application on a mobile device or laptop, 802.11 standards reference, floor plan sketch

## Safety

- Disconnect mains power and hold the power button for 15 seconds before working inside any machine.
- Wear an anti-static strap connected to an earthed point; hold boards and cards by their edges.
- **Never open a power supply unit or a CRT monitor** — both retain a lethal charge after being unplugged.
- Never puncture, compress or charge a swollen lithium battery; isolate it and follow hazardous disposal procedure.

## Step-by-step

1. Build the standards table with rows for 802.11a, b, g, n, ac and ax and columns for frequency band, maximum theoretical throughput, channel width and backward compatibility.
2. Record that 2.4 GHz offers only three non-overlapping channels — 1, 6 and 11 — and explain from channel width why any other choice overlaps.
3. Record that 5 GHz offers around 24 non-overlapping 20 MHz channels, and note the trade-off: more channels and more speed, but shorter range and poorer wall penetration.
4. Open a Wi-Fi analyser on your device and record every visible SSID with its channel, band and signal strength in dBm.
5. Identify from your scan which 2.4 GHz channels are most congested in your location and which of 1, 6 or 11 is least used.
6. Interpret the signal strengths you recorded: better than -50 dBm is excellent, -60 is good, -70 is usable and worse than -80 is unreliable.
7. Sketch a three-room office floor plan and place three access points to give overlapping coverage with no dead zones.
8. Assign 2.4 GHz channels 1, 6 and 11 to the three access points so that no two adjacent cells share a channel, and mark each on the sketch.
9. Explain the difference between co-channel interference, where cells share a channel and must take turns, and adjacent-channel interference, where overlapping channels corrupt each other's transmissions.
10. List five physical sources of 2.4 GHz interference in a typical office — microwave ovens, cordless phones, Bluetooth devices, fluorescent ballasts and thick or metal-reinforced walls.
11. State the security configuration for all three access points: WPA3 where supported, WPA2 with AES-CCMP as the minimum, and never WEP or WPA with TKIP.
12. Write the justification paragraph explaining why your channel assignment minimises interference, referencing the non-overlapping constraint explicitly.

## Test it — verification

Your channel plan uses only channels 1, 6 and 11 in the 2.4 GHz band with no adjacent cells sharing a channel; the scan records real SSIDs with channel and dBm; and the justification correctly distinguishes co-channel from adjacent-channel interference.

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
