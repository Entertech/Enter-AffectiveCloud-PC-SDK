from affectivecloud.protocols.responses.base import Response


class SessionResponse(object):

    class Create(Response):

        def __init__(self, **kwargs) -> None:
            super(SessionResponse.Create, self).__init__(**kwargs)
            self.session_id = self.data.get('session_id')

    class Restore(Response):

        def __init__(self, **kwargs) -> None:
            super(SessionResponse.Restore, self).__init__(**kwargs)
            self.session_id = self.data.get('session_id')

    class Close(Response):
        pass
