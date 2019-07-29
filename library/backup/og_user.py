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
        module.exit_json(changed=False, responce=ogapi.json())
    elif ogapi.status_code == 404:
        module.exit_json(failed=True, responce='User does not exist!')

    else:
        msg = 'Status code was not 200 :: Responded Status code %s' % ogapi.status_code
        module.fail_json(msg=msg)

def Update(url, headers, data):
    ogapi = requests.patch(url, headers=headers, data=data)
    if ogapi.status_code == 200:
        module.exit_json(changed=True, responce=ogapi.json())
    else:
        msg = 'Status code was not 202 :: Responded Status code %s' % ogapi.status_code
        module.fail_json(msg=msg, status_code=ogapi.status_code)

def Delete(url, headers):
    ogapi = requests.delete(url, headers=headers)
    if ogapi.status_code == 200:
        module.exit_json(changed=True, responce=ogapi.json())
    elif ogapi.status_code == 404:
        module.exit_json(failed=True, responce='User does not exist!')
    else:
        msg = 'Status code was not 200 :: Responded Status code %s' % ogapi.status_code
        module.fail_json(msg=msg)

def List(url, headers):
    ogapi = requests.get(url, headers=headers)
    if ogapi.status_code == 200:
        module.exit_json(changed=False, responce=ogapi.json())
    elif ogapi.status_code == 404:
        module.exit_json(failed=True, responce='User does not exist!')
    else:
        msg = 'Status code was not 200 :: Responded Status code %s' % ogapi.status_code
        module.fail_json(msg=msg)

def Escalations(url, headers):
    ogapi = requests.get(url, headers=headers)
    if ogapi.status_code == 200:
        module.exit_json(changed=False, responce=ogapi.json())
    elif ogapi.status_code == 404:
        module.exit_json(failed=True, responce='User does not exist!')
    else:
        msg = 'Status code was not 200 :: Responded Status code %s' % ogapi.status_code
        module.fail_json(msg=msg)

def Teams(url, headers):
    ogapi = requests.get(url, headers=headers)
    if ogapi.status_code == 200:
        module.exit_json(changed=False, responce=ogapi.json())
    elif ogapi.status_code == 404:
        module.exit_json(failed=True, responce='User does not exist!')
    else:
        msg = 'Status code was not 200 :: Responded Status code %s' % ogapi.status_code
        module.fail_json(msg=msg)

def Forwarding(url, headers):
    ogapi = requests.get(url, headers=headers)
    if ogapi.status_code == 200:
        module.exit_json(changed=False, responce=ogapi.json())
    elif ogapi.status_code == 404:
        module.exit_json(failed=True, responce='User does not exist!')
    else:
        msg = 'Status code was not 200 :: Responded Status code %s' % ogapi.status_code
        module.fail_json(msg=msg)

def Schedules(url, headers):
    ogapi = requests.get(url, headers=headers)
    if ogapi.status_code == 200:
        module.exit_json(changed=False, responce=ogapi.json())
    elif ogapi.status_code == 404:
        module.exit_json(failed=True, responce='User does not exist!')
    else:
        msg = 'Status code was not 200 :: Responded Status code %s' % ogapi.status_code
        module.fail_json(msg=msg)

def ListSavedSearch(url, headers):
    ogapi = requests.get(url, headers=headers)
    if ogapi.status_code == 200:
        module.exit_json(changed=False, responce=ogapi.json())
    elif ogapi.status_code == 404:
        module.exit_json(failed=True, responce='User does not exist!')
    else:
        msg = 'Status code was not 200 :: Responded Status code %s' % ogapi.status_code
        module.fail_json(msg=msg)

def GetSavedSearch(url, headers):
    ogapi = requests.get(url, headers=headers)
    if ogapi.status_code == 200:
        module.exit_json(changed=False, responce=ogapi.json())
    elif ogapi.status_code == 404:
        module.exit_json(failed=True, responce='User does not exist!')
    else:
        msg = 'Status code was not 200 :: Responded Status code %s' % ogapi.status_code
        module.fail_json(msg=msg)

def DeleteSavedSearch(url, headers):
    ogapi = requests.delete(url, headers=headers)
    if ogapi.status_code == 200:
        module.exit_json(changed=False, responce=ogapi.json())
    elif ogapi.status_code == 404:
        module.exit_json(failed=True, responce='User does not exist!')
    else:
        msg = 'Status code was not 200 :: Responded Status code %s' % ogapi.status_code
        module.fail_json(msg=msg)

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
            user=dict(required=False, type='str')
            )
    )

    if module.params['operation'] == "create":
        url = "https://%s/v2/users" % (module.params['host'])
        headers_dict = {"Content-Type": "application/json", "Authorization": "GenieKey {}" . format(module.params['apiKey'])}
        headers = json.loads(json.dumps(headers_dict))
        data = json.dumps(module.params['user_details'])
        Create(url, headers, data)

    if module.params['operation'] == "get":
        url = "https://%s/v2/users/%s?expand=contact" % (module.params['host'], module.params['user'])
        headers_dict = {"Content-Type": "application/json", "Authorization": "GenieKey {}" . format(module.params['apiKey'])}
        headers = json.loads(json.dumps(headers_dict))
        Get(url, headers)

    if module.params['operation'] == "update":
        url = "https://%s/v2/users/%s" % (module.params['host'], module.params['user'])
        headers_dict = {"Content-Type": "application/json", "Authorization": "GenieKey {}" . format(module.params['apiKey'])}
        headers = json.loads(json.dumps(headers_dict))
        data = json.dumps(module.params['user_details'])
        Update(url, headers, data)

    if module.params['operation'] == "delete":
        url = "https://%s/v2/users/%s" % (module.params['host'], module.params['user'])
        headers_dict = {"Content-Type": "application/json", "Authorization": "GenieKey {}" . format(module.params['apiKey'])}
        headers = json.loads(json.dumps(headers_dict))
        Delete(url, headers)

    if module.params['operation'] == "list":
        url = "https://%s/v2/users" % (module.params['host'])
        headers_dict = {"Content-Type": "application/json", "Authorization": "GenieKey {}" . format(module.params['apiKey'])}
        headers = json.loads(json.dumps(headers_dict))
        List(url, headers)

    if module.params['operation'] == "escalations":
        url = "https://%s/v2/users/%s/escalations" % (module.params['host'], module.params['user'])
        headers_dict = {"Content-Type": "application/json", "Authorization": "GenieKey {}" . format(module.params['apiKey'])}
        headers = json.loads(json.dumps(headers_dict))
        Escalations(url, headers)

    if module.params['operation'] == "teams":
        url = "https://%s/v2/users/%s/teams" % (module.params['host'], module.params['user'])
        headers_dict = {"Content-Type": "application/json", "Authorization": "GenieKey {}" . format(module.params['apiKey'])}
        headers = json.loads(json.dumps(headers_dict))
        Teams(url, headers)

    if module.params['operation'] == "forwarding":
        url = "https://%s/v2/users/%s/forwarding-rules" % (module.params['host'], module.params['user'])
        headers_dict = {"Content-Type": "application/json", "Authorization": "GenieKey {}" . format(module.params['apiKey'])}
        headers = json.loads(json.dumps(headers_dict))
        Forwarding(url, headers)

    if module.params['operation'] == "schedules":
        url = "https://%s/v2/users/%s/schedules" % (module.params['host'], module.params['user'])
        headers_dict = {"Content-Type": "application/json", "Authorization": "GenieKey {}" . format(module.params['apiKey'])}
        headers = json.loads(json.dumps(headers_dict))
        Schedules(url, headers)

    if module.params['operation'] == "getsavedsearch":
        url = "https://%s/v2/users/%s/saved-searches/%s" % (module.params['host'], module.params['search_id'])
        headers_dict = {"Content-Type": "application/json", "Authorization": "GenieKey {}" . format(module.params['apiKey'])}
        headers = json.loads(json.dumps(headers_dict))
        GetSavedSearch(url, headers)

    if module.params['operation'] == "listsavedsearch":
        url = "https://%s/v2/users/saved-searches" % (module.params['host'])
        headers_dict = {"Content-Type": "application/json", "Authorization": "GenieKey {}" . format(module.params['apiKey'])}
        headers = json.loads(json.dumps(headers_dict))
        ListSavedSearch(url, headers)

    if module.params['operation'] == "deletesavedsearch":
        url = "https://%s/v1/incidents/saved-searched/%s" % (module.params['host'], module.params['search_id'])
        headers_dict = {"Content-Type": "application/json", "Authorization": "GenieKey {}" . format(module.params['apiKey'])}
        headers = json.loads(json.dumps(headers_dict))
        DeleteSavedSearch(url, headers)

if __name__ == '__main__':
    main()
