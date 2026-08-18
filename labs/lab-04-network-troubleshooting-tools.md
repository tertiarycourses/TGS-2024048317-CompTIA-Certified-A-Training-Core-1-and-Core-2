# Lab 04 - Network Troubleshooting Tools

## Objectives

- Use common network commands.
- Interpret IP configuration.
- Test DNS and route paths.
- Write a network troubleshooting note.

## Steps

1. Open Command Prompt or PowerShell.
2. Run `ipconfig /all`.
3. Identify IP address, subnet mask, gateway, DNS, DHCP, and MAC address.
4. Run `ping 127.0.0.1`.
5. Run `ping <default-gateway>`.
6. Ping a public IP address if permitted.
7. Run `nslookup <domain>`.
8. Run `tracert <domain>`.
9. Run `netstat -ano`.
10. Identify symptoms such as APIPA, DNS failure, gateway unreachable, and intermittent connectivity.
11. Create a decision table mapping symptoms to next checks.
12. Write a ticket note summarizing findings.

## Validation

- Command outputs are interpreted correctly.
- DNS and gateway checks are separated.
- Decision table is practical.
- Ticket note is clear.

## Review Questions

1. What does an APIPA address indicate?
2. Why test loopback before gateway?
3. What does `nslookup` verify?
4. How does `tracert` help troubleshooting?
