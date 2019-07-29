#!/usr/bin/python
#
# Ansible Module for OpsGenie Alerts

from ansible.module_utils.basic import *
import requests

def Create(url, headers, data):
    stdout = requests.post(url, headers=headers, data=data)
    if stdout.status_code == 202:
        module.exit_json(changed=True, responce=stdout.json())
    else:
        msg = 'Status code was not 202 :: Responded Status code %s' % stdout.status_code
        module.fail_json(msg=msg, msg1=stdout.status_code)

def Delete(url, headers):
    stdout = requests.delete(url, headers=headers)
    if stdout.status_code == 202:
        module.exit_json(changed=True, responce=stdout.json())
    else:
        msg = 'Status code was not 202 :: Responded Status code %s' % stdout.status_code
        module.fail_json(msg=msg, msg1=stdout.status_code)

def Get(url, headers):
    stdout = requests.get(url, headers=headers)
    if stdout.status_code == 200:
        module.exit_json(changed=False, responce=stdout.json())
    else:
        msg = 'Status code was not 200 :: Responded Status code %s' % stdout.status_code
        module.fail_json(msg=msg, msg1=stdout.status_code)

def List(url, headers):
    stdout = requests.get(url, headers=headers)
    if stdout.status_code == 200:
        module.exit_json(changed=False, responce=stdout.json())
    else:
        msg = 'Status code was not 200 :: Responded Status code %s' % stdout.status_code
        module.fail_json(msg=msg, msg1=stdout.status_code)

def Close(url, headers, data):
    stdout = requests.post(url, headers=headers, data=data)
    if stdout.status_code == 200:
        module.exit_json(changed=False, responce=stdout.json())
    else:
        msg = 'Status code was not 200 :: Responded Status code %s' % stdout.status_code
        module.fail_json(msg=msg, msg1=stdout.status_code)

def Resolve(url, headers, data):
    stdout = requests.post(url, headers=headers, data=data)
    if stdout.status_code == 200:
        module.exit_json(changed=False, responce=stdout.json())
    else:
        msg = 'Status code was not 200 :: Responded Status code %s' % stdout.status_code
        module.fail_json(msg=msg, msg1=stdout.status_code)

def Reopen(url, headers, data):
    stdout = requests.post(url, headers=headers, data=data)
    if stdout.status_code == 200:
        module.exit_json(changed=False, responce=stdout.json())
    else:
        msg = 'Status code was not 200 :: Responded Status code %s' % stdout.status_code
        module.fail_json(msg=msg, msg1=stdout.status_code)

def AddNote(url, headers, data):
    stdout = requests.post(url, headers=headers, data=data)
    if stdout.status_code == 202:
        module.exit_json(changed=True, responce=stdout.json())
    else:
        msg = 'Status code was not 202 :: Responded Status code %s' % stdout.status_code
        module.fail_json(msg=msg, msg1=stdout.status_code)

def AddResponders(url, headers, data):
    stdout = requests.post(url, headers=headers, data=data)
    if stdout.status_code == 202:
        module.exit_json(changed=True, responce=stdout.json())
    else:
        msg = 'Status code was not 202 :: Responded Status code %s' % stdout.status_code
        module.fail_json(msg=msg, msg1=stdout.status_code)

def AddTags(url, headers, data):
    stdout = requests.post(url, headers=headers, data=data)
    if stdout.status_code == 202:
        module.exit_json(changed=True, responce=stdout.json())
    else:
        msg = 'Status code was not 202 :: Responded Status code %s' % stdout.status_code
        module.fail_json(msg=msg, msg1=stdout.status_code)

def RemoveTags(url, headers, data):
    stdout = requests.delete(url, headers=headers, data=data)
    if stdout.status_code == 202:
        module.exit_json(changed=True, responce=stdout.json())
    else:
        msg = 'Status code was not 202 :: Responded Status code %s' % stdout.status_code
        module.fail_json(msg=msg, msg1=stdout.status_code)

def AddDetails(url, headers, data):
    stdout = requests.post(url, headers=headers, data=data)
    if stdout.status_code == 202:
        module.exit_json(changed=True, responce=stdout.json())
    else:
        msg = 'Status code was not 202 :: Responded Status code %s' % stdout.status_code
        module.fail_json(msg=msg, msg1=stdout.status_code)

def RemoveDetails(url, headers, data):
    stdout = requests.delete(url, headers=headers, data=data)
    if stdout.status_code == 202:
        module.exit_json(changed=True, responce=stdout.json())
    else:
        msg = 'Status code was not 202 :: Responded Status code %s' % stdout.status_code
        module.fail_json(msg=msg, msg1=stdout.status_code)

def UpdatePriority(url, headers, data):
    stdout = requests.put(url, headers=headers, data=data)
    if stdout.status_code == 202:
        module.exit_json(changed=True, responce=stdout.json())
    else:
        msg = 'Status code was not 202 :: Responded Status code %s' % stdout.status_code
        module.fail_json(msg=msg, msg1=stdout.status_code)

def UpdateMessage(url, headers, data):
    stdout = requests.put(url, headers=headers, data=data)
    if stdout.status_code == 202:
        module.exit_json(changed=True, responce=stdout.json())
    else:
        msg = 'Status code was not 202 :: Responded Status code %s' % stdout.status_code
        module.fail_json(msg=msg, msg1=stdout.status_code)

def UpdateDescription(url, headers, data):
    stdout = requests.put(url, headers=headers, data=data)
    if stdout.status_code == 202:
        module.exit_json(changed=True, responce=stdout.json())
    else:
        msg = 'Status code was not 202 :: Responded Status code %s' % stdout.status_code
        module.fail_json(msg=msg, msg1=stdout.status_code)

def ListLogs(url, headers):
    stdout = requests.get(url, headers=headers)
    if stdout.status_code == 200:
        module.exit_json(changed=False, responce=stdout.json())
    else:
        msg = 'Status code was not 200 :: Responded Status code %s' % stdout.status_code
        module.fail_json(msg=msg, msg1=stdout.status_code)

def ListNotes(url, headers):
    stdout = requests.get(url, headers=headers)
    if stdout.status_code == 200:
        module.exit_json(changed=False, responce=stdout.json())
    else:
        msg = 'Status code was not 200 :: Responded Status code %s' % stdout.status_code
        module.fail_json(msg=msg, msg1=stdout.status_code)

def main():
    global module
    module = AnsibleModule(
        argument_spec=dict(
            host=dict(required=True, type='str'),
            apiKey=dict(required=True, type='str'),
            status_code=dict(required=False, default=[200, 204], type='list'),
            operation=dict(required=False, default='list', type='str', choice=["list", "create"]),
            incident_details=dict(required=False, type='dict'),
            incident_id=dict(required=False, type='str'),
            search_id=dict(required=False, type='str'),
            incident=dict(required=False, type='str')
            )
    )

    if module.params['operation'] == "create":
        url = "http://%s/v1/incidents/create" % (module.params['host'])
        headers_dict = {"Content-Type": "application/json", "Authorization": "GenieKey {}" . format(module.params['apiKey'])}
        headers = json.loads(json.dumps(headers_dict))
        data = json.dumps(module.params['incident_details'])
        Create(url, headers, data)

    if module.params['operation'] == "delete":
        url = "http://%s/v1/incidents/%s?identifierType=id" % (module.params['host'], module.params['incident_id'])
        headers_dict = {"Authorization": "GenieKey {}" . format(module.params['apiKey'])}
        headers = json.loads(json.dumps(headers_dict))
        Delete(url, headers)

    if module.params['operation'] == "get":
        url = "https://%s/v1/incidents/%s?identifierType=id" % (module.params['host'], module.params['incident_id'])
        headers_dict = {"Authorization": "GenieKey {}" . format(module.params['apiKey'])}
        headers = json.loads(json.dumps(headers_dict))
        Get(url, headers)

    if module.params['operation'] == "list":
        url = "https://%s/v1/incidents" % (module.params['host'])
        headers_dict = {"Authorization": "GenieKey {}" . format(module.params['apiKey'])}
        headers = json.loads(json.dumps(headers_dict))
        List(url, headers)

    if module.params['operation'] == "close":
        url = "https://%s/v1/incidents/%s/close?identifierType=id" % (module.params['host'], module.params['incident_id'])
        headers_dict = {"Authorization": "GenieKey {}" . format(module.params['apiKey'])}
        headers = json.loads(json.dumps(headers_dict))
        data = json.dumps(module.params['incident_details'])
        Close(url, headers, data)

    if module.params['operation'] == "resolve":
        url = "https://%s/v1/incidents/%s/resolve?identifierType=id" % (module.params['host'], module.params['incident_id'])
        headers_dict = {"Authorization": "GenieKey {}" . format(module.params['apiKey'])}
        headers = json.loads(json.dumps(headers_dict))
        data = json.dumps(module.params['incident_details'])
        Resolve(url, headers, data)

    if module.params['operation'] == "reopen":
        url = "https://%s/v1/incidents/%s/reopen?identifierType=id" % (module.params['host'], module.params['incident_id'])
        headers_dict = {"Authorization": "GenieKey {}" . format(module.params['apiKey'])}
        headers = json.loads(json.dumps(headers_dict))
        data = json.dumps(module.params['incident_details'])
        Reopen(url, headers, data)

    if module.params['operation'] == "addnote":
        url = "http://%s/v1/incidents/%s/notes?identifierType=id" % (module.params['host'], module.params['incident_id'])
        headers_dict = {"Content-Type": "application/json", "Authorization": "GenieKey {}" . format(module.params['apiKey'])}
        headers = json.loads(json.dumps(headers_dict))
        data = json.dumps(module.params['incident_details'])
        AddNote(url, headers, data)

    if module.params['operation'] == "addresponders":
        url = "http://%s/v1/incidents/%s/responders?identifierType=id" % (module.params['host'], module.params['incident_id'])
        headers_dict = {"Content-Type": "application/json", "Authorization": "GenieKey {}" . format(module.params['apiKey'])}
        headers = json.loads(json.dumps(headers_dict))
        data = json.dumps(module.params['incident_details'])
        AddResponders(url, headers, data)

    if module.params['operation'] == "addtags":
        url = "http://%s/v1/incidents/%s/tags?identifierType=id" % (module.params['host'], module.params['incident_id'])
        headers_dict = {"Content-Type": "application/json", "Authorization": "GenieKey {}" . format(module.params['apiKey'])}
        headers = json.loads(json.dumps(headers_dict))
        data = json.dumps(module.params['incident_details'])
        AddTags(url, headers, data)

    if module.params['operation'] == "removetags":
        url = "http://%s/v1/incidents/%s/tags?identifierType=id" % (module.params['host'], module.params['incident_id'])
        headers_dict = {"Content-Type": "application/json", "Authorization": "GenieKey {}" . format(module.params['apiKey'])}
        headers = json.loads(json.dumps(headers_dict))
        data = json.dumps(module.params['incident_details'])
        RemoveTags(url, headers, data)

    if module.params['operation'] == "adddetails":
        url = "http://%s/v1/incidents/%s/tags?identifierType=id" % (module.params['host'], module.params['incident_id'])
        headers_dict = {"Content-Type": "application/json", "Authorization": "GenieKey {}" . format(module.params['apiKey'])}
        headers = json.loads(json.dumps(headers_dict))
        data = json.dumps(module.params['incident_details'])
        AddDetails(url, headers, data)

    if module.params['operation'] == "removedetails":
        url = "http://%s/v1/incidents/%s/tags?identifierType=id" % (module.params['host'], module.params['incident_id'])
        headers_dict = {"Content-Type": "application/json", "Authorization": "GenieKey {}" . format(module.params['apiKey'])}
        headers = json.loads(json.dumps(headers_dict))
        data = json.dumps(module.params['incident_details'])
        RemoveDetails(url, headers, data)

    if module.params['operation'] == "updatepriority":
        url = "http://%s/v1/incidents/%s/priority?identifierType=id" % (module.params['host'], module.params['incident_id'])
        headers_dict = {"Content-Type": "application/json", "Authorization": "GenieKey {}" . format(module.params['apiKey'])}
        headers = json.loads(json.dumps(headers_dict))
        data = json.dumps(module.params['incident_details'])
        UpdatePriority(url, headers, data)

    if module.params['operation'] == "updatemessage":
        url = "http://%s/v1/incidents/%s/message?identifierType=id" % (module.params['host'], module.params['incident_id'])
        headers_dict = {"Content-Type": "application/json", "Authorization": "GenieKey {}" . format(module.params['apiKey'])}
        headers = json.loads(json.dumps(headers_dict))
        data = json.dumps(module.params['incident_details'])
        UpdateMessage(url, headers, data)

    if module.params['operation'] == "updatedescription":
        url = "http://%s/v1/incidents/%s/description?identifierType=id" % (module.params['host'], module.params['incident_id'])
        headers_dict = {"Content-Type": "application/json", "Authorization": "GenieKey {}" . format(module.params['apiKey'])}
        headers = json.loads(json.dumps(headers_dict))
        data = json.dumps(module.params['incident_details'])
        UpdateDescription(url, headers, data)

    if module.params['operation'] == "listlogs":
        url = "http://%s/v1/incidents/%s/logs?identifierType=id" % (module.params['host'], module.params['incident_id'])
        headers_dict = {"Authorization": "GenieKey {}" . format(module.params['apiKey'])}
        headers = json.loads(json.dumps(headers_dict))
        ListLogs(url, headers)

    if module.params['operation'] == "listnotes":
        url = "http://%s/v1/incidents/%s/notes?identifierType=id" % (module.params['host'], module.params['incident_id'])
        headers_dict = {"Authorization": "GenieKey {}" . format(module.params['apiKey'])}
        headers = json.loads(json.dumps(headers_dict))
        ListNotes(url, headers)

if __name__ == '__main__':
    main()
