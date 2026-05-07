import discord
from discord import app_commands
import asyncio

# كود المطور عبدالعزيز الزهراني - جحفلة 24 ساعة
TOKEN = 'MTUwMTk1NjYwMzY0NDA4NDQ2NQ.GWo-Hh.RjoO4zKS4J3mIri8BOLLVaMptYAI8ouPAupMyA'

class MyBot(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()
        print(f"Logged in as {self.user} | Developer: Abdulaziz Al-Zahrani")

client = MyBot()

@client.tree.command(name="sp", description="سبام المطور الزهراني")
@app_commands.describe(text="الكلام اللي تبي ترسل", count="عدد المرات")
async def sp(interaction: discord.Interaction, text: str, count: int):
    # رد مخفي عشان ديسكورد ما يعطيك خطأ
    await interaction.response.send_message(f"تم بدء الجحفلة: {text}", ephemeral=True)
    for i in range(count):
        try:
            await interaction.channel.send(text)
            await asyncio.sleep(0.6) # وقت بسيط للحماية من البند
        except:
            break

client.run(TOKEN)
