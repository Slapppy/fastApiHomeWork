import asyncio
import json
import aiohttp


async def fetch_movie_info(movie_id):
    async with aiohttp.ClientSession() as session:
        url = f'https://api.themoviedb.org/3/movie/{movie_id}'
        params = {
            'api_key': '48f1f9d375fb1c3e0e82e88747a49ee2'
        }
        async with session.get(url, params=params) as response:
            data = await response.json()
            return data


async def main():
    movie_ids = [12, 13, 14]  # список идентификаторов фильмов
    tasks = [asyncio.create_task(fetch_movie_info(id)) for id in movie_ids]
    results = await asyncio.gather(*tasks)
    for i, result in enumerate(results):
        with open(f'movie_info_{i}.json', 'w') as f:
            json.dump(result, f)


if __name__ == '__main__':
    asyncio.run(main())
