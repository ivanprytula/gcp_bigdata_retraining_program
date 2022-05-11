class GCPBase(object):
    base_type: str = 'cloud'


class ComputePower(GCPBase):
    pass


class Storage(GCPBase):
    pass


class Networking(GCPBase):
    pass


class Security(ComputePower, Storage, Networking):
    pass
