import asyncio
import logging

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from openai import OpenAI

TG = "6942927465:AAH01rnoDF9V0IEIpGxLZvKpg7HQYOEtjEE"
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

dp = Dispatcher()


@dp.message(Command("ai"))
async def handle_llm(message: types.Message):
    await message.answer(
        text="Generating..."
    )

    completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "Dont mind '/ai', if asked in other language then speak that same language"},
            {"role": "user", "content": f"{message.text}"},
        ],
        model="Mistral-7B-Instruct-v0.2-GGU",
        temperature=0.7,
    )

    await message.answer(
        text=f"{completion.choices[0].message.content}"
    )


async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=TG)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
