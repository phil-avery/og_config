#!/usr/bin/python
#
# Ansible Module for OpsGenie Alerts

from ansible.module_utils.basic import *
import requests

def Create(url, headers, data):
    ogapi = requests.post(url, headers=headers, data=data)
    if ogapi.status_code == 202:
        module.exit_json(changed=True, responce=ogapi.json())
    else:
        msg = 'Status code was not 202 :: Responded Status code %s' % ogapi.status_code
        module.fail_json(msg=msg, status_code=ogapi.status_code)

def Delete(url, headers):
    ogapi = requests.delete(url, headers=headers)
    if ogapi.status_code == 202:
        module.exit_json(changed=True, responce=ogapi.json())
    else:
        msg = 'Status code was not 202 :: Responded Status code %s' % ogapi.status_code
        module.fail_json(msg=msg, status_code=ogapi.status_code)

def Get(url, headers):
    ogapi = requests.get(url, headers=headers)
    if ogapi.status_code == 200:
        module.exit_json(changed=False, responce=ogapi.json())
    else:
        msg = 'Status code was not 200 :: Responded Status code %s' % ogapi.status_code
        module.fail_json(msg=msg, status_code=ogapi.status_code)

def List(url, headers):
    ogapi = requests.get(url, headers=headers)
    if ogapi.status_code == 200:
        module.exit_json(changed=False, responce=ogapi.json())
    else:
        msg = 'Status code was not 200 :: Responded Status code %s' % ogapi.status_code
        module.fail_json(msg=msg, status_code=ogapi.status_code)

def Count(url, headers):
    ogapi = requests.get(url, headers=headers)
    if ogapi.status_code == 200:
        module.exit_json(changed=False, responce=ogapi.json())
    else:
        msg = 'Status code was not 200 :: Responded Status code %s' % ogapi.status_code
        module.fail_json(msg=msg, status_code=ogapi.status_code)

def Acknowledge(url, headers, data):
    ogapi = requests.post(url, headers=headers, data=data)
    if ogapi.status_code == 202:
        module.exit_json(changed=True, responce=ogapi.json())
    else:
        msg = 'Status code was not 202 :: Responded Status code %s' % ogapi.status_code
        module.fail_json(msg=msg, status_code=ogapi.status_code)

def Close(url, headers, data):
    ogapi = requests.post(url, headers=headers, data=data)
    if ogapi.status_code == 202:
        module.exit_json(changed=True, responce=ogapi.json())
    else:
        msg = 'Status code was not 202 :: Responded Status code %s' % ogapi.status_code
        module.fail_json(msg=msg, status_code=ogapi.status_code)

def AddNote(url, headers, data):
    ogapi = requests.post(url, headers=headers, data=data)
    if ogapi.status_code == 202:
        module.exit_json(changed=True, responce=ogapi.json())
    else:
        msg = 'Status code was not 202 :: Responded Status code %s' % ogapi.status_code
        module.fail_json(msg=msg, status_code=ogapi.status_code)

def Unacknowledge(url, headers, data):
    ogapi = requests.post(url, headers=headers, data=data)
    if ogapi.status_code == 202:
        module.exit_json(changed=True, responce=ogapi.json())
    else:
        msg = 'Status code was not 202 :: Responded Status code %s' % ogapi.status_code
        module.fail_json(msg=msg, status_code=ogapi.status_code)

def Snooze(url, headers, data):
    ogapi = requests.post(url, headers=headers, data=data)
    if ogapi.status_code == 202:
        module.exit_json(changed=True, responce=ogapi.json())
    else:
        msg = 'Status code was not 202 :: Responded Status code %s' % ogapi.status_code
        module.fail_json(msg=msg, status_code=ogapi.status_code)

def Escalate(url, headers, data):
    ogapi = requests.post(url, headers=headers, data=data)
    if ogapi.status_code == 202:
        module.exit_json(changed=True, responce=ogapi.json())
    else:
        msg = 'Status code was not 202 :: Responded Status code %s' % ogapi.status_code
        module.fail_json(msg=msg, status_code=ogapi.status_code)

def Assign(url, headers, data):
    ogapi = requests.post(url, headers=headers, data=data)
    if ogapi.status_code == 202:
        module.exit_json(changed=True, responce=ogapi.json())
    else:
        msg = 'Status code was not 202 :: Responded Status code %s' % ogapi.status_code
        module.fail_json(msg=msg, status_code=ogapi.status_code)

def AddTeam(url, headers, data):
    ogapi = requests.post(url, headers=headers, data=data)
    if ogapi.status_code == 202:
        module.exit_json(changed=True, responce=ogapi.json())
    else:
        msg = 'Status code was not 202 :: Responded Status code %s' % ogapi.status_code
        module.fail_json(msg=msg, status_code=ogapi.status_code)

def AddResponders(url, headers, data):
    ogapi = requests.post(url, headers=headers, data=data)
    if ogapi.status_code == 202:
        module.exit_json(changed=True, responce=ogapi.json())
    else:
        msg = 'Status code was not 202 :: Responded Status code %s' % ogapi.status_code
        module.fail_json(msg=msg, status_code=ogapi.status_code)

def AddTags(url, headers, data):
    ogapi = requests.post(url, headers=headers, data=data)
    if ogapi.status_code == 202:
        module.exit_json(changed=True, responce=ogapi.json())
    else:
        msg = 'Status code was not 202 :: Responded Status code %s' % ogapi.status_code
        module.fail_json(msg=msg, status_code=ogapi.status_code)

def RemoveTags(url, headers, data):
    ogapi = requests.delete(url, headers=headers, data=data)
    if ogapi.status_code == 202:
        module.exit_json(changed=True, responce=ogapi.json())
    else:
        msg = 'Status code was not 202 :: Responded Status code %s' % ogapi.status_code
        module.fail_json(msg=msg, status_code=ogapi.status_code)

def AddDetails(url, headers, data):
    ogapi = requests.post(url, headers=headers, data=data)
    if ogapi.status_code == 202:
        module.exit_json(changed=True, responce=ogapi.json())
    else:
        msg = 'Status code was not 202 :: Responded Status code %s' % ogapi.status_code
        module.fail_json(msg=msg, status_code=ogapi.status_code)

def UpdatePriority(url, headers, data):
    ogapi = requests.put(url, headers=headers, data=data)
    if ogapi.status_code == 202:
        module.exit_json(changed=True, responce=ogapi.json())
    else:
        msg = 'Status code was not 202 :: Responded Status code %s' % ogapi.status_code
        module.fail_json(msg=msg, status_code=ogapi.status_code)

def UpdateMessage(url, headers, data):
    ogapi = requests.put(url, headers=headers, data=data)
    if ogapi.status_code == 202:
        module.exit_json(changed=True, responce=ogapi.json())
    else:
        msg = 'Status code was not 202 :: Responded Status code %s' % ogapi.status_code
        module.fail_json(msg=msg, status_code=ogapi.status_code)

def UpdateDescription(url, headers, data):
    ogapi = requests.put(url, headers=headers, data=data)
    if ogapi.status_code == 202:
        module.exit_json(changed=True, responce=ogapi.json())
    else:
        msg = 'Status code was not 202 :: Responded Status code %s' % ogapi.status_code
        module.fail_json(msg=msg, status_code=ogapi.status_code)

def ListRecipients(url, headers):
    ogapi = requests.get(url, headers=headers)
    if ogapi.status_code == 200:
        module.exit_json(changed=False, responce=ogapi.json())
    else:
        msg = 'Status code was not 200 :: Responded Status code %s' % ogapi.status_code
        module.fail_json(msg=msg, status_code=ogapi.status_code)

def ListLogs(url, headers):
    ogapi = requests.get(url, headers=headers)
    if ogapi.status_code == 200:
        module.exit_json(changed=False, responce=ogapi.json())
    else:
        msg = 'Status code was not 200 :: Responded Status code %s' % ogapi.status_code
        module.fail_json(msg=msg, status_code=ogapi.status_code)

def ListNotes(url, headers):
    ogapi = requests.get(url, headers=headers)
    if ogapi.status_code == 200:
        module.exit_json(changed=False, responce=ogapi.json())
    else:
        msg = 'Status code was not 200 :: Responded Status code %s' % ogapi.status_code
        module.fail_json(msg=msg, status_code=ogapi.status_code)

def CreateSavedSearch(url, headers, data):
    ogapi = requests.post(url, headers=headers, data=data)
    if ogapi.status_code == 201:
        module.exit_json(changed=True, responce=ogapi.json())
    elif ogapi.status_code == 409:
        module.exit_json(changed=False, msg='Saved Search already exists!')
    else:
        msg = 'Status code was not 201 or 409 :: Responded Status code %s' % ogapi.status_code
        module.fail_json(msg=msg, status_code=ogapi.status_code)

def UpdateSavedSearch(url, headers, data):
    ogapi = requests.patch(url, headers=headers, data=data)
    if ogapi.status_code == 200:
        module.exit_json(changed=True, responce=ogapi.json())
    elif ogapi.status_code == 409:
        module.exit_json(changed=False)
    else:
        msg = 'Status code was not 201 or 409 :: Responded Status code %s' % ogapi.status_code
        module.fail_json(msg=msg, status_code=ogapi.status_code)

def GetSavedSearch(url, headers):
    ogapi = requests.get(url, headers=headers)
    if ogapi.status_code == 200:
        module.exit_json(changed=True, responce=ogapi.json())
    else:
        msg = 'Status code was not 201 or 409 :: Responded Status code %s' % ogapi.status_code
        module.fail_json(msg=msg, status_code=ogapi.status_code)

def DeleteSavedSearch(url, headers):
    ogapi = requests.delete(url, headers=headers)
    if ogapi.status_code == 200:
        module.exit_json(changed=True, responce=ogapi.json())
    elif ogapi.status_code == 404:
        module.exit_json(changed=False, msg='Saved Search ID does not exist')
    else:
        msg = 'Status code was not 201 or 404 :: Responded Status code %s' % ogapi.status_code
        module.fail_json(msg=msg, status_code=ogapi.status_code)

def ListSavedSearch(url, headers):
    ogapi = requests.get(url, headers=headers)
    if ogapi.status_code == 200:
        module.exit_json(changed=True, responce=ogapi.json())
    else:
        msg = 'Status code was not 201 or 409 :: Responded Status code %s' % ogapi.status_code
        module.fail_json(msg=msg, status_code=ogapi.status_code)

def CreateAlertAttachment(url, headers, files):
    ogapi = requests.post(url, headers=headers, files=files)
    if ogapi.status_code != 201:
        module.exit_json(changed=False, responce=ogapi.status_code)
    else:
        module.exit_json(changed=False, msg='Saved Search already exists!')

def main():
    global module
    module = AnsibleModule(
        argument_spec=dict(
            host=dict(required=True, type='str'),
            apiKey=dict(required=True, type='str'),
            status_code=dict(required=False, default=[200, 204], type='list'),
            operation=dict(required=False, default='list', type='str', choice=["list", "create"]),
            alert_details=dict(required=False, type='dict'),
            alert_id=dict(required=False, type='str'),
            search_id=dict(required=False, type='str'),
            file=dict(required=False, type='str'),
            username=dict(required=False, type='str')
            )
    )

    if module.params['operation'] == "create":
        url = "http://%s/v2/alerts" % (module.params['host'])
        headers_dict = {"Content-Type": "application/json", "Authorization": "GenieKey {}" . format(module.params['apiKey'])}
        headers = json.loads(json.dumps(headers_dict))
        data = json.dumps(module.params['alert_details'])
        Create(url, headers, data)

    if module.params['operation'] == "delete":
        url = "http://%s/v2/alerts/%s?identifierType=id" % (module.params['host'], module.params['alert_id'])
        headers_dict = {"Authorization": "GenieKey {}" . format(module.params['apiKey'])}
        headers = json.loads(json.dumps(headers_dict))
        Delete(url, headers)

    if module.params['operation'] == "get":
        url = "https://%s/v2/alerts/%s?identifierType=id" % (module.params['host'], module.params['alert_id'])
        headers_dict = {"Authorization": "GenieKey {}" . format(module.params['apiKey'])}
        headers = json.loads(json.dumps(headers_dict))
        Get(url, headers)

    if module.params['operation'] == "list":
        url = "https://%s/v2/alerts" % (module.params['host'])
        headers_dict = {"Authorization": "GenieKey {}" . format(module.params['apiKey'])}
        headers = json.loads(json.dumps(headers_dict))
        List(url, headers)

    if module.params['operation'] == "count":
        url = "https://%s/v2/alerts/count" % (module.params['host'])
        headers_dict = {"Authorization": "GenieKey {}" . format(module.params['apiKey'])}
        headers = json.loads(json.dumps(headers_dict))
        Count(url, headers)

    if module.params['operation'] == "acknowledge":
        url = "http://%s/v2/alerts/%s/acknowledge?identifierType=id" % (module.params['host'], module.params['alert_id'])
        headers_dict = {"Content-Type": "application/json", "Authorization": "GenieKey {}" . format(module.params['apiKey'])}
        headers = json.loads(json.dumps(headers_dict))
        data = json.dumps(module.params['alert_details'])
        Acknowledge(url, headers, data)

    if module.params['operation'] == "close":
        url = "http://%s/v2/alerts/%s/close?identifierType=id" % (module.params['host'], module.params['alert_id'])
        headers_dict = {"Content-Type": "application/json", "Authorization": "GenieKey {}" . format(module.params['apiKey'])}
        headers = json.loads(json.dumps(headers_dict))
        data = json.dumps(module.params['alert_details'])
        Close(url, headers, data)

    if module.params['operation'] == "addnote":
        url = "http://%s/v2/alerts/%s/notes?identifierType=id" % (module.params['host'], module.params['alert_id'])
        headers_dict = {"Content-Type": "application/json", "Authorization": "GenieKey {}" . format(module.params['apiKey'])}
        headers = json.loads(json.dumps(headers_dict))
        data = json.dumps(module.params['alert_details'])
        AddNote(url, headers, data)

    if module.params['operation'] == "unacknowledge":
        url = "http://%s/v2/alerts/%s/unacknowledge?identifierType=id" % (module.params['host'], module.params['alert_id'])
        headers_dict = {"Content-Type": "application/json", "Authorization": "GenieKey {}" . format(module.params['apiKey'])}
        headers = json.loads(json.dumps(headers_dict))
        data = json.dumps(module.params['alert_details'])
        Unacknowledge(url, headers, data)

    if module.params['operation'] == "snooze":
        url = "http://%s/v2/alerts/%s/snooze?identifierType=id" % (module.params['host'], module.params['alert_id'])
        headers_dict = {"Content-Type": "application/json", "Authorization": "GenieKey {}" . format(module.params['apiKey'])}
        headers = json.loads(json.dumps(headers_dict))
        data = json.dumps(module.params['alert_details'])
        Snooze(url, headers, data)

    if module.params['operation'] == "escalate":
        url = "http://%s/v2/alerts/%s/escalate?identifierType=id" % (module.params['host'], module.params['alert_id'])
        headers_dict = {"Content-Type": "application/json", "Authorization": "GenieKey {}" . format(module.params['apiKey'])}
        headers = json.loads(json.dumps(headers_dict))
        data = json.dumps(module.params['alert_details'])
        Escalate(url, headers, data)

    if module.params['operation'] == "assign":
        url = "http://%s/v2/alerts/%s/assign?identifierType=id" % (module.params['host'], module.params['alert_id'])
        headers_dict = {"Content-Type": "application/json", "Authorization": "GenieKey {}" . format(module.params['apiKey'])}
        headers = json.loads(json.dumps(headers_dict))
        data = json.dumps(module.params['alert_details'])
        Assign(url, headers, data)

    if module.params['operation'] == "addteam":
        url = "http://%s/v2/alerts/%s/team?identifierType=id" % (module.params['host'], module.params['alert_id'])
        headers_dict = {"Content-Type": "application/json", "Authorization": "GenieKey {}" . format(module.params['apiKey'])}
        headers = json.loads(json.dumps(headers_dict))
        data = json.dumps(module.params['alert_details'])
        AddTeam(url, headers, data)

    if module.params['operation'] == "addresponders":
        url = "http://%s/v2/alerts/%s/responders?identifierType=id" % (module.params['host'], module.params['alert_id'])
        headers_dict = {"Content-Type": "application/json", "Authorization": "GenieKey {}" . format(module.params['apiKey'])}
        headers = json.loads(json.dumps(headers_dict))
        data = json.dumps(module.params['alert_details'])
        AddResponders(url, headers, data)

    if module.params['operation'] == "addtags":
        url = "http://%s/v2/alerts/%s/tags?identifierType=id" % (module.params['host'], module.params['alert_id'])
        headers_dict = {"Content-Type": "application/json", "Authorization": "GenieKey {}" . format(module.params['apiKey'])}
        headers = json.loads(json.dumps(headers_dict))
        data = json.dumps(module.params['alert_details'])
        AddTags(url, headers, data)

    if module.params['operation'] == "removetags":
        url = "http://%s/v2/alerts/%s/tags?identifierType=id" % (module.params['host'], module.params['alert_id'])
        headers_dict = {"Content-Type": "application/json", "Authorization": "GenieKey {}" . format(module.params['apiKey'])}
        headers = json.loads(json.dumps(headers_dict))
        data = json.dumps(module.params['alert_details'])
        RemoveTags(url, headers, data)

    if module.params['operation'] == "adddetails":
        url = "http://%s/v2/alerts/%s/details?identifierType=id" % (module.params['host'], module.params['alert_id'])
        headers_dict = {"Content-Type": "application/json", "Authorization": "GenieKey {}" . format(module.params['apiKey'])}
        headers = json.loads(json.dumps(headers_dict))
        data = json.dumps(module.params['alert_details'])
        AddDetails(url, headers, data)

    if module.params['operation'] == "updatepriority":
        url = "http://%s/v2/alerts/%s/priority?identifierType=id" % (module.params['host'], module.params['alert_id'])
        headers_dict = {"Content-Type": "application/json", "Authorization": "GenieKey {}" . format(module.params['apiKey'])}
        headers = json.loads(json.dumps(headers_dict))
        data = json.dumps(module.params['alert_details'])
        UpdatePriority(url, headers, data)

    if module.params['operation'] == "updatemessage":
        url = "http://%s/v2/alerts/%s/message?identifierType=id" % (module.params['host'], module.params['alert_id'])
        headers_dict = {"Content-Type": "application/json", "Authorization": "GenieKey {}" . format(module.params['apiKey'])}
        headers = json.loads(json.dumps(headers_dict))
        data = json.dumps(module.params['alert_details'])
        UpdateMessage(url, headers, data)

    if module.params['operation'] == "updatedescription":
        url = "http://%s/v2/alerts/%s/description?identifierType=id" % (module.params['host'], module.params['alert_id'])
        headers_dict = {"Content-Type": "application/json", "Authorization": "GenieKey {}" . format(module.params['apiKey'])}
        headers = json.loads(json.dumps(headers_dict))
        data = json.dumps(module.params['alert_details'])
        UpdateDescription(url, headers, data)

    if module.params['operation'] == "listrecipients":
        url = "http://%s/v2/alerts/%s/recipients?identifierType=id" % (module.params['host'], module.params['alert_id'])
        headers_dict = {"Authorization": "GenieKey {}" . format(module.params['apiKey'])}
        headers = json.loads(json.dumps(headers_dict))
        ListRecipients(url, headers)

    if module.params['operation'] == "listlogs":
        url = "http://%s/v2/alerts/%s/logs?identifierType=id" % (module.params['host'], module.params['alert_id'])
        headers_dict = {"Authorization": "GenieKey {}" . format(module.params['apiKey'])}
        headers = json.loads(json.dumps(headers_dict))
        ListLogs(url, headers)

    if module.params['operation'] == "listnotes":
        url = "http://%s/v2/alerts/%s/notes?identifierType=id" % (module.params['host'], module.params['alert_id'])
        headers_dict = {"Authorization": "GenieKey {}" . format(module.params['apiKey'])}
        headers = json.loads(json.dumps(headers_dict))
        ListNotes(url, headers)

    if module.params['operation'] == "createsavedsearch":
        url = "http://%s/v2/alerts/saved-searches" % (module.params['host'])
        headers_dict = {"Content-Type": "application/json", "Authorization": "GenieKey {}" . format(module.params['apiKey'])}
        headers = json.loads(json.dumps(headers_dict))
        data = json.dumps(module.params['alert_details'])
        CreateSavedSearch(url, headers, data)

    if module.params['operation'] == "updatesavedsearch":
        url = "http://%s/v2/alerts/saved-searches/%s" % (module.params['host'], module.params['search_id'])
        headers_dict = {"Content-Type": "application/json", "Authorization": "GenieKey {}" . format(module.params['apiKey'])}
        headers = json.loads(json.dumps(headers_dict))
        data = json.dumps(module.params['alert_details'])
        UpdateSavedSearch(url, headers, data)

    if module.params['operation'] == "getsavedsearch":
        url = "http://%s/v2/alerts/saved-searches/%s" % (module.params['host'], module.params['search_id'])
        headers_dict = {"Authorization": "GenieKey {}" . format(module.params['apiKey'])}
        headers = json.loads(json.dumps(headers_dict))
        GetSavedSearch(url, headers)

    if module.params['operation'] == "deletesavedsearch":
        url = "http://%s/v2/alerts/saved-searches/%s" % (module.params['host'], module.params['search_id'])
        headers_dict = {"Authorization": "GenieKey {}" . format(module.params['apiKey'])}
        headers = json.loads(json.dumps(headers_dict))
        DeleteSavedSearch(url, headers)

    if module.params['operation'] == "listsavedsearch":
        url = "http://%s/v2/alerts/saved-searches" % (module.params['host'])
        headers_dict = {"Authorization": "GenieKey {}" . format(module.params['apiKey'])}
        headers = json.loads(json.dumps(headers_dict))
        ListSavedSearch(url, headers)

    if module.params['operation'] == "createalertattachment":
        url = "http://%s/v2/alerts/%s/attachments?identifierType=id" % (module.params['host'], module.params['alert_id'])
        headers_dict = {"Content-Type": "multipart/form-data", "Authorization": "GenieKey {}" . format(module.params['apiKey'])}
        headers = json.loads(json.dumps(headers_dict))
        files_dict = {"file": "@test.zip"}
        files = json.loads(json.dumps(files_dict))
        UpdateSavedSearch(url, headers, files)


if __name__ == '__main__':
    main()
