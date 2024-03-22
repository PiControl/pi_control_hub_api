# coding: utf-8

from fastapi.testclient import TestClient


from pi_control_hub_api.models.device_command import DeviceCommand  # noqa: F401
from pi_control_hub_api.models.device_driver import DeviceDriver  # noqa: F401
from pi_control_hub_api.models.device_info import DeviceInfo  # noqa: F401
from pi_control_hub_api.models.finalize_pairing_request import FinalizePairingRequest  # noqa: F401
from pi_control_hub_api.models.finalize_pairing_response import FinalizePairingResponse  # noqa: F401
from pi_control_hub_api.models.paired_device import PairedDevice  # noqa: F401
from pi_control_hub_api.models.remote_layout import RemoteLayout  # noqa: F401
from pi_control_hub_api.models.start_pairing_request import StartPairingRequest  # noqa: F401
from pi_control_hub_api.models.start_pairing_response import StartPairingResponse  # noqa: F401


def test_execute_device_command(client: TestClient):
    """Test case for execute_device_command

    
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/paired-devices/{pairingId}/execute-command/{commandId}".format(pairingId='pairing_id_example', commandId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_finalize_pairing(client: TestClient):
    """Test case for finalize_pairing

    
    """
    finalize_pairing_request = {"device_provides_pin":1,"pin":"pin"}

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/device-drivers/{driverId}/devices/{deviceId}/finalize_pairing/{pairingRequestId}".format(driverId='driver_id_example', deviceId='device_id_example', pairingRequestId='pairing_request_id_example'),
    #    headers=headers,
    #    json=finalize_pairing_request,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_read_device_commands(client: TestClient):
    """Test case for read_device_commands

    
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/paired-devices/{pairingId}/commands".format(pairingId='pairing_id_example'),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_read_device_drivers(client: TestClient):
    """Test case for read_device_drivers

    
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/device-drivers",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_read_device_remote_layout(client: TestClient):
    """Test case for read_device_remote_layout

    
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/paired-devices/{pairingId}/remote-layout".format(pairingId='pairing_id_example'),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_read_devices(client: TestClient):
    """Test case for read_devices

    
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/device-drivers/{driverId}/devices".format(driverId='driver_id_example'),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_read_paired_devices(client: TestClient):
    """Test case for read_paired_devices

    
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/paired-devices",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_start_pairing(client: TestClient):
    """Test case for start_pairing

    
    """
    start_pairing_request = {"remote_name":"remoteName"}

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/device-drivers/{driverId}/devices/{deviceId}/start_pairing".format(driverId='driver_id_example', deviceId='device_id_example'),
    #    headers=headers,
    #    json=start_pairing_request,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_unpair_device(client: TestClient):
    """Test case for unpair_device

    
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/paired-devices/{pairingId}".format(pairingId='pairing_id_example'),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

