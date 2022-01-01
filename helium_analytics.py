import requests
import os
import json

import helpers


def get_hotspot_rewards_average_timeseries_by_city(city_id):
    online_hotspots = helpers.get_city_hotspots_online(city_id)
    hotspot_rewards_timeseries_averages = []
    for hotspot in online_hotspots:
        print(hotspot["name"])
        hotspot_address = hotspot["address"]
        hotspot_rewards_ts = helpers.get_hotspot_rewards_timeseries_7d(hotspot_address)
        hotspot_rewards_timeseries_averages.append(
            helpers.get_hotspot_rewards_timeseries_average(hotspot_rewards_ts)
        )
    
    reward_total = 0
    for r in hotspot_rewards_timeseries_averages:
        reward_total+=r
    return reward_total/len(hotspot_rewards_timeseries_averages)


def main():
    # print("Salt Lake City hotspots reward average for last 30 days")
    # slc_city_id = "c2FsdCBsYWtlIGNpdHl1dGFodW5pdGVkIHN0YXRlcw"
    # hotspot_rewards_average_timeseries = get_hotspot_rewards_average_timeseries_by_city(slc_city_id)
    # print(hotspot_rewards_average_timeseries)

    hotspot_address = str(os.getenv("HELIUM_HOTSPOT_ADDRESS"))
    print(f"{helpers.get_hotspot(hotspot_address)['name']} hotspot rewards")

    rewards_timeseries = helpers.get_hotspot_rewards_timeseries_24h(hotspot_address)
    print("hotspot rewards average for last 24 hours")
    print(helpers.get_hotspot_rewards_timeseries_average(rewards_timeseries))
    print("hotspot rewards total for last 24 hours")
    print(helpers.get_hotspot_rewards_timeseries_total(rewards_timeseries))

    rewards_timeseries = helpers.get_hotspot_rewards_timeseries_7d(hotspot_address)
    print("hotspot rewards average for last 7 days")
    print(helpers.get_hotspot_rewards_timeseries_average(rewards_timeseries))
    print("hotspot rewards total for last 7 days")
    print(helpers.get_hotspot_rewards_timeseries_total(rewards_timeseries))

    rewards_timeseries = helpers.get_hotspot_rewards_timeseries_30d(hotspot_address)
    print("hotspot rewards average for last 30 days")
    print(helpers.get_hotspot_rewards_timeseries_average(rewards_timeseries))
    print("hotspot rewards total for last 30 days")
    print(helpers.get_hotspot_rewards_timeseries_total(rewards_timeseries))


if __name__ == "__main__":
    main()