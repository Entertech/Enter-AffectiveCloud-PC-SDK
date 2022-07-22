from protocols.responses.base import Response


class BaseServiceResponse(object):

    class Init(Response):

        def __init__(self, **kwargs) -> None:
            super(BaseServiceResponse.Init, self).__init__(**kwargs)
            self.base_services = self.data.get('bio_data_type')

    class Subscribe(Response):

        class ResponseType(object):
            Status = 0
            Data = 1

        def __init__(self, **kwargs) -> None:
            super(BaseServiceResponse.Subscribe, self).__init__(**kwargs)
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
            super(BaseServiceResponse.Unsubscribe, self).__init__(**kwargs)
            self.unsubscribes = {}
            for key, values in self.data.items():
                self.unsubscribes['_'.join(key.split('_')[1:-1])] = values

    class Report(Response):

        def __init__(self, **kwargs) -> None:
            super(BaseServiceResponse.Report, self).__init__(**kwargs)
            self.reports = self.data

    class SubmitAdditionalInformationToStore(Response):

        def __init__(self, **kwargs) -> None:
            super(BaseServiceResponse.SubmitAdditionalInformationToStore, self).__init__(**kwargs)
            self.commits = self.data
