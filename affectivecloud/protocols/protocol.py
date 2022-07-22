import json


ServiceType: type = str

OperationType: type = str


class Services(object):

    class Type(object):
        SESSION: ServiceType = "session"
        BASE_SERVICE: ServiceType = "biodata"
        AFFECTIVE_SERVICE: ServiceType = "affective"

    class Operation:
        class Session:
            CREATE: OperationType = "create"
            RESTORE: OperationType = "restore"
            CLOSE: OperationType = "close"

        class BaseService:
            INIT: OperationType = "init"
            SUBSCRIBE: OperationType = "subscribe"
            UNSUBSCRIBE: OperationType = "unsubscribe"
            UPLOAD: OperationType = "upload"
            REPORT: OperationType = "report"
            SUBMIT: OperationType = "submit"

        class AffectiveService:
            START: OperationType = "start"
            SUBSCRIBE: OperationType = "subscribe"
            UNSUBSCRIBE: OperationType = "unsubscribe"
            REPORT: OperationType = "report"
            FINISH: OperationType = "finish"

    class DataUploadCycleLength:
        EEG: int = 1000
        HR: int = 3


class ProtocolBase(object):
    def dumps(self):
        return json.dumps(self.dict())

    def dict(self):
        return self.__dict__

    def __str__(self):
        return self.dumps()


class ProtocolDictBody(ProtocolBase):
    def __init__(self, **kwargs):
        super(ProtocolDictBody, self).__init__()
        for k, v in kwargs.items():
            setattr(self, k, v)

    def dumps(self):
        return json.dumps(self.dict())

    def dict(self):
        return self.__dict__

    def __str__(self):
        return self.dumps()
