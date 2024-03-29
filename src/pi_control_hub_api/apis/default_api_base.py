# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pi_control_hub_api.models.device_command import DeviceCommand
from pi_control_hub_api.models.device_driver import DeviceDriver
from pi_control_hub_api.models.device_info import DeviceInfo
from pi_control_hub_api.models.finalize_pairing_request import FinalizePairingRequest
from pi_control_hub_api.models.finalize_pairing_response import FinalizePairingResponse
from pi_control_hub_api.models.paired_device import PairedDevice
from pi_control_hub_api.models.remote_layout import RemoteLayout
from pi_control_hub_api.models.start_pairing_request import StartPairingRequest
from pi_control_hub_api.models.start_pairing_response import StartPairingResponse


class BaseDefaultApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseDefaultApi.subclasses = BaseDefaultApi.subclasses + (cls,)
    async def execute_device_command(
        self,
        pairingId: str,
        commandId: int,
    ) -> None:
        """Execute the command on the paired device."""
        ...


    async def finalize_pairing(
        self,
        driverId: str,
        deviceId: str,
        pairingRequestId: str,
        finalize_pairing_request: FinalizePairingRequest,
    ) -> FinalizePairingResponse:
        """Finalize the pairing process for the device with the given device ID."""
        ...


    async def is_device_ready(
        self,
        pairingId: str,
    ) -> bool:
        """Check whether the device is ready for executing commands."""
        ...


    async def read_device_commands(
        self,
        pairingId: str,
    ) -> List[DeviceCommand]:
        """Get the commands supported by the device."""
        ...


    async def read_device_drivers(
        self,
    ) -> List[DeviceDriver]:
        """Read all installed device drivers"""
        ...


    async def read_device_remote_layout(
        self,
        pairingId: str,
    ) -> RemoteLayout:
        """Get the layout of the remote control for the device."""
        ...


    async def read_devices(
        self,
        driverId: str,
    ) -> List[DeviceInfo]:
        """Read all devices that are supported by the driver with the given driver ID"""
        ...


    async def read_paired_devices(
        self,
    ) -> List[PairedDevice]:
        """Read the list of paired devices."""
        ...


    async def start_pairing(
        self,
        driverId: str,
        deviceId: str,
        start_pairing_request: StartPairingRequest,
    ) -> StartPairingResponse:
        """Start the pairing process for the device with the given device ID."""
        ...


    async def unpair_device(
        self,
        pairingId: str,
    ) -> None:
        """Unpair the device."""
        ...
