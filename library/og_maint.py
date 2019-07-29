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
    if ogapi.status_code == 201:
        module.exit_json(changed=True, responce=ogapi.json())
    elif ogapi.status_code == 409:
        module.exit_json(changed=False, responce=ogapi.json())
    else:
        msg = 'Status code was not 202 :: Responded Status code %s' % ogapi.status_code
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
    if ogapi.status_code == 201:
        module.exit_json(changed=True, responce=ogapi.json())
    elif ogapi.status_code == 409:
        module.exit_json(changed=False, responce=ogapi.json())
    else:
        msg = 'Status code was not 202 :: Responded Status code %s' % ogapi.status_code
        module.fail_json(msg=msg, status_code=ogapi.status_code)

def List(url, headers):
    ogapi = requests.get(url, headers=headers)
    if ogapi.status_code == 201:
        module.exit_json(changed=True, responce=ogapi.json())
    elif ogapi.status_code == 409:
        module.exit_json(changed=False, responce=ogapi.json())
    else:
        msg = 'Status code was not 202 :: Responded Status code %s' % ogapi.status_code
        module.fail_json(msg=msg, status_code=ogapi.status_code)

def Cancel(url, headers):
    ogapi = requests.post(url, headers=headers)
    if ogapi.status_code == 201:
        module.exit_json(changed=True, responce=ogapi.json())
    elif ogapi.status_code == 409:
        module.exit_json(changed=False, responce=ogapi.json())
    else:
        msg = 'Status code was not 202 :: Responded Status code %s' % ogapi.status_code
        module.fail_json(msg=msg, status_code=ogapi.status_code)

def main():
    global module
    module = AnsibleModule(
        argument_spec=dict(
            host=dict(type='str', default="api.opsgenie.com"),
            apiKey=dict(required=True, type='str'),
            status_code=dict(required=False, default=[200, 204], type='list'),
            operation=dict(required=False, default='list', type='str', choice=["list", "create"]),
            maint_details=dict(required=False, type='dict'),
            maint_id=dict(required=False, type='str'),
            username=dict(required=False, type='str')
            )
    )

    if module.params['operation'] == "create":
        url = "https://%s/v1/maintenance" % (module.params['host'])
        headers_dict = {"Content-Type": "application/json", "Authorization": "GenieKey {}" . format(module.params['apiKey'])}
        headers = json.loads(json.dumps(headers_dict))
        data = json.dumps(module.params['user_details'])
        Create(url, headers, data)

    if module.params['operation'] == "get":
        url = "https://%s/v1/maintenance/%s" % (module.params['host'], module.params['maint_id'])
        headers_dict = {"Content-Type": "application/json", "Authorization": "GenieKey {}" . format(module.params['apiKey'])}
        headers = json.loads(json.dumps(headers_dict))
        Get(url, headers)

    if module.params['operation'] == "update":
        url = "https://%s/v1/maintenance/%s" % (module.params['host'], module.params['maint_id'])
        headers_dict = {"Content-Type": "application/json", "Authorization": "GenieKey {}" . format(module.params['apiKey'])}
        headers = json.loads(json.dumps(headers_dict))
        data = json.dumps(module.params['user_details'])
        Update(url, headers, data)

    if module.params['operation'] == "delete":
        url = "https://%s/v1/maintenance/%s" % (module.params['host'], module.params['maint_id'])
        headers_dict = {"Content-Type": "application/json", "Authorization": "GenieKey {}" . format(module.params['apiKey'])}
        headers = json.loads(json.dumps(headers_dict))
        Delete(url, headers)

    if module.params['operation'] == "list":
        url = "https://%s/v1/maintenance" % (module.params['host'])
        headers_dict = {"Content-Type": "application/json", "Authorization": "GenieKey {}" . format(module.params['apiKey'])}
        headers = json.loads(json.dumps(headers_dict))
        List(url, headers)

    if module.params['operation'] == "cancel":
        url = "https://%s/v1/maintenance/%/cancel" % (module.params['host'], module.params['maint_id'])
        headers_dict = {"Content-Type": "application/json", "Authorization": "GenieKey {}" . format(module.params['apiKey'])}
        headers = json.loads(json.dumps(headers_dict))
        Cancel(url, headers)

if __name__ == '__main__':
    main()
