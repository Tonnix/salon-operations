# Architecture and contracts
Browser HTML/CSS/JS -> explicit RPC allowlist -> Auth/Permissions -> domain service -> Posting/Lock -> repository -> Sheets tabs. Separate contact repository/workbook. Domain services never call browser. Sheets rows use permanent IDs and header names, not row positions. Schema changes are versioned, additive where possible, tested on copies. Use integer minor units, Africa/Nairobi timezone, ISO timestamps with offset or UTC plus business date. No duplicate client/order/task ledger.

## Modules (planned; only bootstrap files exist)
| File | Role |
|---|---|
| App.gs | doGet and minimal RPC entry |
| Auth.gs / Permissions.gs | verified principal, role/branch/ownership checks |
| Config.gs / Schema.gs | environment and versioned table registry |
| Repository.gs / ContactRepository.gs | batched reads/writes and restricted contacts |
| Posting.gs / Audit.gs | lock, idempotency, atomic same-workbook batch, recovery journal |
| Catalogue.gs / Inventory.gs / Transfers.gs | approval, SKU, stock events and transfer lifecycle |
| Orders.gs / Payments.gs / Promotions.gs | basket, receipts, allocations, discounts, credits/refunds |
| ServiceRoutes.gs / Resources.gs | versioned stage graph, skills, shifts and station calendars |
| CapacityPlanner.gs / BookingService.gs | candidate insertion, holds, confirmation, recheck |
| VisitService.gs / QueueService.gs | check-in, one ticket, eligibility and priority |
| Dispatch.gs / TaskService.gs | offers, start/complete, readiness, remaining time |
| StaffReview.gs / Complaints.gs | acknowledgement, dispute, redo |
| Reporting.gs / Recovery.gs | reconciliation, flow metrics, exception recovery |
| Index.html / Styles.html / Client.html | responsive UI, safe rendering, RPC wrapper |

Use a single script lock for authoritative commits across both branches initially; re-read current state inside lock, validate, write supported atomic Sheets API batch in same workbook, release in finally. No external calls while holding lock unless essential to commit. Lock does not protect manual edits or another script project: prohibit alternate writers. Cross-workbook/provider operations require pending/committed/recovery states, not fictional atomicity. Retry by submission ID and payload hash; conflicting reuse rejected. Store original promise separately from revised ETA. All scheduling operations use same reservation model. Active work cannot be moved; pooled future allocations provisional, named commitments consent-bound. A timer never certifies readiness. No fixed appointment/walk-in ratio.

RPC contract: {action, requestId, branchId, expectedVersion, payload}; server derives actor; response {ok, data, error:{code,message}, version}. Do not expose raw rows, stack traces or contacts to technicians. State changes return authoritative result, never optimistic success. Use explicit DTO allowlists. No public booking until P7 separate approval.
