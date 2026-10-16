# UDP Message Format (Agent to Server)

Status: PROPOSAL. Pair 1, please review and tell me what to change.

Each agent sends one UDP packet every 2 seconds to the server (port 9999 for now).
The packet body is a JSON text encoded as UTF-8.

## Fields

| Field | Type | Meaning |
|---|---|---|
| device_id | string | Unique name of the laptop |
| timestamp | string | Time the report was made (ISO 8601) |
| bytes_sent | integer | Bytes sent since the last report |
| bytes_recv | integer | Bytes received since the last report |
| packets_sent | integer | Packets sent since the last report |
| packets_recv | integer | Packets received since the last report |
| connections | integer | Number of open network connections |
| active_site | string or null | "YouTube" or "Netflix" if open in the focused window, otherwise null |

## Example

```json
{
  "device_id": "laptop-fatima",
  "timestamp": "2026-10-16T10:30:00",
  "bytes_sent": 1234,
  "bytes_recv": 5678,
  "packets_sent": 12,
  "packets_recv": 30,
  "connections": 18,
  "active_site": null
}
```