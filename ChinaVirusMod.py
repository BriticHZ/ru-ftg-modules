from .. import loader
from asyncio import sleep
@loader.tds
class ChinaVirusMod(loader.Module):
 strings = {"name":"CninaVirus"}
 @loader.owner
 async def cviruscmd(self, message):
  for _ in range(10):
   for heart in ['寧寧馃', '馃實馃', '馃寧馃寧', '實寧馃', '馃實馃寧', '馃馃']:
    await message.edit(heart)
    await sleep(0.3)
