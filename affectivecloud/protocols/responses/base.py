

class RequestHead(object):

    services: str = None

    op: str = None

    def __init__(self, **kwargs):
        super(RequestHead, self).__init__()
        for k, v in kwargs.items():
            if k not in ('services', 'op'):
                raise Exception('Protocol Error: invalid parameters({}).'.format(k))
            setattr(self, k, v)

    def __str__(self):
        return '[{}:{}]'.format(self.services, self.op)


class Response(object):

    code: int = None

    request: RequestHead = None

    data = None

    msg: str = None

    def __init__(self, **kwargs):
        super(Response, self).__init__()
        for k, v in kwargs.items():
            if k == 'request':
                setattr(self, k, RequestHead(**v))
                continue
            if k not in ('code', 'request', 'data', 'msg'):
                raise Exception('Protocol Error: invalid parameters({}).'.format(k))
            setattr(self, k, v)

    def __str__(self):
        return '[code: {}] [msg: {}] {} >>> {}'.format(self.code, self.msg, self.request, self.data)
