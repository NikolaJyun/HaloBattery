"""Traditional Chinese text helpers for HaloBattery's user interface."""
from __future__ import annotations

import re


_EXACT_STATUS = {
    "connected, battery level not reported": "已連線，未回報電量",
    "connected, battery level not reported yet": "已連線，尚未回報電量",
    "on cable, charging": "已接上纜線，充電中",
    "empty": "電量耗盡",
    "low": "低電量",
    "medium": "中等電量",
    "full": "電量充足",
}


def status(text: str) -> str:
    """Translate the short, user-visible status snippets returned by providers."""
    if not text:
        return text
    if text in _EXACT_STATUS:
        return _EXACT_STATUS[text]
    m = re.fullmatch(r"about (\d+)% \((empty|low|medium|full)\)", text)
    if m:
        return f"約 {m.group(1)}%（{_EXACT_STATUS[m.group(2)]}）"
    m = re.fullmatch(r"about (\d+)%(, charging)?", text)
    if m:
        return f"約 {m.group(1)}%" + ("，充電中" if m.group(2) else "")
    return text.replace(", charging", "，充電中").replace("charging", "充電中")
