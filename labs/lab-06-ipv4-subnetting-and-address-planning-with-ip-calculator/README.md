# Lab 6 — IPv4 Subnetting and Address Planning with IP Calculator

> **Course:** CompTIA Certified A+ Training (Core 1 and Core 2) (TGS-2024048317)  
> **Topic 02:** Networking — Core 1, 23% of Core 1  
> **Exam objective:** Calculate subnet masks, network and broadcast addresses, usable host ranges and CIDR notation, and design an address plan for a SOHO network (Core 1 objective 2.5).

## Goal

You use IP Calculator to work subnetting from both directions — decoding a given address and designing a plan to meet a host requirement — then verify every result by hand so you can reproduce it in an exam where no calculator is allowed.

## What you'll produce

A verified subnetting worksheet and a complete four-subnet SOHO address plan exported as CSV.

## Tools and equipment

IP Calculator (https://alfredang.github.io/ipcalculator/), Killercoda Ubuntu Playground, ipcalc

### Browser tools used in this lab

- **IP Calculator** — <https://alfredang.github.io/ipcalculator/>
- **Killercoda Ubuntu Playground** — <https://killercoda.com/playgrounds/scenario/ubuntu>

![IP Calculator interface map](../../courseware/assets/tool-ipcalculator.png)

*IP Calculator — the panels and fields this lab uses.*

![Killercoda Ubuntu Playground interface map](../../courseware/assets/tool-killercoda.png)

*Killercoda Ubuntu Playground — the panels and fields this lab uses.*

## Safety

- Disconnect mains power and hold the power button for 15 seconds before working inside any machine.
- Wear an anti-static strap connected to an earthed point; hold boards and cards by their edges.
- **Never open a power supply unit or a CRT monitor** — both retain a lethal charge after being unplugged.
- Never puncture, compress or charge a swollen lithium battery; isolate it and follow hazardous disposal procedure.

## Step-by-step

1. Open IP Calculator at https://alfredang.github.io/ipcalculator/ and select the IPv4 tab.
2. Enter 192.168.10.75/24 and record the network address, broadcast address, first and last usable host, netmask in dotted decimal, and the usable host count.
3. Change the prefix to /26 with the same address and record how the network address, broadcast address and usable host count change.
4. Verify the /26 result by hand: 32 minus 26 leaves 6 host bits, 2 to the power 6 is 64 addresses per block, minus 2 reserved gives 62 usable hosts. Confirm this matches the tool.
5. Enter 172.16.0.0/12 and 10.0.0.0/8 in turn, and confirm from the output that all three RFC 1918 private ranges are non-routable on the internet.
6. Enter 169.254.14.9/16 and record what this range signifies — an APIPA address assigned when no DHCP server answered.
7. Design a SOHO plan from the 192.168.20.0/24 block for four departments needing 50, 25, 10 and 5 hosts. Choose the smallest prefix that satisfies each requirement.
8. Verify each chosen prefix in IP Calculator: /26 gives 62 usable for the 50-host subnet, /27 gives 30 for the 25-host subnet, /28 gives 14 for the 10-host subnet and /29 gives 6 for the 5-host subnet.
9. Switch to the Batch tab, paste all four subnets one per line with a comment naming each department, and process them together.
10. Export the batch results to CSV using the export control, and keep the file as the address-plan deliverable.
11. Open the Killercoda Ubuntu playground and install ipcalc to cross-check your work with an independent tool.

   ```bash
   apt-get update -qq && apt-get install -y ipcalc
   ```

12. Cross-check the first subnet on the command line and confirm the network, broadcast and host range match IP Calculator exactly.

   ```bash
   ipcalc 192.168.20.0/26
   ```


## Test it — verification

Every subnet in your plan satisfies its host requirement with no wasted block larger than necessary, the hand calculation matches the IP Calculator output for the /26 case, ipcalc agrees with the browser tool, and the CSV export contains all four subnets.

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
