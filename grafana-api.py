import requests, json, os

headers = {
    "Accept" : "application/json",
    "Content-Type" : "application/json",
    "Authorization" : "Bearer eyJrIjoiUHpzMHZUQTNHeDZrNHdaeGlLWUFlRUU0bzNISUxZa0wiLCJuIjoiU3JlZXRhbSIsImlkIjoxfQ=="
#     eyJrIjoiQ0tnd1ZheWdmdHNkenBQZ3dsNTZmVTN3eE9kUUhuRm4iLCJuIjoiU2Vjb25kT25lIiwiaWQiOjF9
}

paths = {
    "auth_keys": "/api/auth/keys",
    "admin_settings": "/api/admin/settings",
    "get_dashboard": "/api/dashboards/db/apache_db",
    "actual_user": "/api/user",
    "grafana_stats": "/api/admin/stats",
    "create_user": "/api/admin/users",
    "list_dashboards": "/api/search?query=",
    "export_dashboards": "export_dash",
    "import_dashboard": "import_dash"
}

# when adding a new user
payload = {
    "name": "NewUser",
    "email": "new@user.com",
    "login": "user",
    "password": "asdasdasd@123"
}

"""         functions follow          """


def grafana_api(perform, user):
    if chosen == "export_dash":
        return export_dash()sre
        r = requests.get("http://" + (user + "@" if login  else "") + "localhost:3000" + perform, headers=headers,
             data=json.dumps(payload))
        print r.url
        # print r.content
        parsed = json.loads(r.text)
        pretty = json.dumps(parsed, indent=4)
        return pretty

def export_dash():
    r = requests.get("http://" + (user + "@" if login  else "") + "localhost:3000/api/search?query=", headers=headers)
    print r.url
    # print r.content
    parsed = json.loads(r.text)
    urls = []
    for i in xrange(len(parsed)):
        urls.append(parsed[i]["uri"])
    for url in urls:
        r = requests.get("http://localhost:3000/api/dashboards/" + url, headers=headers)
        parsed = json.loads(r.text)
        dir_name = os.path.dirname(url + ".json")
        print dir_name
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)
        with open(url + ".json", 'w') as output:
            json.dump(parsed, output, indent=4)
        print "Exporting DB: ", url.split("/")[1]
    print "Successfully exported to db/"
    return ""


def import_dash(json_data):
    if not os.path.isfile(json_data):
        json_data = str(raw_input("Wrong path. Enter path again: "))
    with open(json_data, 'r+') as incoming:
        in_data = json.load(incoming)
        in_data["overwrite"] = True # true: overwrite if db exists, with newer version or with same title; false: DONT.
        pretty = json.dumps(in_data, indent=4)
        r = requests.post("http://localhost:3000/api/dashboards/db", headers=headers, data=pretty)
        return r.text


chosen = paths["import_dashboard"]

login = False
# login = True

credentials = {
    "admin": "admin:admin",
    "me": "sreetamdas:asdasdasd"
}

user = credentials["admin"]

print grafana_api(chosen, user)


