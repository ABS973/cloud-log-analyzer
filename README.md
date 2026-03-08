# Cloud Log Analyzer — Step 3: Analyze Clean Logs

Analyzes validated log entries to help operations teams understand system behavior.

## Files

| File | Purpose |
|------|---------|
| `log_analyzer.py` | Core functions: `filter_by_level()`, `count_levels()`, `count_services()` |
| `test_log_analyzer.py` | Test script with unit tests + analysis summary |

## Run

```bash
python test_log_analyzer.py
```

## Log Line Format

```
timestamp | level | service | message
```

Example:
```
2026-02-05 08:11:20 | ERROR | db | DB timeout
```

## Functions

| Function | What it does |
|----------|-------------|
| `filter_by_level(lines, wanted_level)` | Returns only lines matching the given level |
| `count_levels(lines)` | Returns a dict counting entries per level |
| `count_services(lines)` | Returns a dict counting entries per service |
