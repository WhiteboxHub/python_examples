#!/usr/bin/env python3

# spinner_curio.py

# credits: Example by Luciano Ramalho inspired by


import curio

import itertools
import sys


async def spin(msg):  # <1>
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in itertools.cycle('|/-\\'):
        status = char + ' ' + msg
        write(status)
        flush()
        write('\x08' * len(status))
        try:
            await curio.sleep(.1)  # <2>
        except curio.CancelledError:  # <3>
            break
    write(' ' * len(status) + '\x08' * len(status))


async def slow_function():  # <4>
    # pretend waiting a long time for I/O
    await curio.sleep(3)  # <5>
    return 42


async def supervisor():  # <6>
    spinner = await curio.spawn(spin('thinking!'))  # <7>
    print('spinner object:\n ', repr(spinner))  # <8>
    result = await slow_function()  # <9>
    await spinner.cancel()  # <10>
    return result


def main():
    result = curio.run(supervisor)  # <12>
    print('Answer:', result)


if __name__ == '__main__':
    main()