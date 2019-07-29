#!/usr/bin/python
#
# Ansible Module for OpsGenie Alerts

from ansible.module_utils.basic import *
import requests

def Ping(url, headers):
    stdout = requests.get(url, headers=headers)
    if stdout.status_code == 200:
        module.exit_json(changed=True, responce=stdout.json())
    else:
        msg = 'Status code was not 200 :: Responded Status code %s' % stdout.status_code
        module.fail_json(msg=msg, status_code=stdout.status_code)

def Create(url, headers, data):
    stdout = requests.post(url, headers=headers, data=data)
    if stdout.status_code == 202:
        module.exit_json(changed=True, responce=stdout.json())
    elif stdout.status_code == 409:
        module.exit_json(changed=False, responce=stdout.json())
    else:
        msg = 'Status code was not 202 :: Responded Status code %s' % stdout.status_code
        module.fail_json(msg=msg, status_code=stdout.status_code)

def Get(url, headers):
    stdout = requests.get(url, headers=headers)
    if stdout.status_code == 200:
        module.exit_json(changed=True, responce=stdout.json())
    else:
        msg = 'Status code was not 200 :: Responded Status code %s' % stdout.status_code
        module.fail_json(msg=msg, status_code=stdout.status_code)

def List(url, headers):
    stdout = requests.get(url, headers=headers)
    if stdout.status_code == 200:
        module.exit_json(changed=True, responce=stdout.json())
    else:
        msg = 'Status code was not 200 :: Responded Status code %s' % stdout.status_code
        module.fail_json(msg=msg, status_code=stdout.status_code)

def Update(url, headers, data):
    stdout = requests.patch(url, headers=headers, data=data)
    if stdout.status_code == 202:
        module.exit_json(changed=True, responce=stdout.json())
    else:
        msg = 'Status code was not 202 :: Responded Status code %s' % stdout.status_code
        module.fail_json(msg=msg, status_code=stdout.status_code)

def Delete(url, headers):
    stdout = requests.delete(url, headers=headers)
    if stdout.status_code == 202:
        module.exit_json(changed=True, responce=stdout.json())
    else:
        msg = 'Status code was not 202 :: Responded Status code %s' % stdout.status_code
        module.fail_json(msg=msg, status_code=stdout.status_code)

def Enable(url, headers):
    stdout = requests.post(url, headers=headers)
    if stdout.status_code == 200:
        module.exit_json(changed=True, responce=stdout.json())
    else:
        msg = 'Status code was not 200 :: Responded Status code %s' % stdout.status_code
        module.fail_json(msg=msg, status_code=stdout.status_code)

def Disable(url, headers):
    stdout = requests.post(url, headers=headers)
    if stdout.status_code == 200:
        module.exit_json(changed=True, responce=stdout.json())
    else:
        msg = 'Status code was not 200 :: Responded Status code %s' % stdout.status_code
        module.fail_json(msg=msg, status_code=stdout.status_code)

def main():
    global module
    module = AnsibleModule(
        argument_spec=dict(
            host=dict(type='str', default="api.opsgenie.com"),
            apiKey=dict(required=True, type='str'),
            status_code=dict(required=False, default=[200, 204], type='list'),
            operation=dict(required=False, default='list', type='str', choice=["list", "create"]),
            user_details=dict(required=False, type='dict'),
            user_id=dict(required=False, type='str'),
            search_id=dict(required=False, type='str'),
            file=dict(required=False, type='str'),
            username=dict(required=False, type='str')
            )
    )

    if module.params['operation'] == "ping":
        url = "https://%s/v2/heartbeats/%s/ping" % (module.params['host'], module.params['heartbeat_name'])
        headers_dict = {"Content-Type": "application/json", "Authorization": "GenieKey {}" . format(module.params['apiKey'])}
        headers = json.loads(json.dumps(headers_dict))
        Ping(url, headers)

    if module.params['operation'] == "create":
        url = "https://%s/v2/heartbeats" % (module.params['host'])
        headers_dict = {"Content-Type": "application/json", "Authorization": "GenieKey {}" . format(module.params['apiKey'])}
        headers = json.loads(json.dumps(headers_dict))
        data = json.dumps(module.params['user_details'])
        Create(url, headers, data)

    if module.params['operation'] == "get":
        url = "https://%s/v2/heartbeats/%s" % (module.params['host'], module.params['heartbeat_name'])
        headers_dict = {"Content-Type": "application/json", "Authorization": "GenieKey {}" . format(module.params['apiKey'])}
        headers = json.loads(json.dumps(headers_dict))
        Get(url, headers)

    if module.params['operation'] == "list":
        url = "https://%s/v2/heartbeats" % (module.params['host'])
        headers_dict = {"Content-Type": "application/json", "Authorization": "GenieKey {}" . format(module.params['apiKey'])}
        headers = json.loads(json.dumps(headers_dict))
        List(url, headers)

    if module.params['operation'] == "update":
        url = "https://%s/v2/heartbeats/%s" % (module.params['host'], module.params['heartbeat_name'])
        headers_dict = {"Content-Type": "application/json", "Authorization": "GenieKey {}" . format(module.params['apiKey'])}
        headers = json.loads(json.dumps(headers_dict))
        data = json.dumps(module.params['user_details'])
        Update(url, headers, data)

    if module.params['operation'] == "delete":
        url = "https://%s/v2/heartbeats/%s" % (module.params['host'], module.params['heartbeat_name'])
        headers_dict = {"Content-Type": "application/json", "Authorization": "GenieKey {}" . format(module.params['apiKey'])}
        headers = json.loads(json.dumps(headers_dict))
        Delete(url, headers)

    if module.params['operation'] == "enable":
        url = "https://%s/v2/heartbeats/%s/enable" % (module.params['host'], module.params['heartbeat_name'])
        headers_dict = {"Content-Type": "application/json", "Authorization": "GenieKey {}" . format(module.params['apiKey'])}
        headers = json.loads(json.dumps(headers_dict))
        Enable(url, headers)

    if module.params['operation'] == "disable":
        url = "https://%s/v2/heartbeats/%s/disable" % (module.params['host'], module.params['heartbeat_name'])
        headers_dict = {"Content-Type": "application/json", "Authorization": "GenieKey {}" . format(module.params['apiKey'])}
        headers = json.loads(json.dumps(headers_dict))
        Disable(url, headers)

if __name__ == '__main__':
    main()
