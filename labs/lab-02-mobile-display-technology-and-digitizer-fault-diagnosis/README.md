# Lab 2 — Mobile Display Technology and Digitizer Fault Diagnosis

> **Course:** CompTIA Certified A+ Training (Core 1 and Core 2) (TGS-2024048317)  
> **Topic 01:** Mobile Devices — Core 1, 13% of Core 1  
> **Exam objective:** Compare LCD, IPS, VA and OLED panel technologies and correctly distinguish a display panel fault from a backlight, inverter or digitizer fault (Core 1 objective 1.2).

## Goal

You compare the four panel technologies on the criteria that matter in support work, then work through a set of display symptoms and decide, for each, which component has actually failed. The output is a diagnostic decision table you can use on the job.

## What you'll produce

A panel technology comparison table and a symptom-to-component diagnostic decision table covering eight display faults.

## Tools and equipment

Reference displays or specification sheets, a torch, a smartphone with an OLED screen, a laptop with an LCD panel

## Safety

- Disconnect mains power and hold the power button for 15 seconds before working inside any machine.
- Wear an anti-static strap connected to an earthed point; hold boards and cards by their edges.
- **Never open a power supply unit or a CRT monitor** — both retain a lethal charge after being unplugged.
- Never puncture, compress or charge a swollen lithium battery; isolate it and follow hazardous disposal procedure.

## Step-by-step

1. Build a comparison table with rows for TN, IPS, VA and OLED and columns for backlight required, colour accuracy, viewing angle, response time, contrast ratio and typical use.
2. Shine a torch at a dark area of a powered-off LCD panel and then an OLED panel, and record which one reflects a visible backlight layer.
3. Display a full-black image on both an LCD and an OLED screen in a dark room and record the difference in black level, then explain it from the backlight architecture.
4. For the symptom 'image is visible only under a bright torch', identify the failed component and justify it — the panel is working, so the backlight or inverter has failed.
5. For the symptom 'image is perfect but touch does not respond anywhere', identify the failed component as the digitizer and note that on bonded assemblies it is replaced with the panel.
6. For the symptom 'flickering that worsens as the machine warms up on an older CCFL laptop', identify the inverter as the probable cause.
7. Work through the remaining symptoms — dead pixels, burn-in, wrong colours, no image with a lit backlight, and intermittent image when the lid moves — and assign a component to each.
8. For the 'intermittent image when the lid moves' symptom, note the display cable running through the hinge as the classic cause and add a physical inspection step.
9. Complete the decision table with a column for the confirming test you would run before ordering a replacement part.
10. Write a customer-facing explanation of one fault in plain language with no jargon, suitable for reading aloud to a non-technical user.

## Test it — verification

Your decision table covers all eight symptoms with a named component and a confirming test for each, and correctly separates the backlight, inverter, panel and digitizer as four distinct failure points.

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
