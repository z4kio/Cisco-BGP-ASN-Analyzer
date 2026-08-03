# Cisco BGP Received Routes ASN Analyzer

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Platform](https://img.shields.io/badge/Platform-Cisco-orange)
![License](https://img.shields.io/badge/License-MIT-green)

A lightweight Python utility that parses Cisco BGP received routes, counts the number of prefixes received from each Autonomous System (ASN), retrieves the ASN holder name from the RIPEstat API, and exports the results to a CSV file.

This tool is particularly useful for ISPs, network engineers, and peering coordinators who need to analyze upstream or peer routing information.

---

## Features

- Parses Cisco BGP received routes
- Counts unique origin ASNs
- Counts prefixes received from each ASN
- Retrieves ASN holder names using the RIPEstat API
- Exports results to CSV
- Caches API lookups to reduce duplicate requests
- Simple, lightweight, and easy to use

---

## Requirements

- Python 3.9+
- pandas
- requests

```bash
pip install pandas requests
```

## Supported Cisco Commands

### IPv4

```cisco
show ip bgp neighbors <NEIGHBOR-IP> routes
show ip bgp neighbors 203.76.110.1 routes | redirect flash:203.76.110.1-routes.txt
```

### VPNv4

```cisco
show ip bgp vpnv4 vrf <VRF_NAME> neighbors <NEIGHBOR-IP> routes
```

## Usage

1. Export the BGP received routes from your Cisco router.
2. Copy the output to `bgp_neighbor_routes.txt`.
3. Place the text file in the same directory as `asn_lookup_ripestat.py`.
4. Run:

```bash
python asn_lookup_ripestat.py
```

## Output

The script generates:

- `asn_prefix_count_with_names.csv`

Columns:

- ASN
- AS_Name
- Prefix_Count

## RIPEstat API

https://stat.ripe.net/docs/data-api/ripestat-data-api

## Roadmap

- IPv6 support
- CLI arguments
- Excel export
- JSON export
- Progress bar
- Multi-threaded lookups

## License

MIT License
