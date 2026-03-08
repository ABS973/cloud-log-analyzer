# test_log_analyzer.py
# Test script for log_analyzer.py

from log_analyzer import filter_by_level, count_levels, count_services

# ─────────────────────────────────────────────
# Sample log data (clean, validated entries)
# ─────────────────────────────────────────────
logs = [
    "2026-02-05 08:11:20 | ERROR | db   | DB timeout",
    "2026-02-05 08:11:21 | INFO  | api  | Request received",
    "2026-02-05 08:11:22 | WARN  | disk | Disk almost full",
    "2026-02-05 08:11:23 | ERROR | api  | Failed request",
    "2026-02-05 08:11:24 | INFO  | auth | User login",
    "2026-02-05 08:11:25 | WARN  | api  | Slow response",
    "2026-02-05 08:11:26 | ERROR | auth | Auth service down",
    "2026-02-05 08:11:27 | INFO  | db   | Query completed",
]

# ─────────────────────────────────────────────
# TEST 1: filter_by_level()
# ─────────────────────────────────────────────
print("=" * 55)
print("TEST 1: filter_by_level()")
print("=" * 55)

# Filter ERROR logs
error_logs = filter_by_level(logs, "ERROR")
print(f"\n  filter_by_level(logs, 'ERROR') → {len(error_logs)} result(s)")
for line in error_logs:
    print(f"    {line}")

expected_errors = 3
status = "✅ PASS" if len(error_logs) == expected_errors else "❌ FAIL"
print(f"\n  {status}  Expected {expected_errors} ERROR entries, got {len(error_logs)}")

# Filter WARN logs
warn_logs = filter_by_level(logs, "WARN")
print(f"\n  filter_by_level(logs, 'WARN') → {len(warn_logs)} result(s)")
for line in warn_logs:
    print(f"    {line}")

expected_warns = 2
status = "✅ PASS" if len(warn_logs) == expected_warns else "❌ FAIL"
print(f"\n  {status}  Expected {expected_warns} WARN entries, got {len(warn_logs)}")

# Filter a level that doesn't exist
debug_logs = filter_by_level(logs, "DEBUG")
status = "✅ PASS" if debug_logs == [] else "❌ FAIL"
print(f"\n  {status}  filter_by_level(logs, 'DEBUG') → {debug_logs} (expected [])")

# ─────────────────────────────────────────────
# TEST 2: count_levels()
# ─────────────────────────────────────────────
print()
print("=" * 55)
print("TEST 2: count_levels()")
print("=" * 55)

level_counts = count_levels(logs)
print(f"\n  count_levels(logs) →")
for level, count in sorted(level_counts.items()):
    print(f"    {level:<6} : {count}")

expected_level_counts = {"ERROR": 3, "INFO": 3, "WARN": 2}
status = "✅ PASS" if level_counts == expected_level_counts else "❌ FAIL"
print(f"\n  {status}  Expected: {expected_level_counts}")
print(f"           Got:      {level_counts}")

# ─────────────────────────────────────────────
# TEST 3: count_services()
# ─────────────────────────────────────────────
print()
print("=" * 55)
print("TEST 3: count_services()")
print("=" * 55)

service_counts = count_services(logs)
print(f"\n  count_services(logs) →")
for service, count in sorted(service_counts.items()):
    print(f"    {service:<6} : {count}")

expected_service_counts = {"api": 3, "auth": 2, "db": 2, "disk": 1}
status = "✅ PASS" if service_counts == expected_service_counts else "❌ FAIL"
print(f"\n  {status}  Expected: {expected_service_counts}")
print(f"           Got:      {service_counts}")

# ─────────────────────────────────────────────
# BONUS: Combined analysis summary
# ─────────────────────────────────────────────
print()
print("=" * 55)
print("ANALYSIS SUMMARY")
print("=" * 55)
print(f"\n  Total log entries : {len(logs)}")
print(f"\n  By level:")
for level, count in sorted(level_counts.items()):
    bar = "█" * count
    print(f"    {level:<6} {bar} ({count})")
print(f"\n  By service:")
for service, count in sorted(service_counts.items()):
    bar = "█" * count
    print(f"    {service:<6} {bar} ({count})")
most_errors = filter_by_level(logs, "ERROR")
print(f"\n  ⚠️  {len(most_errors)} ERROR(s) detected — review required")
