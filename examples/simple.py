import asyncio
import sys
import os
import logging
import platform

from enterble import DeviceScanner, FlowtimeCollector

from algorithm.base_services import BaseServices

if sys.version_info < (3, 7):
    asyncio.get_running_loop = asyncio._get_running_loop

logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s - %(asctime)s - %(name)s - %(message)s'
)
logger = logging.getLogger(__name__)


def bleak_log(level=logging.INFO):
    import bleak
    logging.getLogger('bleak').setLevel(level=level)


async def get_device():
    devices = await DeviceScanner.discover(
        name=None,
        model_nbr_uuid='0000ff10-1212-abcd-1523-785feabcd123',
    )
    if not devices:
        raise Exception('No device found, please try again later.')

    for device in devices:
        try:
            services = await device.get_services()
            for _id, service in services.characteristics.items():
                logger.info(f'{device} - {_id} - {service}')
            MAC = await device.get_mac_address()
            logger.info(
                f'{device} - {MAC}'
            )
        except Exception as e:
            logger.error(f'{device} - {device.identify} - {e}')


async def data_collector():

    async def soc_callback(soc):
        logger.info(f'SOC: {soc}')
        pass

    async def wear_status_callback(wear_status):
        logger.info(f'Wear status: {wear_status}')
        pass

    async def eeg_data_collector(data):
        logger.info(f'EEG: {data}')
        pass

    async def hr_data_collector(data):
        logger.info(f'HR: {data}')
        pass

    model_nbr_uuid = '0000ff10-1212-abcd-1523-785feabcd123'
    device_identify = (
        "FB:EC:25:DE:1A:92"
        if platform.system() != "Darwin"
        # else "AAE31983-8A63-BBA9-3CD4-3EBECC8C315D"
        # else "D5D4362A-1690-4204-B797-3015EEDB510E"
        else "7500F2E8-4606-48EF-8CAB-72E1949D15E4"
    )

    collector = FlowtimeCollector(
        name='Flowtime',
        model_nbr_uuid=model_nbr_uuid,
        device_identify=device_identify,
        soc_data_callback=soc_callback,
        wear_status_callback=wear_status_callback,
        eeg_data_callback=eeg_data_collector,
        hr_data_callback=hr_data_collector,
    )
    await collector.start()
    await collector.wait_for_stop()


async def ws_client():
    from client import ACClient
    from protocols.protocol import Services

    client: ACClient = None

    async def session_create(data: str) -> None:
        print(f"< {data}")
        await client.init_base_services(services=[
            BaseServices.EEG,
            BaseServices.HR,
        ])

    async def session_restore(data: str) -> None:
        print(f"< {data}")

    async def session_close(data: str) -> None:
        print(f"< {data}")

    async def base_service_init(data: str) -> None:
        print(f"< {data}")
        await client.subscribe_base_services(services=[
            BaseServices.EEG,
            BaseServices.HR,
        ])

    async def base_service_subscribe(data: str) -> None:
        print(f"< {data}")

    async def base_service_report(data: str) -> None:
        print(f"< {data}")

    async def affective_service_start(data: str) -> None:
        print(f"< {data}")

    async def affective_service_subscribe(data: str) -> None:
        print(f"< {data}")

    async def affective_service_report(data: str) -> None:
        print(f"< {data}")

    async def affective_service_finish(data: str) -> None:
        print(f"< {data}")

    # wss://server.affectivecloud.com/ws/algorithm/v2/
    # ws://localhost:8765
    client = ACClient(
        url="wss://server-test.affectivecloud.cn/ws/algorithm/v2/",
        app_key=os.environ.get("APP_KEY"),
        secret=os.environ.get("APP_SECRET"),
        client_id=os.environ.get("CLIENT_ID"),
        recv_callbacks={
            Services.Type.SESSION: {
                Services.Operation.Session.CREATE: session_create,
                Services.Operation.Session.RESTORE: session_restore,
                Services.Operation.Session.CLOSE: session_close,
            },
            Services.Type.BASE_SERVICE: {
                Services.Operation.BaseService.INIT: base_service_init,
                Services.Operation.BaseService.SUBSCRIBE: base_service_subscribe,
                Services.Operation.BaseService.REPORT: base_service_report,
            },
            Services.Type.AFFECTIVE_SERVICE: {
                Services.Operation.AffectiveService.START: affective_service_start,
                Services.Operation.AffectiveService.SUBSCRIBE: affective_service_subscribe,
                Services.Operation.AffectiveService.REPORT: affective_service_report,
                Services.Operation.AffectiveService.FINISH: affective_service_finish,
            },
        }
    )
    await client.connect()

    await client.create_session()

    while not client.ws.closed:
        await asyncio.sleep(10)

    print("websocket closed")


if __name__ == '__main__':
    bleak_log(logging.INFO)

    loop = asyncio.get_event_loop()
    # loop.run_until_complete(get_device())
    loop.run_until_complete(data_collector())
    # loop.run_until_complete(ws_client())
