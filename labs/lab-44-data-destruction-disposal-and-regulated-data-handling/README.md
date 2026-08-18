# Lab 44 — Data Destruction, Disposal and Regulated Data Handling

> **Course:** CompTIA Certified A+ Training (Core 1 and Core 2) (TGS-2024048317)  
> **Topic 07:** Security — Core 2, 28% of Core 2  
> **Exam objective:** Select the correct data destruction method for a stated sensitivity and retention requirement, and handle regulated data according to its legal obligations (Core 2 objectives 2.8 and 4.6).

## Goal

Data destruction is where a wrong choice creates legal liability rather than an inconvenience. You match destruction methods to data sensitivity, then work the regulated data categories and the chain-of-custody discipline that evidence handling requires.

## What you'll produce

A destruction method decision table, a regulated data handling reference and a completed chain-of-custody form.

## Tools and equipment

Data destruction reference, regulatory documentation, chain-of-custody template

## Safety

- Disconnect mains power and hold the power button for 15 seconds before working inside any machine.
- Wear an anti-static strap connected to an earthed point; hold boards and cards by their edges.
- **Never open a power supply unit or a CRT monitor** — both retain a lethal charge after being unplugged.
- Never puncture, compress or charge a swollen lithium battery; isolate it and follow hazardous disposal procedure.

## Step-by-step

1. Separate the two destruction goals: physical destruction where the media will never be reused, and sanitisation where the media is to be reused or resold.
2. Record the physical destruction methods: drilling through the platters, shredding into small fragments, degaussing with a strong magnetic field, and incineration.
3. Record the critical exception: degaussing does not work on solid state drives, because SSDs store data in flash cells rather than magnetically. Shredding or cryptographic erase is required instead.
4. Record the sanitisation methods for reuse: a standard format which only clears the file table, a low-level format, and a multi-pass overwrite wipe which is the only reliable software method on a hard disk.
5. Record why a standard format is not destruction: it removes the index but leaves the data recoverable with freely available tools.
6. Record cryptographic erase for self-encrypting drives: destroying the encryption key renders all data unrecoverable instantly, which is the fastest correct method for an SED or an encrypted SSD.
7. Build the decision table matching data sensitivity to method: public data may simply be deleted, internal data must be wiped, confidential data must be wiped and verified, and regulated data must be physically destroyed with a certificate.
8. Record the outsourcing requirements: use a certified vendor, obtain a certificate of destruction listing serial numbers, and retain that certificate for the audit period.
9. Build the regulated data reference: personally identifiable information, PCI DSS for payment card data, GDPR for EU personal data, PHI under HIPAA for health data, and Singapore's PDPA.
10. For each regulation record what data it covers, the core obligation it imposes and the consequence of a breach.
11. Record the chain of custody: the chronological documentation of who held evidence, when, and what they did with it, and note that a gap in the chain can render evidence inadmissible.
12. Complete a chain-of-custody form for a hypothetical drive removed from a compromised machine, recording every handover with date, time, person and purpose.

## Test it — verification

Your decision table gives a method for all four sensitivity levels; you correctly state that degaussing does not work on SSDs; the regulated data reference covers at least five frameworks with obligations; and the chain-of-custody form has no gaps between handovers.

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
