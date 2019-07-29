#!/usr/bin/python
#
# Ansible Module for OpsGenie Alerts

from ansible.module_utils.basic import *
import requests

def List(url, headers):
    stdout = requests.get(url, headers=headers)
    if stdout.status_code == 200:
        module.exit_json(changed=False, responce=stdout.json())
    else:
        msg = 'Status code was not 200 :: Responded Status code %s' % stdout.status_code
        module.fail_json(msg=msg, msg1=stdout.status_code)

def Get(url, headers):
    stdout = requests.get(url, headers=headers)
    if stdout.status_code == 200:
        module.exit_json(changed=False, responce=stdout.json())
    else:
        msg = 'Status code was not 200 :: Responded Status code %s' % stdout.status_code
        module.fail_json(msg=msg, msg1=stdout.status_code)

def Create(url, headers, data):
    stdout = requests.post(url, headers=headers, data=data)
    if stdout.status_code == 201:
        module.exit_json(changed=True, responce=stdout.json())
    elif stdout.status_code == 422:
        module.exit_json(changed=False, responce="Integration with name already exists!")
    else:
        msg = 'Status code was not 201 :: Responded Status code %s' % stdout.status_code
        module.fail_json(msg=msg, msg1=stdout.status_code)

def Update(url, headers, data):
    stdout = requests.post(url, headers=headers, data=data)
    if stdout.status_code == 201:
        module.exit_json(changed=True, responce=stdout.json())
    elif stdout.status_code == 422:
        module.exit_json(changed=False, responce="Integration with name already exists!")
    else:
        msg = 'Status code was not 201 :: Responded Status code %s' % stdout.status_code
        module.fail_json(msg=msg, msg1=stdout.status_code)

def Delete(url, headers):
    stdout = requests.delete(url, headers=headers)
    if stdout.status_code == 202:
        module.exit_json(changed=True, responce=stdout.json())
    else:
        msg = 'Status code was not 202 :: Responded Status code %s' % stdout.status_code
        module.fail_json(msg=msg, msg1=stdout.status_code)

def Enable(url, headers):
    stdout = requests.post(url, headers=headers)
    if stdout.status_code == 200:
        module.exit_json(changed=True, responce=stdout.json())
    else:
        msg = 'Status code was not 200 :: Responded Status code %s' % stdout.status_code
        module.fail_json(msg=msg, msg1=stdout.status_code)

def Disable(url, headers):
    stdout = requests.post(url, headers=headers)
    if stdout.status_code == 200:
        module.exit_json(changed=True, responce=stdout.json())
    else:
        msg = 'Status code was not 200 :: Responded Status code %s' % stdout.status_code
        module.fail_json(msg=msg, msg1=stdout.status_code)

def GetActions(url, headers):
    stdout = requests.get(url, headers=headers)
    if stdout.status_code == 200:
        module.exit_json(changed=False, responce=stdout.json())
    else:
        msg = 'Status code was not 200 :: Responded Status code %s' % stdout.status_code
        module.fail_json(msg=msg, msg1=stdout.status_code)

def CreateActions(url, headers, data):
    stdout = requests.post(url, headers=headers, data=data)
    if stdout.status_code == 201:
        module.exit_json(changed=True, responce=stdout.json())
    elif stdout.status_code == 422:
        module.exit_json(changed=False, responce="Integration with name already exists!")
    else:
        msg = 'Status code was not 201 :: Responded Status code %s' % stdout.status_code
        module.fail_json(msg=msg, msg1=stdout.status_code)

def UpdateActions(url, headers, data):
    stdout = requests.post(url, headers=headers, data=data)
    if stdout.status_code == 201:
        module.exit_json(changed=True, responce=stdout.json())
    elif stdout.status_code == 422:
        module.exit_json(changed=False, responce="Integration with name already exists!")
    else:
        msg = 'Status code was not 201 :: Responded Status code %s' % stdout.status_code
        module.fail_json(msg=msg, msg1=stdout.status_code)

def main():
    global module
    module = AnsibleModule(
        argument_spec=dict(
            host=dict(required=True, type='str'),
            apiKey=dict(required=True, type='str'),
            status_code=dict(required=False, default=[200, 204], type='list'),
            operation=dict(required=False, default='list', type='str', choice=["list", "create"]),
            integration_details=dict(required=False, type='dict'),
            integration_id=dict(required=False, type='str'),
            search_id=dict(required=False, type='str'),
            integration=dict(required=False, type='str')
            )
    )

    if module.params['operation'] == "list":
        url = "https://%s/v2/integrations" % (module.params['host'])
        headers_dict = {"Authorization": "GenieKey {}" . format(module.params['apiKey'])}
        headers = json.loads(json.dumps(headers_dict))
        List(url, headers)

    if module.params['operation'] == "get":
        url = "https://%s/v2/integrations/%s?identifierType=id" % (module.params['host'], module.params['integration_id'])
        headers_dict = {"Authorization": "GenieKey {}" . format(module.params['apiKey'])}
        headers = json.loads(json.dumps(headers_dict))
        Get(url, headers)

    if module.params['operation'] == "create":
        url = "http://%s/v2/integrations" % (module.params['host'])
        headers_dict = {"Content-Type": "application/json", "Authorization": "GenieKey {}" . format(module.params['apiKey'])}
        headers = json.loads(json.dumps(headers_dict))
        data = json.dumps(module.params['integration_details'])
        Create(url, headers, data)

    if module.params['operation'] == "update":
        url = "http://%s/v2/integrations/%s" % (module.params['host'], module.params['integration_id'])
        headers_dict = {"Content-Type": "application/json", "Authorization": "GenieKey {}" . format(module.params['apiKey'])}
        headers = json.loads(json.dumps(headers_dict))
        data = json.dumps(module.params['integration_details'])
        Update(url, headers, data)

    if module.params['operation'] == "delete":
        url = "http://%s/v2/integrations/%s?identifierType=id" % (module.params['host'], module.params['integration_id'])
        headers_dict = {"Authorization": "GenieKey {}" . format(module.params['apiKey'])}
        headers = json.loads(json.dumps(headers_dict))
        Delete(url, headers)

    if module.params['operation'] == "enable":
        url = "http://%s/v2/integrations/%s/enable" % (module.params['host'], module.params['integration_id'])
        headers_dict = {"Content-Type": "application/json", "Authorization": "GenieKey {}" . format(module.params['apiKey'])}
        headers = json.loads(json.dumps(headers_dict))
        data = json.dumps(module.params['integration_details'])
        Update(url, headers, data)

    if module.params['operation'] == "disable":
        url = "http://%s/v2/integrations/%s/disable" % (module.params['host'], module.params['integration_id'])
        headers_dict = {"Content-Type": "application/json", "Authorization": "GenieKey {}" . format(module.params['apiKey'])}
        headers = json.loads(json.dumps(headers_dict))
        data = json.dumps(module.params['integration_details'])
        Update(url, headers, data)

    if module.params['operation'] == "authenticate":
        url = "http://%s/v2/integrations/%s" % (module.params['host'], module.params['integration_id'])
        headers_dict = {"Content-Type": "application/json", "Authorization": "GenieKey {}" . format(module.params['apiKey'])}
        headers = json.loads(json.dumps(headers_dict))
        data = json.dumps(module.params['integration_details'])
        Update(url, headers, data)

    if module.params['operation'] == "getactions":
        url = "https://%s/v2/integrations/%s/actions" % (module.params['host'], module.params['integration_id'])
        headers_dict = {"Authorization": "GenieKey {}" . format(module.params['apiKey'])}
        headers = json.loads(json.dumps(headers_dict))
        GetActions(url, headers)

    if module.params['operation'] == "createactions":
        url = "http://%s/v2/integrations/%s/actions" % (module.params['host'], module.params['integration_id'])
        headers_dict = {"Content-Type": "application/json", "Authorization": "GenieKey {}" . format(module.params['apiKey'])}
        headers = json.loads(json.dumps(headers_dict))
        data = json.dumps(module.params['integration_details'])
        CreateActions(url, headers, data)

    if module.params['operation'] == "updateactions":
        url = "http://%s/v2/integrations/%s/actions" % (module.params['host'], module.params['integration_id'])
        headers_dict = {"Content-Type": "application/json", "Authorization": "GenieKey {}" . format(module.params['apiKey'])}
        headers = json.loads(json.dumps(headers_dict))
        data = json.dumps(module.params['integration_details'])
        UpdateActions(url, headers, data)


if __name__ == '__main__':
    main()
