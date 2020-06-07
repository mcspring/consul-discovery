"""
Service registry with python-consul
"""

from __future__ import absolute_import

import time
from consul import Consul
from consul.base import Check
from consul.base import Timeout
from ipv4 import get_ipv4


class Registry(object):
    def __init__(
        self,
        host='127.0.0.1',
        port=8500,
        consistency='stale'):
        self.host = host
        self.port = port
        self.consistency = consistency
        self.client = Consul(
            host=self.host,
            port=self.port,
            consistency=self.consistency)

    def register(self,
        service_name,
        service_port,
        service_addr=None,
        service_tags=None,
        service_meta=None,
        service_checks=None):
        assert service_name, \
            'service name cannot be empty'
        assert service_port, \
            'service port is required'

        if service_addr is None:
            service_addr = get_ipv4()

        if service_checks is None:
            service_checks = Check.tcp(service_addr, service_port, '3s', timeout='1s')

        service_id = '%s~%s' % (service_name, service_addr)

        # asynchronously poll for register
        while True:
            try:
                ok = self.client.agent.service.register(service_name,
                    service_id=service_id,
                    address=service_addr,
                    port=service_port,
                    tags=service_tags,
                    meta=service_meta,
                    check=service_checks,
                    enable_tag_override=True)
                if ok:
                    self.service_id = service_id

                    return ok

                time.sleep(10)

            except Timeout:
                # gracefully handle request timeout
                pass


if __name__ == '__main__':
    registry = Registry()
    registry.register('my-app', 8500)
