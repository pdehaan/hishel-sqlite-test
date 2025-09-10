import logging

import hishel
import httpx

logging.basicConfig(
    level=logging.WARNING,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logging.getLogger("hishel.controller").setLevel(logging.DEBUG)


def main():
    def _log(res: httpx.Response) -> None:
        print(f"total time={res.elapsed.total_seconds()}s")
        print(f"from cache={res.extensions['from_cache']}")

    storage = hishel.SQLiteStorage(ttl=3_600)
    # NOTE: Not sure if the `trust_env` actually... does anything. 
    # https://www.python-httpx.org/environment_variables/ but I couldn't find any referneces in hishel docs.
    with hishel.CacheClient(storage=storage, trust_env=False) as client:
        res1 = client.get("https://hishel.com")
        _log(res1)

        res2 = client.get("https://hishel.com")
        _log(res2)


if __name__ == "__main__":
    main()
