from affectivecloud.protocols.responses.base import Response


class AffectiveServiceResponse(object):

    class Start(Response):

        def __init__(self, **kwargs) -> None:
            super(AffectiveServiceResponse.Start, self).__init__(**kwargs)
            self.ac_services = self.data.get('cloud_service')

    class Subscribe(Response):

        class ResponseType(object):
            Status = 0
            Data = 1

        def __init__(self, **kwargs) -> None:
            super(AffectiveServiceResponse.Subscribe, self).__init__(**kwargs)
            self.subscribes = {}
            for key, values in self.data.items():
                keys = key.split('_')
                if (keys[0], keys[-1]) == ('sub', 'fields'):
                    self.response_type = self.ResponseType.Status
                    self.subscribes['_'.join(keys[1:-1])] = values
                else:
                    self.response_type = self.ResponseType.Data

    class Unsubscribe(Response):

        def __init__(self, **kwargs) -> None:
            super(AffectiveServiceResponse.Unsubscribe, self).__init__(**kwargs)
            self.unsubscribes = {}
            for key, values in self.data.items():
                self.unsubscribes['_'.join(key.split('_')[1:-1])] = values

    class Report(Response):

        def __init__(self, **kwargs) -> None:
            super(AffectiveServiceResponse.Report, self).__init__(**kwargs)
            self.reports = self.data

    class Finish(Response):

        def __init__(self, **kwargs) -> None:
            super(AffectiveServiceResponse.Finish, self).__init__(**kwargs)
            self.ac_services = self.data.get('cloud_service')
