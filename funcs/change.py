def change():
    import requests
    import inflect
    p = inflect.engine()
    domain = input("type your domain: ")
    dest_ip = input("type your destination ip please: ")
    dest_domain = input("type your destination domain please: ")
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
            if val["type"] == "a":
                a_obj = {
                    "value": [{
                        "ip": dest_ip,
                        "port": val['value'][0]['port'],
                        "weight": val['value'][0]['weight'],
                        "country": val['value'][0]['country']
                    }],
                    "type": val['type'],
                    "name": val['name'],
                    "ttl": val['ttl'],
                    "cloud": val['cloud'],
                    "upstream_https": val['upstream_https'],
                    "ip_filter_mode": val['ip_filter_mode']
                }
                post_url = url + "/" + val['id']
                post_req = requests.put(post_url, json=a_obj, headers=headers)
                print(post_req.text)
            elif val["type"] == "cname":
                cname_obj = {
                    "value": {
                        "host": dest_domain,
                        "host_header": val["value"]["host_header"],
                        "port": val["value"]["port"]
                    },
                    "type": val['type'],
                    "name": val['name'],
                    "ttl": val['ttl'],
                    "cloud": val['cloud'],
                    "upstream_https": val['upstream_https'],
                    "ip_filter_mode": val['ip_filter_mode']
                }
                post_url = url + "/" + val['id']
                post_req = requests.put(post_url, json=cname_obj, headers=headers)
                print(post_req.text)
            elif val["type"] == "aname":
                aname_obj = {
                    "value": {
                        "location": dest_domain,
                        "host_header": val["value"]["host_header"],
                        "port": val["value"]["port"]
                    },
                    "type": val['type'],
                    "name": val['name'],
                    "ttl": val['ttl'],
                    "cloud": val['cloud'],
                    "upstream_https": val['upstream_https'],
                    "ip_filter_mode": val['ip_filter_mode']
                }
                post_url = url + "/" + val['id']
                post_req = requests.put(post_url, json=aname_obj, headers=headers)
                print(post_req.text)
            else:
                print("there is sth wrong")
        except KeyError:
            pass
