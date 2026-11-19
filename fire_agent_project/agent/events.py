"""메인 Agent와 독립된 실행 이벤트 발행/수집 계층."""
from datetime import datetime, timezone
from typing import Callable

_subscribers: list[Callable[[dict], None]] = []


def subscribe(callback: Callable[[dict], None]):
    if callback not in _subscribers:
        _subscribers.append(callback)


def unsubscribe(callback: Callable[[dict], None]):
    if callback in _subscribers:
        _subscribers.remove(callback)


def publish(session_id: str, event_type: str, **payload):
    event = {
        "session_id": session_id,
        "event_type": event_type,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "payload": payload,
    }
    # 구독자 오류가 메인 Agent 실행을 중단시키지 않도록 분리
    for callback in tuple(_subscribers):
        try:
            callback(event)
        except Exception:
            pass
    return event
