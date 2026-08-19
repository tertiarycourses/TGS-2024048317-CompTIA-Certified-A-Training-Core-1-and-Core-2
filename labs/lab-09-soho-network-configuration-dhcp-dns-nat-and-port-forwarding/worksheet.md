# Lab 9 Worksheet — SOHO Network Configuration — DHCP, DNS, NAT and Port Forwarding

**Name:** ______________________    **Date:** ______________

**Exam objective:** Configure a SOHO router including DHCP scope, DNS, NAT, DHCP reservations and port forwarding, and verify each service from a client (Core 1 objective 2.5).

## Record as you go

| Step | What you did | What you observed |
| --- | --- | --- |
| 1 | Plan the addressing before touching the router: choose 192.168.50.0/24, reserve .1 for the gateway, .2 to .99 for static assignments and .100 to .250 for the DHCP scope. |  |
| 2 | Verify the plan in IP Calculator by entering 192.168.50.0/24 and confirming the usable host range covers every allocation you made. |  |
| 3 | Configure the DHCP scope on the router with the start and end addresses from your plan, and set the lease time. |  |
| 4 | Define the exclusion range covering .2 to .99 so the DHCP server never hands out an address reserved for static assignment. |  |
| 5 | Create a DHCP reservation binding a printer's MAC address to a fixed address such as 192.168.50.20, so it always receives the same IP. |  |
| 6 | Set the DNS servers the router hands to clients, and record whether you used the ISP resolver or a public one such as 8.8.8.8 or 1.1.1.1. |  |
| 7 | On a client, release and renew the DHCP lease and record the address, mask, gateway and DNS servers received. |  |
| 8 | On the Killercoda playground, inspect the equivalent client-side configuration and identify the interface address, mask and default route. |  |
| 9 | Verify DNS resolution works through the configured resolver and record the answer section of the response. |  |
| 10 | Explain how NAT lets many private hosts share one public address, and identify from the router status page what your public address is. |  |
| 11 | Create a port-forwarding rule directing external TCP 3389 to an internal host, and state the security risk of exposing RDP directly to the internet. |  |
| 12 | Document the complete configuration in a table a colleague could use to rebuild the router from scratch after a factory reset. |  |

## Verification

**Success criterion:** The client receives an address inside the DHCP scope and outside the exclusion range, the reservation returns the same address after a release and renew, DNS resolves successfully through the configured resolver, and the port-forwarding rule is documented with its security risk stated.

- [ ] I completed every step in the lab.
- [ ] My result meets the success criterion above.
- [ ] I recorded my evidence (screenshots, output, completed tables).

## Reflection

**What surprised you in this lab?**

_______________________________________________________________

**Where would you apply this on the job?**

_______________________________________________________________

**What do you still need to revise before the exam?**

_______________________________________________________________
