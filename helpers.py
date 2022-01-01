import requests
import os
import time


HELIUM_API_KEY = str(os.getenv("HELIUM_API_KEY"))


def helium_api_get(url):
    headers = {"User-Agent": HELIUM_API_KEY}
    return requests.get(url, headers=headers).json()


def helium_api_paginator(url, timeout=30):
    """Get helium cities data."""
    data = next_data = helium_api_get(url)
    next_cursor = data["cursor"]

    start_time = time.time()
    while "cursor" in next_data:
        next_data = requests.get(f"{url}?cursor={next_cursor}", headers=headers).json()
        next_cursor = next_data["cursor"]
        data["data"]+=next_data["data"]

        next_time = time.time()
        if next_time - start_time >= timeout:
            break

    return data["data"]


def get_hotspot(hotspot_address):
    return helium_api_get(f"https://helium-api.stakejoy.com/v1/hotspots/{hotspot_address}")["data"]


def get_top_hotspot_cities(top=100):
    return helium_api_get("https://helium-api.stakejoy.com/v1/cities?order=hotspot_count")["data"][:top]


def get_city_hotspots(city_id):
    return helium_api_get(f"https://helium-api.stakejoy.com/v1/cities/{city_id}/hotspots")["data"]


def get_city_hotspots_online(city_id):
    return [h for h in get_city_hotspots(city_id) if h["status"]["online"] == "online"]


def get_city_hotspots_offline(city_id):
    return [h for h in get_city_hotspots(city_id) if h["status"]["online"] == "offline"]


def get_hotspot_rewards_timeseries(hotspot_address, min_time="-24 hour", max_time="0 hour", bucket="hour"):
     return helium_api_get(f"https://helium-api.stakejoy.com/v1/hotspots/{hotspot_address}/rewards/sum?min_time={min_time}&max_time={max_time}&bucket={bucket}")


def get_hotspot_rewards_timeseries_24h(hotspot_address):
    min_time="-24 hour"
    max_time="0 hour"
    bucket="hour"
    return helium_api_get(f"https://helium-api.stakejoy.com/v1/hotspots/{hotspot_address}/rewards/sum?min_time={min_time}&max_time={max_time}&bucket={bucket}")


def get_hotspot_rewards_timeseries_7d(hotspot_address):
    min_time="-7 day"
    max_time="0 day"
    bucket="day"
    return helium_api_get(f"https://helium-api.stakejoy.com/v1/hotspots/{hotspot_address}/rewards/sum?min_time={min_time}&max_time={max_time}&bucket={bucket}")


def get_hotspot_rewards_timeseries_30d(hotspot_address):
    min_time="-30 day"
    max_time="0 day"
    bucket="day"
    return helium_api_get(f"https://helium-api.stakejoy.com/v1/hotspots/{hotspot_address}/rewards/sum?min_time={min_time}&max_time={max_time}&bucket={bucket}")


def get_hotspot_rewards_timeseries_average(rewards_timeseries):
    reward_total = 0
    for r in rewards_timeseries["data"]:
        reward_total+=r["total"]
    return reward_total/len(rewards_timeseries["data"])


def get_hotspot_rewards_timeseries_total(rewards_timeseries):
    reward_total = 0
    for r in rewards_timeseries["data"]:
        reward_total+=r["total"]
    return reward_total