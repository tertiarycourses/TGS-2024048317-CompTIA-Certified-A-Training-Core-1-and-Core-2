# Lab 4 — MDM Policy Design and Mobile Synchronisation

> **Course:** CompTIA Certified A+ Training (Core 1 and Core 2) (TGS-2024048317)  
> **Topic 01:** Mobile Devices — Core 1, 13% of Core 1  
> **Exam objective:** Design a mobile device management policy and configure account synchronisation for corporate email, calendar and contacts, accounting for data caps (Core 1 objective 1.4).

## Goal

You design an MDM policy for a small organisation issuing corporate devices, then configure and verify account synchronisation on a real device. You finish by calculating the data cost of a full photo sync so you can advise a user before they exceed their cap.

## What you'll produce

A written MDM policy covering eight control areas, plus a verified synchronisation configuration and a data-cap impact calculation.

## Tools and equipment

Mobile device, a Microsoft 365 or Google Workspace account, IP Calculator, organisational policy template

### Browser tools used in this lab

- **IP Calculator** — <https://alfredang.github.io/ipcalculator/>

![IP Calculator interface map](../../courseware/assets/tool-ipcalculator.png)

*IP Calculator — the panels and fields this lab uses.*

## Safety

- Disconnect mains power and hold the power button for 15 seconds before working inside any machine.
- Wear an anti-static strap connected to an earthed point; hold boards and cards by their edges.
- **Never open a power supply unit or a CRT monitor** — both retain a lethal charge after being unplugged.
- Never puncture, compress or charge a swollen lithium battery; isolate it and follow hazardous disposal procedure.

## Step-by-step

1. List the eight MDM control areas your policy must cover: device enrolment, screen lock, encryption, corporate email profile, two-factor authentication, application whitelisting, remote wipe and location services.
2. For each control area, write the specific rule your policy enforces and one sentence on the risk it mitigates.
3. Distinguish MDM from MAM in your policy: MDM controls the whole device, while MAM controls only the corporate applications and data on it.
4. Write the BYOD section covering what the organisation may and may not wipe on a personally owned device, and why a full remote wipe is inappropriate there.
5. On the device, add a Microsoft 365 or Google Workspace account and select which data types to synchronise: mail, calendar, contacts and photos.
6. Verify synchronisation by creating a calendar entry on the device and confirming it appears in the web client within one minute.
7. Open the device's data usage screen and record the current billing-period total and the configured data cap or warning threshold.
8. Estimate the size of a full photo library sync, then calculate what percentage of a 5 GB monthly cap it would consume and state whether it should run on cellular.
9. Configure the account to synchronise photos on Wi-Fi only, and record the exact setting path so it can be included in a user guide.
10. Write the user-facing section of the guide: how to enrol, what the organisation can see, and what to do if the device is lost or stolen.

## Test it — verification

Your policy covers all eight control areas with a rule and a risk for each, clearly separates MDM from MAM and corporate from BYOD, synchronisation is verified end to end within one minute, and the data-cap calculation supports a stated Wi-Fi-only recommendation.

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
