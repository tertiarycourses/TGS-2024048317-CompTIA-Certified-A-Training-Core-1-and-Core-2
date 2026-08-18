# Lab 12 — Cables and Connectors — Identification and Selection

> **Course:** CompTIA Certified A+ Training (Core 1 and Core 2) (TGS-2024048317)  
> **Topic 03:** Hardware — Core 1, 25% of Core 1  
> **Exam objective:** Identify every cable and connector on the A+ objective list by sight and select the correct one for a stated requirement (Core 1 objectives 3.1 and 3.2).

## Goal

You identify cables and connectors from physical samples or high-resolution references, record the specification that limits each one, and then solve a set of selection scenarios where choosing the wrong cable would fail. The output is a selection guide organised by the question it answers.

## What you'll produce

A completed cable and connector identification table and a solved set of eight selection scenarios.

## Tools and equipment

Cable and connector samples or reference images, specification sheets, measuring tape

## Safety

- Disconnect mains power and hold the power button for 15 seconds before working inside any machine.
- Wear an anti-static strap connected to an earthed point; hold boards and cards by their edges.
- **Never open a power supply unit or a CRT monitor** — both retain a lethal charge after being unplugged.
- Never puncture, compress or charge a swollen lithium battery; isolate it and follow hazardous disposal procedure.

## Step-by-step

1. Build the identification table with columns for connector name, cable type, what it carries, maximum speed, maximum distance and typical use.
2. Identify the network group: RJ45 for Ethernet, RJ11 for telephone, F-type for coaxial, LC, SC and ST for fibre, and record what distinguishes each visually.
3. Record the twisted-pair categories with their speed and distance limits: Cat 5e at 1 Gbps to 100 m, Cat 6 at 10 Gbps to 55 m, Cat 6a at 10 Gbps to the full 100 m.
4. Identify the video group: HDMI, DisplayPort, DVI and VGA, and record for each whether it carries digital or analog video and whether it carries audio.
5. Identify the peripheral group: USB-A, USB-B, USB-C, micro-USB, mini-USB, Lightning and Thunderbolt, and record the speed each generation supports.
6. Identify the storage group: SATA data and power, eSATA, M.2, and the legacy IDE/PATA 40-pin and SCSI 80-pin ribbon connectors.
7. Solve scenario one: a 120-metre run between two buildings needs 1 Gbps. Copper cannot exceed 100 m, so fibre is the only correct answer — record your justification.
8. Solve scenario two: a cable run passes beside fluorescent lighting and a motor room. Record why shielded twisted pair or fibre is required and unshielded is not.
9. Solve scenario three: a user needs to connect a modern laptop with only USB-C to an old VGA projector. Record why an active adapter is required, since VGA is analog and USB-C is digital.
10. Solve scenario four: a 4K display at 120 Hz is needed. Record which connector versions support this and which do not.
11. Solve the remaining scenarios covering an external drive at maximum speed, a multi-monitor daisy chain, a legacy serial console connection and a PoE camera run.
12. Complete the selection guide organised by the question asked: how far, how fast, digital or analog, and does it carry power.

## Test it — verification

Your identification table covers at least 20 connectors with speed and distance limits; every scenario answer names a specific cable or connector and justifies it against a stated limit rather than a preference.

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
