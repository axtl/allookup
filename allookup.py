#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import socket
import sys

from socket import gethostbyaddr, gethostbyname_ex


DESCRIPTION = "Find all related IPs and hostnames for the given host"


class memoize(object):
    """Decorator that caches a function's return value each time it is called.
    If called later with the same arguments, the cached value is returned, and
    not re-evaluated.
    """
    # http://wiki.python.org/moin/PythonDecoratorLibrary#Memoize
    def __init__(self, func):
        self.func = func
        self.cache = {}

    def __call__(self, *args):
        try:
            return self.cache[args]
        except KeyError:
            value = self.func(*args)
            self.cache[args] = value
            return value
        except TypeError:
            # uncachable -- for instance, passing a list as an argument.
            # Better to not cache than to blow up entirely.
            return self.func(*args)

    def __repr__(self):
        """Return the function's docstring."""
        return self.func.__doc__

    def __get__(self, obj, objtype):
        """Support instance methods."""
        return functools.partial(self.__call__, obj)


def _is_ip_addr(addr):
    """Attempt to identify if @addr is a valid IP4/6 address."""
    try:
        socket.inet_pton(socket.AF_INET6, addr)
        return True
    except:
        try:
            socket.inet_pton(socket.AF_INET, addr)
            return True
        except:
            return False


@memoize
def _related_names(addr):
    # Not meant to be resolvable
    if addr.endswith('.arpa'):
        return set()
    else:
        fun = gethostbyaddr if _is_ip_addr(addr) else gethostbyname_ex
        (cname, aliases, ips) = fun(addr)
        aliases.append(cname)
        aliases.extend(ips)
        return set(aliases)


def _server_names(addr):
    names = set([addr])
    # track if new entries need to be looked at for related names
    new_entries = True

    while new_entries:
        aliases = set()
        for ent in names:
            aliases.update(_related_names(ent))
        old_size = len(names)
        names.update(aliases)
        new_size = len(names)
        new_entries = old_size != new_size

    return names


def main(argv):
    # setup and parse arguments
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument('-a', '--address',
        action='append',
        help='The hostname/IP address to search.')

    # create namespace with args
    if len(argv) == 0:
        parser.print_help()
        sys.exit(0)

    ns = parser.parse_args(args=argv)

    for addr in ns.address:
        names = _server_names(addr)
        sys.stdout.write('%s is known as:\n\n' % addr)
        for name in names:
            sys.stdout.write('\t%s\n' % name)
        sys.stdout.write('\n\n')


if __name__ == '__main__':
    main(sys.argv[1:])
