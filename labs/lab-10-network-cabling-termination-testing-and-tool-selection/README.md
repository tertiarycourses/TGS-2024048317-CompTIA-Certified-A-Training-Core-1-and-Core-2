# Lab 10 — Network Cabling — Termination, Testing and Tool Selection

> **Course:** CompTIA Certified A+ Training (Core 1 and Core 2) (TGS-2024048317)  
> **Topic 02:** Networking — Core 1, 23% of Core 1  
> **Exam objective:** Terminate twisted-pair cable to T568B, test it end to end, and select the correct tool for each cabling task (Core 1 objectives 2.3 and 3.1).

## Goal

You terminate a patch cable to the T568B standard, test it with a cable tester, and deliberately create a fault to see how the tester reports it. You then build a tool selection guide matching each networking tool to the single question it answers.

## What you'll produce

A terminated and tested patch cable, a fault-injection test record, and a tool selection guide.

## Tools and equipment

Crimper, RJ45 plugs, Cat 5e/6 cable, cable stripper, cable tester, toner probe, punch-down tool, loopback plug

## Safety

- Disconnect mains power and hold the power button for 15 seconds before working inside any machine.
- Wear an anti-static strap connected to an earthed point; hold boards and cards by their edges.
- **Never open a power supply unit or a CRT monitor** — both retain a lethal charge after being unplugged.
- Never puncture, compress or charge a swollen lithium battery; isolate it and follow hazardous disposal procedure.

## Step-by-step

1. Write out the T568B colour order from memory before you begin: white-orange, orange, white-green, blue, white-blue, green, white-brown, brown.
2. Strip about 25 mm of the outer jacket with the cable stripper, taking care not to nick the insulation of the individual conductors.
3. Untwist and straighten the four pairs, then arrange all eight conductors flat in the T568B order you wrote down.
4. Trim the conductors square to about 12 mm so they will all reach the end of the plug while the jacket still enters the strain relief.
5. Insert the conductors fully into the RJ45 plug, confirm through the clear plastic that each wire reaches the end and the order is still correct, then crimp firmly.
6. Terminate the far end to T568B as well, which makes this a straight-through patch cable rather than a crossover.
7. Test the cable with the cable tester and confirm the lights advance 1 through 8 in sequence on both the main unit and the remote.
8. Deliberately make a second cable with two conductors swapped, test it, and record how the tester reports the crossed pair.
9. Make a third cable with one conductor not fully seated, test it, and record how the tester reports the open circuit.
10. Use the toner probe on a bundle: attach the tone generator to one known end and use the probe to find the matching far end.
11. Terminate a cable to a patch panel or keystone jack with the punch-down tool, noting that the blade trims the excess conductor as it seats.
12. Build the tool selection guide: crimper terminates plugs, stripper removes the jacket, cable tester verifies the pinout, toner probe identifies a cable in a bundle, punch-down seats wires in a block, loopback plug tests a port, and a Wi-Fi analyser shows channel congestion.

## Test it — verification

Your good cable passes the tester with all eight lights in sequence on both ends; the two faulty cables produce distinctly different tester results that you have recorded; and the tool guide matches all seven tools to the specific question each answers.

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
