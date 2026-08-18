# Lab 48 — Mobile OS and Application Troubleshooting

> **Course:** CompTIA Certified A+ Training (Core 1 and Core 2) (TGS-2024048317)  
> **Topic 08:** Software Troubleshooting — Core 2, 23% of Core 2  
> **Exam objective:** Diagnose and resolve mobile operating system and application faults including crashes, connectivity, battery and performance problems (Core 2 objectives 3.4 and 3.5).

## Goal

Mobile faults have a fixed escalation order that resolves the large majority without data loss. You work that order on a real device, then handle the security-related symptoms that indicate something worse than a misbehaving app.

## What you'll produce

A mobile troubleshooting escalation sequence and a security symptom map with the response for each.

## Tools and equipment

Android or iOS device, application settings, device settings, mobile OS documentation

## Safety

- Disconnect mains power and hold the power button for 15 seconds before working inside any machine.
- Wear an anti-static strap connected to an earthed point; hold boards and cards by their edges.
- **Never open a power supply unit or a CRT monitor** — both retain a lethal charge after being unplugged.
- Never puncture, compress or charge a swollen lithium battery; isolate it and follow hazardous disposal procedure.

## Step-by-step

1. Build the application escalation sequence in order: force close, clear the cache, clear the application data, uninstall and reinstall, then check for OS and application updates.
2. Record the critical distinction: clearing the cache is non-destructive, while clearing application data resets the app and removes local content including saved logins.
3. Practise the sequence on a real application, recording the exact settings path for force close, clear cache and clear data on your device.
4. Diagnose an application that fails to launch by working the sequence, and record which step resolved it.
5. Diagnose an application that fails to update by checking available storage, checking the network connection, and clearing the store application's own cache.
6. Diagnose battery drain by separating the causes: background applications, a weak signal forcing the radio to maximum transmit power, high screen brightness, or a genuinely degraded battery.
7. Use the device's battery usage screen to identify the top three consuming applications, and record the figures.
8. Diagnose overheating by separating sustained high load, a charging fault, an ambient heat source and a failing battery, and record that a swollen battery is an immediate safety stop.
9. Diagnose connectivity faults with a fixed sequence per technology: toggle airplane mode, forget and rejoin the Wi-Fi network, unpair and re-pair the Bluetooth device, then reset network settings.
10. Record what resetting network settings actually does — it clears all saved Wi-Fi networks, Bluetooth pairings and VPN configurations — so the user must be warned before you do it.
11. Build the security symptom map: high network traffic, sluggish response, data cap notifications, unexpected ads, fake security warnings and unfamiliar applications.
12. Record the causes behind those symptoms — sideloaded APKs from outside the official store, a rooted or jailbroken device, application spoofing, or developer mode left enabled — and the response for each.

## Test it — verification

Your sequence orders the five application steps from least to most destructive; the cache-versus-data distinction is stated with its consequence; the battery record names the top three consumers with figures; and every security symptom has a named cause and response.

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
