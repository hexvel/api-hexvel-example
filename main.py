import asyncio
from io import BytesIO

import aiohttp


# Функция для загрузки изображения и отправки POST-запроса с использованием aiohttp
async def upload_image(url, file_path=None, params=None, avatar_path=None):
    async with aiohttp.ClientSession() as session:
        data = aiohttp.FormData()

        # Если нужно отправить фон или основное изображение
        if file_path:
            data.add_field(
                "file", open(file_path, "rb"), filename=file_path.split("/")[-1]
            )

        # Если нужно отправить аватар
        if avatar_path:
            data.add_field(
                "avatar", open(avatar_path, "rb"), filename=avatar_path.split("/")[-1]
            )

        async with session.post(url, data=data, params=params) as response:
            # Выводим статус ответа и возвращаем изображение
            print(f"Status: {response.status}")
            if response.status == 200:
                image_bytes = await response.read()
                return BytesIO(image_bytes)
            else:
                print("Error:", await response.text())
                return None


# Пример запроса для "/image/pixelate"
async def pixelate_image_example():
    url = "https://api.hexvel.ru/image/pixelate"
    file_path = "assets/bg.jpg"

    result = await upload_image(url, file_path)
    if result:
        with open("pixelated_image.png", "wb") as f:
            f.write(result.read())
        print("Pixelated image saved!")


# Пример запроса для "/image/edge"
async def edge_image_example():
    url = "https://api.hexvel.ru/image/edge"
    file_path = "assets/bg.jpg"

    result = await upload_image(url, file_path)
    if result:
        with open("edged_image.png", "wb") as f:
            f.write(result.read())
        print("Edged image saved!")


# Пример запроса для "/image/cut"
async def cut_image_example():
    url = "https://api.hexvel.ru/image/cut"
    file_path = "assets/bg.jpg"

    result = await upload_image(url, file_path)
    if result:
        with open("cropped_image.png", "wb") as f:
            f.write(result.read())
        print("Cropped image saved!")


# Пример запроса для "/image/quote"
async def quote_image_example():
    url = "https://api.hexvel.ru/image/quote"
    avatar_path = "assets/avatar.jpg"

    params = {
        "fullname": "Дилмурод Абдукаримов",
        "time": "2024-12-14 14:26",
        "text": "Тестовая фраза",
    }

    result = await upload_image(
        url, params=params, avatar_path=avatar_path
    )  # Добавляете сюда file_path если хотите изменить фон цитаты на своё изображение
    if result:
        with open("quote_image.png", "wb") as f:
            f.write(result.read())
        print("Quote image saved!")


# Основная функция для выполнения всех примеров
async def main():
    await asyncio.gather(
        pixelate_image_example(),
        edge_image_example(),
        cut_image_example(),
        quote_image_example(),
    )


# Запуск примеров
asyncio.run(main())
