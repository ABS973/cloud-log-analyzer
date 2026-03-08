# log_analyzer.py
# Cloud Log Processing Pipeline - Step 3: Analyze Clean Logs
#
# Each log line format:
#   timestamp | level | service | message


def filter_by_level(lines, wanted_level):
    """
    Return only the log lines that match the requested level.

    Args:
        lines        -- list of clean log line strings
        wanted_level -- e.g. "ERROR", "WARN", "INFO"

    Returns:
        List of matching log lines.
    """
    result = []
    for line in lines:
        parts = line.split("|")
        level = parts[1].strip()
        if level == wanted_level:
            result.append(line)
    return result


def count_levels(lines):
    """
    Count how many log entries exist for each level.

    Args:
        lines -- list of clean log line strings

    Returns:
        Dictionary e.g. {"INFO": 3, "WARN": 2, "ERROR": 5}
    """
    counts = {}
    for line in lines:
        parts = line.split("|")
        level = parts[1].strip()
        counts[level] = counts.get(level, 0) + 1
    return counts


def count_services(lines):
    """
    Count how many log entries come from each service.

    Args:
        lines -- list of clean log line strings

    Returns:
        Dictionary e.g. {"api": 5, "db": 2, "auth": 3}
    """
    counts = {}
    for line in lines:
        parts = line.split("|")
        service = parts[2].strip()
        counts[service] = counts.get(service, 0) + 1
    return counts
