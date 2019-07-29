#!/usr/bin/python
#
# Ansible Module for OpsGenie Alerts

from ansible.module_utils.basic import *
import requests

def Create(url, headers, data):
    ogapi = requests.post(url, headers=headers, data=data)
    if ogapi.status_code == 201:
        module.exit_json(changed=True, responce=ogapi.json())
    elif ogapi.status_code == 409:
        module.exit_json(changed=False, responce=ogapi.json())
    else:
        msg = 'Status code was not 202 :: Responded Status code %s' % ogapi.status_code
        module.fail_json(msg=msg, status_code=ogapi.status_code)

def Get(url, headers):
    ogapi = requests.get(url, headers=headers)
    if ogapi.status_code == 200:
        module.exit_json(changed=True, responce=ogapi.json())
    else:
        msg = 'Status code was not 200 :: Responded Status code %s' % ogapi.status_code
        module.fail_json(msg=msg, status_code=ogapi.status_code)

def Update(url, headers, data):
    ogapi = requests.put(url, headers=headers, data=data)
    if ogapi.status_code == 201:
        module.exit_json(changed=True, responce=ogapi.json())
    elif ogapi.status_code == 409:
        module.exit_json(changed=False, responce=ogapi.json())
    else:
        msg = 'Status code was not 202 :: Responded Status code %s' % ogapi.status_code
        module.fail_json(msg=msg, status_code=ogapi.status_code)

def Delete(url, headers):
    ogapi = requests.delete(url, headers=headers)
    if ogapi.status_code == 200:
        module.exit_json(changed=True, responce=ogapi.json())
    else:
        msg = 'Status code was not 200 :: Responded Status code %s' % ogapi.status_code
        module.fail_json(msg=msg, status_code=ogapi.status_code)

def Disable(url, headers):
    ogapi = requests.post(url, headers=headers)
    if ogapi.status_code == 200:
        module.exit_json(changed=True, responce=ogapi.json())
    else:
        msg = 'Status code was not 200 :: Responded Status code %s' % ogapi.status_code
        module.fail_json(msg=msg, status_code=ogapi.status_code)

def Enable(url, headers):
    ogapi = requests.post(url, headers=headers)
    if ogapi.status_code == 200:
        module.exit_json(changed=True, responce=ogapi.json())
    else:
        msg = 'Status code was not 200 :: Responded Status code %s' % ogapi.status_code
        module.fail_json(msg=msg, status_code=ogapi.status_code)

def Change(url, headers):
    ogapi = requests.post(url, headers=headers)
    if ogapi.status_code == 200:
        module.exit_json(changed=True, responce=ogapi.json())
    else:
        msg = 'Status code was not 200 :: Responded Status code %s' % ogapi.status_code
        module.fail_json(msg=msg, status_code=ogapi.status_code)

def ListAlerts(url, headers):
    ogapi = requests.get(url, headers=headers)
    if ogapi.status_code == 200:
        module.exit_json(changed=True, responce=ogapi.json())
    else:
        msg = 'Status code was not 200 :: Responded Status code %s' % ogapi.status_code
        module.fail_json(msg=msg, status_code=ogapi.status_code)

def ListNotifications(url, headers):
    ogapi = requests.get(url, headers=headers)
    if ogapi.status_code == 200:
        module.exit_json(changed=True, responce=ogapi.json())
    else:
        msg = 'Status code was not 200 :: Responded Status code %s' % ogapi.status_code
        module.fail_json(msg=msg, status_code=ogapi.status_code)

def main():
    global module
    module = AnsibleModule(
        argument_spec=dict(
            host=dict(type='str', default="api.opsgenie.com"),
            apiKey=dict(required=True, type='str'),
            status_code=dict(required=False, default=[200, 204], type='list'),
            operation=dict(required=False, default='list', type='str', choice=["list", "create"]),
            policy_details=dict(required=False, type='dict'),
            policy_id=dict(required=False, type='str'),
            policy_name=dict(required=False, type='str')
            )
    )

    if module.params['operation'] == "create":
        url = "https://%s/v2/policies" % (module.params['host'])
        headers_dict = {"Content-Type": "application/json", "Authorization": "GenieKey {}" . format(module.params['apiKey'])}
        headers = json.loads(json.dumps(headers_dict))
        data = json.dumps(module.params['policy_details'])
        Create(url, headers, data)

    if module.params['operation'] == "get":
        url = "https://%s/v2/policies/%s" % (module.params['host'], module.params['policy_id'])
        headers_dict = {"Content-Type": "application/json", "Authorization": "GenieKey {}" . format(module.params['apiKey'])}
        headers = json.loads(json.dumps(headers_dict))
        Get(url, headers)

    if module.params['operation'] == "update":
        url = "https://%s/v2/policies/%s" % (module.params['host'], module.params['policy_id'])
        headers_dict = {"Content-Type": "application/json", "Authorization": "GenieKey {}" . format(module.params['apiKey'])}
        headers = json.loads(json.dumps(headers_dict))
        data = json.dumps(module.params['policy_details'])
        Update(url, headers, data)

    if module.params['operation'] == "delete":
        url = "https://%s/v2/policies/%s" % (module.params['host'], module.params['policy_id'])
        headers_dict = {"Content-Type": "application/json", "Authorization": "GenieKey {}" . format(module.params['apiKey'])}
        headers = json.loads(json.dumps(headers_dict))
        Delete(url, headers)

    if module.params['operation'] == "disable":
        url = "https://%s/v2/policies/%s/disable" % (module.params['host'], module.params['policy_id'])
        headers_dict = {"Content-Type": "application/json", "Authorization": "GenieKey {}" . format(module.params['apiKey'])}
        headers = json.loads(json.dumps(headers_dict))
        Disable(url, headers)

    if module.params['operation'] == "enable":
        url = "https://%s/v2/policies/%s/enable" % (module.params['host'], module.params['policy_id'])
        headers_dict = {"Content-Type": "application/json", "Authorization": "GenieKey {}" . format(module.params['apiKey'])}
        headers = json.loads(json.dumps(headers_dict))
        Enable(url, headers)

    if module.params['operation'] == "change":
        url = "https://%s/v2/policies/%s/change-order" % (module.params['host'], module.params['policy_id'])
        headers_dict = {"Content-Type": "application/json", "Authorization": "GenieKey {}" . format(module.params['apiKey'])}
        headers = json.loads(json.dumps(headers_dict))
        Change(url, headers)

    if module.params['operation'] == "change":
        url = "https://%s/v2/policies/%s/change-order" % (module.params['host'], module.params['policy_id'])
        headers_dict = {"Content-Type": "application/json", "Authorization": "GenieKey {}" . format(module.params['apiKey'])}
        headers = json.loads(json.dumps(headers_dict))
        Change(url, headers)

    if module.params['operation'] == "listalerts":
        url = "https://%s/v2/policies/alert" % (module.params['host'], module.params['policy_id'])
        headers_dict = {"Content-Type": "application/json", "Authorization": "GenieKey {}" . format(module.params['apiKey'])}
        headers = json.loads(json.dumps(headers_dict))
        ListAlerts(url, headers)

    if module.params['operation'] == "listnotifications":
        url = "https://%s/v2/policies/notification" % (module.params['host'], module.params['policy_id'])
        headers_dict = {"Content-Type": "application/json", "Authorization": "GenieKey {}" . format(module.params['apiKey'])}
        headers = json.loads(json.dumps(headers_dict))
        ListNotifications(url, headers)

if __name__ == '__main__':
    main()
