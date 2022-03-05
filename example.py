import argparse
import asyncio
from argparse import ArgumentParser
from configparser import ConfigParser

from client import IRacingApiClient


async def main(client: IRacingApiClient):
    documentation = client.get_documentation()
    # print(documentation)

    series_seasons = client.get_series_seasons(include_series=True)
    # print(series_seasons)

    season_id = series_seasons[0]["schedules"][0]["season_id"]
    season_results = client.get_season_results(season_id=season_id)
    print(season_results)
    return


def get_config(config_file: str) -> tuple[str, str]:
    config = ConfigParser()
    config.read(config_file)
    email = config["iRacing"]["Email"]
    password = config["iRacing"]["Password"]
    return email, password


if __name__ == "__main__":
    arg_parser = ArgumentParser(description="Example API Usage")
    arg_parser.add_argument('--config', metavar='path', required=True,
                        help='The path to the config file')
    args = arg_parser.parse_args()
    email, password = get_config(args.config)
    client = IRacingApiClient(email, password)
    client.connect()
    asyncio.run(main(client))
