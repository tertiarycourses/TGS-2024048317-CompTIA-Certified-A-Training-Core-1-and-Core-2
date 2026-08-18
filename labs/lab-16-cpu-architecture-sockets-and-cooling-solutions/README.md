# Lab 16 — CPU Architecture, Sockets and Cooling Solutions

> **Course:** CompTIA Certified A+ Training (Core 1 and Core 2) (TGS-2024048317)  
> **Topic 03:** Hardware — Core 1, 25% of Core 1  
> **Exam objective:** Compare CPU architectures, socket types and cooling solutions, and diagnose thermal problems from observed behaviour (Core 1 objectives 3.4 and 5.2).

## Goal

You compare x86-64 and ARM on the criteria that decide platform choice, match processors to sockets, and then work the thermal chain from paste to airflow — because most CPU problems in the field are thermal rather than electrical.

## What you'll produce

A CPU and socket compatibility matrix, a cooling comparison, and a thermal fault diagnostic sequence.

## Tools and equipment

Training PC, CPU and cooler samples or references, thermal paste, Task Manager, hardware monitoring utility

## Safety

- Disconnect mains power and hold the power button for 15 seconds before working inside any machine.
- Wear an anti-static strap connected to an earthed point; hold boards and cards by their edges.
- **Never open a power supply unit or a CRT monitor** — both retain a lethal charge after being unplugged.
- Never puncture, compress or charge a swollen lithium battery; isolate it and follow hazardous disposal procedure.

## Step-by-step

1. Compare x86-64 and ARM on power consumption, heat output, software compatibility and typical device class, and record which dominates desktops and which dominates mobile.
2. Record the socket types: LGA with pins on the motherboard used by Intel, PGA with pins on the processor still used by some AMD parts, and BGA soldered permanently in mobile devices.
3. Explain why a BGA processor in a laptop cannot be upgraded, and what that means when advising a customer on a slow machine.
4. Define core count, thread count and simultaneous multithreading, and explain why an eight-core processor may report sixteen logical processors.
5. Open Task Manager, go to Performance then CPU, and record the reported cores, logical processors, base speed, current speed and virtualization state.

   ```bash
   taskmgr
   ```

6. Explain thermal throttling: a processor reduces its clock speed when it exceeds its temperature limit, which protects the silicon but degrades performance.
7. Explain the difference between throttling and overclocking, and note that Intel Turbo Boost and AMD Precision Boost are sanctioned automatic overclocking within thermal headroom.
8. Compare passive cooling — heatsink, thermal paste and heat pipes with no moving parts — against active cooling with a fan, and note where each is appropriate.
9. Explain the role of thermal paste: it fills the microscopic gaps between the processor's heat spreader and the cooler base so heat can actually transfer, and record that too much is as bad as too little.
10. Compare air cooling against liquid cooling on cooling capacity, noise, cost and failure mode, noting that a liquid cooler leak can destroy the whole system.
11. Build the thermal fault diagnostic sequence: confirm all fans spin, check intakes and heatsink fins for dust, verify the cooler is properly seated, check paste condition, then check ambient temperature and case airflow.
12. Monitor processor temperature under load and record the idle temperature, the load temperature and whether the clock speed dropped, then state whether the cooling is adequate.

## Test it — verification

Task Manager confirms the core and logical processor counts and the virtualization state; your diagnostic sequence orders the checks from cheapest to most invasive; and the temperature record supports a stated conclusion about cooling adequacy.

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
