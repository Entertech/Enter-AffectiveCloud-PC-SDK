from typing import List, Dict, Any
import json

from algorithm.base_services import BaseServiceType


class BaseServiceRequest(object):

    class _request(object):

        services = "biodata"

    class Init(_request):

        def __init__(self, services: List[str], storage_settings: dict = None, algorithm_params: dict = None) -> None:
            self.base_services = services
            self.storage_settings = storage_settings
            self.algorithm_params = algorithm_params

        def __str__(self) -> str:
            body = {
                "services": self.services,
                "op": "init",
                "kwargs": {
                    "bio_data_type": self.base_services,
                },
            }
            if self.storage_settings:
                body["kwargs"]["storage_settings"] = self.storage_settings
            if self.algorithm_params:
                body["kwargs"]["algorithm_params"] = self.algorithm_params
            return json.dumps(body)

    class Subscribe(_request):

        def __init__(self, services: List[str]) -> None:
            self.base_services = services

        def __str__(self) -> str:
            return json.dumps({
                "services": self.services,
                "op": "subscribe",
                "args": self.base_services,
            })

    class Unsubscribe(_request):

        def __init__(self, services: List[str]) -> None:
            self.base_services = services

        def __str__(self) -> str:
            return json.dumps({
                "services": self.services,
                "op": "unsubscribe",
                "args": self.base_services,
            })

    class Upload(_request):

        def __init__(self, services_data: Dict[BaseServiceType, List[Any]]) -> None:
            self.services_data = services_data

        def __str__(self) -> str:
            return json.dumps({
                "services": self.services,
                "op": "upload",
                "kwargs": self.services_data,
            })

    class Report(_request):

        def __init__(self, services: List[str], ignore_report_body: bool = False) -> None:
            self.base_services = services
            self.ignore_report_body = ignore_report_body

        def __str__(self) -> str:
            return json.dumps({
                "services": self.services,
                "op": "report",
                "kwargs": {
                    "bio_data_type": self.base_services,
                    "ignore_report_body": self.ignore_report_body,
                },
            })

    class SubmitAdditionalInformationToStore(_request):

        def __init__(self, data: Dict[str, Any]) -> None:
            self.data = data

        def __str__(self) -> str:
            return json.dumps({
                "services": self.services,
                "op": "submit",
                "kwargs": {
                    "bio_data_type": self.base_services,
                    "data": self.data,
                },
            })
