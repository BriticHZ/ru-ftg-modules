# (c) @br1t1c
# Original written by @UniBorg edit by @br1t1c

from telethon import events
import asyncio
from collections import deque


@borg.on(events.NewMessage(pattern=r"\.china", outgoing=True))
async def _(event):
	if event.fwd_from:
		return
	deq = deque(list("馃審馃實馃寧馃寧馃實馃審馃實馃寧"))
	for _ in range(48):
		await asyncio.sleep(0.1)
		await event.edit("".join(deq))
		deq.rotate(1)
    
