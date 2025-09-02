import nextcord
from nextcord.ext import commands
import asyncio
import config

intents = nextcord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ 봇 로그인: {bot.user}")
    print("등록된 명령어:")
    for cmd in bot.commands:
        print(f"- {cmd.name}")

initial_extensions = [
    "cogs.Economy",
    "cogs.embed_example",
    "cogs.game",
    "cogs.greetings",
    "cogs.music",
    "cogs.attendance",
]

async def load_extensions():
    for extension in initial_extensions:
        try:
            if extension not in bot.extensions:
                bot.load_extension(extension)  # await 꼭 붙이기
                print(f"✅ 확장 로드 성공: {extension}")
            else:
                print(f"⚠️ 확장이 이미 로드됨: {extension}")
        except Exception as e:
            print(f"❌ 확장 로드 실패: {extension} - {e}")

async def main():
    await load_extensions()
    await bot.start(config.DISCORD_TOKEN)

if __name__ == "__main__":
    asyncio.run(main())
