# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from pi_control_hub_api.apis.default_api_base import BaseDefaultApi
import openapi_server.impl

from fastapi import (  # noqa: F401
    APIRouter,
    Body,
    Cookie,
    Depends,
    Form,
    Header,
    Path,
    Query,
    Response,
    Security,
    status,
)

from pi_control_hub_api.models.extra_models import TokenModel  # noqa: F401
from pi_control_hub_api.models.device_command import DeviceCommand
from pi_control_hub_api.models.device_driver import DeviceDriver
from pi_control_hub_api.models.device_info import DeviceInfo
from pi_control_hub_api.models.finalize_pairing_request import FinalizePairingRequest
from pi_control_hub_api.models.finalize_pairing_response import FinalizePairingResponse
from pi_control_hub_api.models.paired_device import PairedDevice
from pi_control_hub_api.models.remote_layout import RemoteLayout
from pi_control_hub_api.models.start_pairing_request import StartPairingRequest
from pi_control_hub_api.models.start_pairing_response import StartPairingResponse


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.post(
    "/paired-devices/{pairingId}/execute-command/{commandId}",
    responses={
        204: {"description": "Successfully read the remote of the paired device."},
        400: {"description": "Error while executing the command"},
        404: {"description": "Pairing not found."},
    },
    tags=["default"],
    response_model_by_alias=True,
)
async def execute_device_command(
    pairingId: str = Path(..., description="Pairing ID"),
    commandId: int = Path(..., description="Command ID"),
) -> None:
    """Execute the command on the paired device."""
    return await BaseDefaultApi.subclasses[0]().execute_device_command(pairingId, commandId)


@router.post(
    "/device-drivers/{driverId}/devices/{deviceId}/finalize_pairing/{pairingRequestId}",
    responses={
        200: {"model": FinalizePairingResponse, "description": "Successfully finalized pairing"},
        404: {"description": "Driver, device or pairing request not found."},
        406: {"description": "Not Acceptable"},
    },
    tags=["default"],
    response_model_by_alias=True,
)
async def finalize_pairing(
    driverId: str = Path(..., description="Driver ID"),
    deviceId: str = Path(..., description="Device ID"),
    pairingRequestId: str = Path(..., description="Pairing Request ID"),
    finalize_pairing_request: FinalizePairingRequest = Body(None, description=""),
) -> FinalizePairingResponse:
    """Finalize the pairing process for the device with the given device ID."""
    return await BaseDefaultApi.subclasses[0]().finalize_pairing(driverId, deviceId, pairingRequestId, finalize_pairing_request)


@router.get(
    "/paired-devices/{pairingId}/ready",
    responses={
        200: {"model": bool, "description": "Successfully checked whether device is ready."},
        404: {"description": "Pairing not found."},
    },
    tags=["default"],
    response_model_by_alias=True,
)
async def is_device_ready(
    pairingId: str = Path(..., description="Pairing ID"),
) -> bool:
    """Check whether the device is ready for executing commands."""
    return await BaseDefaultApi.subclasses[0]().is_device_ready(pairingId)


@router.get(
    "/paired-devices/{pairingId}/commands",
    responses={
        200: {"model": List[DeviceCommand], "description": "Successfully read the commands of the paired device."},
        404: {"description": "Pairing not found."},
        406: {"description": "Not Acceptable"},
    },
    tags=["default"],
    response_model_by_alias=True,
)
async def read_device_commands(
    pairingId: str = Path(..., description="Pairing ID"),
) -> List[DeviceCommand]:
    """Get the commands supported by the device."""
    return await BaseDefaultApi.subclasses[0]().read_device_commands(pairingId)


@router.get(
    "/device-drivers",
    responses={
        200: {"model": List[DeviceDriver], "description": "Successfully read the installed drivers"},
        406: {"description": "Not Acceptable"},
    },
    tags=["default"],
    response_model_by_alias=True,
)
async def read_device_drivers(
) -> List[DeviceDriver]:
    """Read all installed device drivers"""
    return await BaseDefaultApi.subclasses[0]().read_device_drivers()


@router.get(
    "/paired-devices/{pairingId}/remote-layout",
    responses={
        200: {"model": RemoteLayout, "description": "Successfully read the remote of the paired device."},
        404: {"description": "Pairing not found."},
        406: {"description": "Not Acceptable"},
    },
    tags=["default"],
    response_model_by_alias=True,
)
async def read_device_remote_layout(
    pairingId: str = Path(..., description="Pairing ID"),
) -> RemoteLayout:
    """Get the layout of the remote control for the device."""
    return await BaseDefaultApi.subclasses[0]().read_device_remote_layout(pairingId)


@router.get(
    "/device-drivers/{driverId}/devices",
    responses={
        200: {"model": List[DeviceInfo], "description": "Successfully read the devices"},
        404: {"description": "Driver not found."},
        406: {"description": "Not Acceptable"},
    },
    tags=["default"],
    response_model_by_alias=True,
)
async def read_devices(
    driverId: str = Path(..., description="Driver ID"),
) -> List[DeviceInfo]:
    """Read all devices that are supported by the driver with the given driver ID"""
    return await BaseDefaultApi.subclasses[0]().read_devices(driverId)


@router.get(
    "/paired-devices",
    responses={
        200: {"model": List[PairedDevice], "description": "Successfully read the paired devices."},
        406: {"description": "Not Acceptable"},
    },
    tags=["default"],
    response_model_by_alias=True,
)
async def read_paired_devices(
) -> List[PairedDevice]:
    """Read the list of paired devices."""
    return await BaseDefaultApi.subclasses[0]().read_paired_devices()


@router.post(
    "/device-drivers/{driverId}/devices/{deviceId}/start_pairing",
    responses={
        200: {"model": StartPairingResponse, "description": "Successfully started pairing"},
        404: {"description": "Driver or device not found."},
        406: {"description": "Not Acceptable"},
    },
    tags=["default"],
    response_model_by_alias=True,
)
async def start_pairing(
    driverId: str = Path(..., description="Driver ID"),
    deviceId: str = Path(..., description="Device ID"),
    start_pairing_request: StartPairingRequest = Body(None, description=""),
) -> StartPairingResponse:
    """Start the pairing process for the device with the given device ID."""
    return await BaseDefaultApi.subclasses[0]().start_pairing(driverId, deviceId, start_pairing_request)


@router.delete(
    "/paired-devices/{pairingId}",
    responses={
        204: {"description": "Successfully read the unpaired the device."},
        404: {"description": "Pairing not found."},
    },
    tags=["default"],
    response_model_by_alias=True,
)
async def unpair_device(
    pairingId: str = Path(..., description="Pairing ID"),
) -> None:
    """Unpair the device."""
    return await BaseDefaultApi.subclasses[0]().unpair_device(pairingId)
