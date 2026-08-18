# Lab 9 Worksheet — SOHO Network Configuration — DHCP, DNS, NAT and Port Forwarding

**Name:** ______________________    **Date:** ______________

**Exam objective:** Configure a SOHO router including DHCP scope, DNS, NAT, DHCP reservations and port forwarding, and verify each service from a client (Core 1 objective 2.5).

## Record as you go

| Step | What you did | What you observed |
| --- | --- | --- |
| 1 | Plan the addressing before touching the router: choose 192.168.50.0... |  |
| 2 | Verify the plan in IP Calculator by entering 192.168.50.0/24 and co... |  |
| 3 | Configure the DHCP scope on the router with the start and end addre... |  |
| 4 | Define the exclusion range covering .2 to .99 so the DHCP server ne... |  |
| 5 | Create a DHCP reservation binding a printer's MAC address to a fixe... |  |
| 6 | Set the DNS servers the router hands to clients, and record whether... |  |
| 7 | On a client, release and renew the DHCP lease and record the addres... |  |
| 8 | On the Killercoda playground, inspect the equivalent client-side co... |  |
| 9 | Verify DNS resolution works through the configured resolver and rec... |  |
| 10 | Explain how NAT lets many private hosts share one public address, a... |  |
| 11 | Create a port-forwarding rule directing external TCP 3389 to an int... |  |
| 12 | Document the complete configuration in a table a colleague could us... |  |

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
