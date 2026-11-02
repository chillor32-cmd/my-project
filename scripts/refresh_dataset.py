"""Power BI Dataset Refresh Trigger via REST API.

This script demonstrates how to authenticate with Microsoft Entra ID
(formerly Azure AD) using a Service Principal or Device Code, and trigger
an asynchronous refresh of a Power BI semantic model (dataset).

Prerequisites:
    pip install msal requests

Environment variables:
    PBI_TENANT_ID: Azure AD Tenant ID
    PBI_CLIENT_ID: Registered App / Service Principal Client ID
    PBI_CLIENT_SECRET: Service Principal Secret (for unattended execution)
    PBI_WORKSPACE_ID: Power BI Workspace GUID
    PBI_DATASET_ID: Power BI Semantic Model / Dataset GUID
"""

import os
import sys
import requests
import msal


def get_access_token(tenant_id: str, client_id: str, client_secret: str) -> str:
    authority = f"https://login.microsoftonline.com/{tenant_id}"
    scope = ["https://analysis.windows.net/powerbi/api/.default"]

    app = msal.ConfidentialClientApplication(
        client_id=client_id,
        client_credential=client_secret,
        authority=authority,
    )

    result = app.acquire_token_for_client(scopes=scope)
    if "access_token" in result:
        return result["access_token"]
    else:
        error_msg = result.get("error_description", result.get("error"))
        raise RuntimeError(f"Authentication failed: {error_msg}")


def trigger_dataset_refresh(workspace_id: str, dataset_id: str, token: str) -> dict:
    url = f"https://api.powerbi.com/v1.0/myorg/groups/{workspace_id}/datasets/{dataset_id}/refreshes"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }

    payload = {
        "notifyOption": "MailOnFailure"
    }

    response = requests.post(url, headers=headers, json=payload, timeout=30)
    if response.status_code == 202:
        print(f"Successfully triggered refresh for dataset: {dataset_id}")
        return {"status": "Accepted", "code": 202}
    else:
        print(f"Failed to trigger refresh. Status code: {response.status_code}")
        print(response.text)
        response.raise_for_status()


def main():
    tenant_id = os.getenv("PBI_TENANT_ID")
    client_id = os.getenv("PBI_CLIENT_ID")
    client_secret = os.getenv("PBI_CLIENT_SECRET")
    workspace_id = os.getenv("PBI_WORKSPACE_ID")
    dataset_id = os.getenv("PBI_DATASET_ID")

    if not all([tenant_id, client_id, client_secret, workspace_id, dataset_id]):
        print(
            "Missing environment variables. Please set PBI_TENANT_ID, PBI_CLIENT_ID, "
            "PBI_CLIENT_SECRET, PBI_WORKSPACE_ID, and PBI_DATASET_ID."
        )
        sys.exit(1)

    token = get_access_token(tenant_id, client_id, client_secret)
    trigger_dataset_refresh(workspace_id, dataset_id, token)


if __name__ == "__main__":
    main()
