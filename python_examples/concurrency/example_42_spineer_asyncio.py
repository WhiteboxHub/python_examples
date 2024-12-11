#!/usr/bin/env python3

# spinner_asyncio.py

import asyncio
import itertools
import sys

async def spin(msg):  # Coroutine function
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in itertools.cycle('|/-\\'):
        status = char + ' ' + msg
        write(status)
        flush()
        write('\x08' * len(status))
        try:
            await asyncio.sleep(0.1)  # Use await instead of yield from
        except asyncio.CancelledError:
            break
    write(' ' * len(status) + '\x08' * len(status))

async def slow_function():  # Coroutine function
    # Simulate a time-consuming operation
    await asyncio.sleep(3)
    return 42

async def supervisor():  # Coroutine function
    spinner = asyncio.create_task(spin('thinking!'))  # Modern task creation
    print('spinner object:', spinner)
    result = await slow_function()  # Await the result
    spinner.cancel()  # Cancel the spinner task
    return result

def main():
    result = asyncio.run(supervisor())  # Modern event loop management
    print('Answer:', result)

if __name__ == '__main__':
    main()
