import hashlib
import time
import json
from typing import Tuple


class SessionRequest(object):

    @classmethod
    def _sign(cls, app_key: str, secret: str, client_id: str) -> Tuple[str, str]:
        _timestamp = str(int(time.time()))
        params = 'app_key={}&app_secret={}&timestamp={}&user_id={}'.format(
            app_key, secret, _timestamp, client_id or client_id
        )
        _md5 = hashlib.md5()
        _md5.update(params.encode())
        return _timestamp, _md5.hexdigest().upper()

    class _request(object):

        services = "session"

    class Create(_request):

        def __init__(self, app_key: str, secret: str, client_id: str, upload_cycle: int = 3) -> None:
            self.app_key = app_key
            self.secret = secret
            self.client_id = client_id
            self.upload_cycle = upload_cycle

        def __str__(self) -> str:
            timestamp, sign = SessionRequest._sign(
                self.app_key, self.secret, self.client_id
            )
            return json.dumps({
                "services": self.services,
                "op": "create",
                "kwargs": {
                    "app_key": self.app_key,
                    "sign": sign,
                    "user_id": self.client_id,
                    "timestamp": timestamp,
                    "upload_cycle": self.upload_cycle,
                },
            })

    class Restore(_request):

        def __init__(self, app_key: str, secret: str, client_id: str, session_id: str, upload_cycle: int = 3) -> None:
            self.app_key = app_key
            self.secret = secret
            self.client_id = client_id
            self.session_id = session_id
            self.upload_cycle = upload_cycle

        def __str__(self) -> str:
            timestamp, sign = SessionRequest._sign(
                self.app_key, self.secret, self.client_id
            )
            return json.dumps({
                "services": self.services,
                "op": "restore",
                "kwargs": {
                    "app_key": self.app_key,
                    "sign": sign,
                    "user_id": self.client_id,
                    "timestamp": timestamp,
                    "session_id": self.session_id,
                    "upload_cycle": self.upload_cycle,
                },
            })

    class Close(_request):

        def __str__(self) -> str:
            return json.dumps({"services": "session", "op": "close"})
