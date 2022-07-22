import json
from typing import List


class AffectiveServiceRequest(object):

    class _request(object):

        services = "affective"

    class Start(_request):

        def __init__(self, services: List[str]) -> None:
            self.ac_services = services

        def __str__(self) -> str:
            return json.dumps({
                "services": self.services,
                "op": "start",
                "kwargs": {
                    "cloud_services": self.ac_services,
                },
            })

    class Subscribe(_request):

        def __init__(self, services: List[str]) -> None:
            self.ac_services = services

        def __str__(self) -> str:
            return json.dumps({
                "services": self.services,
                "op": "subscribe",
                "args": self.ac_services,
            })

    class Unsubscribe(_request):

        def __init__(self, services: List[str]) -> None:
            self.ac_services = services

        def __str__(self) -> str:
            return json.dumps({
                "services": self.services,
                "op": "unsubscribe",
                "args": self.ac_services,
            })

    class Report(_request):

        def __init__(self, services: List[str], ignore_report_body: bool = False) -> None:
            self.ac_services = services
            self.ignore_report_body = ignore_report_body

        def __str__(self) -> str:
            return json.dumps({
                "services": self.services,
                "op": "report",
                "kwargs": {
                    "cloud_services": self.ac_services,
                    "ignore_report_body": self.ignore_report_body,
                },
            })

    class Finish(_request):

        def __init__(self, services: List[str]) -> None:
            self.ac_services = services

        def __str__(self) -> str:
            return json.dumps({
                "services": self.services,
                "op": "finish",
                "kwargs": {
                    "cloud_services": self.ac_services,
                },
            })
