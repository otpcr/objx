# This file is placed in the Public Domain.


"show uptime/version"


import time


from objx.package import STARTTIME
from objx.utility import elapsed


def upt(event):
    event.reply(elapsed(time.time()-STARTTIME))


def __dir__():
    return (
        'upt',
    )
