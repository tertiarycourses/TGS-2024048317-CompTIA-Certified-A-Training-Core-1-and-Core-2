# Lab 21 — Cloud Service and Deployment Model Selection

> **Course:** CompTIA Certified A+ Training (Core 1 and Core 2) (TGS-2024048317)  
> **Topic 04:** Virtualization and Cloud Computing — Core 1, 11% of Core 1  
> **Exam objective:** Compare IaaS, PaaS and SaaS and the public, private, community and hybrid deployment models, and select the correct combination for a stated business requirement (Core 1 objective 4.1).

## Goal

You build the responsibility matrix that separates the three service models, compare the four deployment models on the concerns that decide them, and then solve selection scenarios where the wrong choice creates either a compliance breach or an unnecessary cost.

## What you'll produce

A shared-responsibility matrix, a deployment model comparison and six justified service and deployment selections.

## Tools and equipment

Cloud provider documentation, IaaS/PaaS/SaaS reference material, organisational scenario briefs

## Safety

- Disconnect mains power and hold the power button for 15 seconds before working inside any machine.
- Wear an anti-static strap connected to an earthed point; hold boards and cards by their edges.
- **Never open a power supply unit or a CRT monitor** — both retain a lethal charge after being unplugged.
- Never puncture, compress or charge a swollen lithium battery; isolate it and follow hazardous disposal procedure.

## Step-by-step

1. Build the shared-responsibility matrix with rows for networking, storage, servers, virtualization, operating system, middleware, runtime, data and applications.
2. Mark for on-premises that the customer manages every layer, which is the baseline the three cloud models are measured against.
3. Mark for IaaS that the provider manages up to virtualization and the customer manages the operating system and everything above it — examples are AWS EC2, Azure Virtual Machines and Google Compute Engine.
4. Mark for PaaS that the provider manages up to the runtime and the customer manages only applications and data — examples are Azure App Service, Google App Engine and Heroku.
5. Mark for SaaS that the provider manages every layer and the customer manages only their own data and users — examples are Microsoft 365, Google Workspace and Salesforce.
6. Compare the four deployment models on cost, control, security, compliance and typical use: public, private, community and hybrid.
7. Record the five cloud characteristics that define the model: shared resources, rapid elasticity, high availability, file synchronisation and metered utilisation.
8. Explain metered utilisation and why it changes budgeting — you pay for what you consume, so an idle over-provisioned resource is pure waste.
9. Solve the scenario of a hospital storing patient records under strict data residency rules, and justify why private cloud is correct and public is not.
10. Solve the scenario of a startup needing email and document collaboration with no IT staff, and justify why SaaS on public cloud is correct.
11. Solve the scenario of a retailer with steady baseline load and extreme seasonal peaks, and justify why hybrid cloud with cloud bursting is correct.
12. Solve the remaining scenarios — several hospitals sharing a compliance platform, a development team needing full OS control, and a team deploying code without managing servers — and justify each.

## Test it — verification

Your responsibility matrix correctly divides all nine layers across on-premises, IaaS, PaaS and SaaS; every scenario names both a service model and a deployment model; and each justification cites the specific requirement that ruled the alternatives out.

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
