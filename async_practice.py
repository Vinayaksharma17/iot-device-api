import asyncio


async def fetch_device_details() -> dict:
    print("Fetching device details...")
    await asyncio.sleep(1)
    return {
        "id": 1,
        "name": "Temperature Sensor 01",
    }


async def fetch_telemetry() -> dict:
    print("Fetching latest telemetry...")
    await asyncio.sleep(1)
    return {
        "temperature": 25.4,
        "unit": "Celsius",
    }

async def main() -> None:
    # TODO: Fetch both results concurrently using asyncio.gather()
    device_details, telemetry = await asyncio.gather(
          fetch_device_details(),
          fetch_telemetry()
    )
    print ("Device details: ", device_details)
    print ("Telemtry details: ", telemetry)

if __name__ == "__main__":
    asyncio.run(main())