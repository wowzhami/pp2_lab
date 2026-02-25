import json 
with open("sample-data.json") as f:
    data = json.load(f)
print("Interface Status")
print("=" * 80)
print(f"{'DN':50} {'Description':12} {'Speed':8} {'MTU':5}")
print("-" * 80)
for i in data["imdata"]:
    a = i["l1PhysIf"]["attributes"] 
    dn = a["dn"]
    de = a["descr"]
    s = a["speed"]
    mtu = a["mtu"] 
    print(f"{dn:50} {de:12} {s:8} {mtu:5}")