# Lab 9 — SOHO Network Configuration — DHCP, DNS, NAT and Port Forwarding

> **Course:** CompTIA Certified A+ Training (Core 1 and Core 2) (TGS-2024048317)  
> **Topic 02:** Networking — Core 1, 23% of Core 1  
> **Exam objective:** Configure a SOHO router including DHCP scope, DNS, NAT, DHCP reservations and port forwarding, and verify each service from a client (Core 1 objective 2.5).

## Goal

You configure the full service set a SOHO router provides, then verify each one from a client using the command line. Where physical hardware is unavailable you use the Killercoda playground to inspect and reason about the same configuration from the client side.

## What you'll produce

A documented SOHO configuration with DHCP scope, reservation, DNS and port-forwarding rule, each verified from a client.

## Tools and equipment

SOHO router or router emulator, Killercoda Ubuntu Playground, IP Calculator, ipconfig/ip, nslookup/dig

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

1. Plan the addressing before touching the router: choose 192.168.50.0/24, reserve .1 for the gateway, .2 to .99 for static assignments and .100 to .250 for the DHCP scope.
2. Verify the plan in IP Calculator by entering 192.168.50.0/24 and confirming the usable host range covers every allocation you made.
3. Configure the DHCP scope on the router with the start and end addresses from your plan, and set the lease time.
4. Define the exclusion range covering .2 to .99 so the DHCP server never hands out an address reserved for static assignment.
5. Create a DHCP reservation binding a printer's MAC address to a fixed address such as 192.168.50.20, so it always receives the same IP.
6. Set the DNS servers the router hands to clients, and record whether you used the ISP resolver or a public one such as 8.8.8.8 or 1.1.1.1.
7. On a client, release and renew the DHCP lease and record the address, mask, gateway and DNS servers received.

   ```bash
   ipconfig /release && ipconfig /renew && ipconfig /all
   ```

8. On the Killercoda playground, inspect the equivalent client-side configuration and identify the interface address, mask and default route.

   ```bash
   ip addr show && ip route show && cat /etc/resolv.conf
   ```

9. Verify DNS resolution works through the configured resolver and record the answer section of the response.

   ```bash
   dig +noall +answer www.tertiarycourses.com.sg
   ```

10. Explain how NAT lets many private hosts share one public address, and identify from the router status page what your public address is.
11. Create a port-forwarding rule directing external TCP 3389 to an internal host, and state the security risk of exposing RDP directly to the internet.
12. Document the complete configuration in a table a colleague could use to rebuild the router from scratch after a factory reset.

## Test it — verification

The client receives an address inside the DHCP scope and outside the exclusion range, the reservation returns the same address after a release and renew, DNS resolves successfully through the configured resolver, and the port-forwarding rule is documented with its security risk stated.

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
