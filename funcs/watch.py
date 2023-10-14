def watch():
    import requests
    import inflect
    p = inflect.engine()
    domain = input("type your domain: ")
    url = "https://napi.arvancloud.ir/cdn/4.0/domains/"
    headers = {
        "Authorization": "apikey 899028ad-dc7a-5be2-b434-38b4632c47b9"
    }
    params = {
        "search": " ",
        "per_page": 100,
        "type": "cname,a,aname",
        "page": 1
    }
    url = url + domain + "/dns-records"
    r = requests.get(url, headers=headers, params=params)
    my_json = (r.json())
    count = 1

    for val in my_json["data"]:
        try:
            print(f"{p.ordinal(count)}: ")
            count += 1
            print(f"type: {val['type']}")
            print(f"id: {val['id']}")
            print(f"name: {val['name']}")
            print(f"ip: {val['value'][0]['ip']}")
            print(f"port: {val['value'][0]['port']}")

        except KeyError:
            continue