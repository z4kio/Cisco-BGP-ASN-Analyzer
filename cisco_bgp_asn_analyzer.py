import re
import time
import requests
import pandas as pd
from collections import Counter

INPUT_FILE = "bgp_neighbor_routes.txt"
OUTPUT_FILE = "asn_prefix_count_with_names.csv"

# Regex to extract the AS_PATH
pattern = re.compile(r'^\*?>?\s+\S+\s+\S+.*?\s0\s+((?:\d+\s*)+)')

counter = Counter()

print("Reading BGP Routes file...")

with open(INPUT_FILE, "r", encoding="utf-8", errors="ignore") as f:
    for line in f:
        m = pattern.match(line)
        if not m:
            continue

        as_path = m.group(1).strip().split()

        if as_path:
            first_asn = int(as_path[0])
            counter[first_asn] += 1

print(f"Found {len(counter)} unique ASNs.")

cache = {}

def lookup_asn(asn):
    if asn in cache:
        return cache[asn]

    try:
        url = f"https://stat.ripe.net/data/as-overview/data.json?resource=AS{asn}"
        r = requests.get(url, timeout=10)
        r.raise_for_status()

        holder = r.json()["data"].get("holder", "Unknown")

    except Exception:
        holder = "Lookup Failed"

    cache[asn] = holder
    time.sleep(0.05)
    return holder

rows = []

print("Looking up AS names...")

for asn, count in counter.most_common():
    rows.append({
        "ASN": asn,
        "AS_Name": lookup_asn(asn),
        "Prefix_Count": count
    })

df = pd.DataFrame(rows)

df.to_csv(OUTPUT_FILE, index=False)

print(f"\nDone! Output written to {OUTPUT_FILE}")