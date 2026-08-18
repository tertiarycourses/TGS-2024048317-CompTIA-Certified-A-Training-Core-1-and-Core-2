# Lab 37 — Physical and Logical Security Control Design

> **Course:** CompTIA Certified A+ Training (Core 1 and Core 2) (TGS-2024048317)  
> **Topic 07:** Security — Core 2, 28% of Core 2  
> **Exam objective:** Select and justify physical and logical security controls for a site, applying the principle of least privilege and defence in depth (Core 2 objectives 2.1 and 2.2).

## Goal

You design the control set for a small office, working outward from the data to the perimeter. Each control must be justified by the specific threat it defeats, because a control chosen without a threat is a cost without a benefit.

## What you'll produce

A layered security design with physical and logical controls, each mapped to the threat it defeats.

## Tools and equipment

Site plan or scenario brief, security control reference, organisational policy template

## Safety

- Disconnect mains power and hold the power button for 15 seconds before working inside any machine.
- Wear an anti-static strap connected to an earthed point; hold boards and cards by their edges.
- **Never open a power supply unit or a CRT monitor** — both retain a lethal charge after being unplugged.
- Never puncture, compress or charge a swollen lithium battery; isolate it and follow hazardous disposal procedure.

## Step-by-step

1. Record the principle of defence in depth: no single control is trusted alone, so controls are layered such that defeating one still leaves the attacker facing another.
2. List the physical perimeter controls and the threat each defeats: fences and bollards against vehicle and forced entry, lighting against concealment, and cameras against undetected intrusion.
3. Record the access control vestibule, note that it admits one person at a time, and record that it specifically defeats tailgating and piggybacking.
4. Distinguish tailgating, where the attacker follows without the employee's knowledge, from piggybacking, where the employee knowingly holds the door.
5. List the entry controls: badge readers, key fobs, smart cards, conventional keys and biometrics including fingerprint, retina and palm print.
6. Record the equipment-level controls: cable locks for laptops, locking server racks, lockable equipment cabinets and privacy screens against shoulder surfing.
7. Record the detection controls: motion sensors including passive infrared, microwave and dual-technology, alarm systems on doors and windows, and guards.
8. Move to logical controls and record the principle of least privilege: every user gets exactly the access their role requires and no more.
9. Record the access control list as the mechanism, and note that ACLs are applied on file systems, on network devices and on cloud resources alike.
10. Record multifactor authentication and its three categories — something you know, something you have and something you are — and state why two passwords do not constitute MFA.
11. Distinguish a hard token, which is a physical device generating a code, from a soft token, which is an application on a phone, and record the trade-off between them.
12. Complete the design as a table with every control, its layer, the threat it defeats and its approximate cost, and state which three controls you would implement first on a limited budget.

## Test it — verification

Every control in your design is mapped to a specific threat; tailgating and piggybacking are correctly distinguished; the MFA section correctly rejects two same-category factors; and your first-three prioritisation is justified on risk rather than cost alone.

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
