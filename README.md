# AsusLeak

A proof-of-concept security research tool demonstrating an information disclosure vulnerability in ASUS routers running vulnerable firmware versions.

[![CVE-2018-18287](https://img.shields.io/badge/CVE-2018--18287-red.svg)](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-18287)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

## Overview

AsusLeak is a proof-of-concept demonstrating CVE-2018-18287, an information disclosure vulnerability affecting certain ASUS router models. This vulnerability allows unauthenticated attackers to extract sensitive network information from vulnerable routers without authentication.

## Vulnerability Details

**CVE-2018-18287** is an information disclosure vulnerability that affects ASUS routers running specific firmware versions. The vulnerability exists in the router's web interface and allows unauthorized access to sensitive network data.

### Technical Description

The vulnerability is present in the main login page (`Main_Login.asp`) and additional pages of the router's web interface. These pages inadvertently expose:

- **DHCP Lease Information**: Complete list of devices connected to the network, including IP addresses and hostnames
- **Network Time Information**: Current time, date, and system uptime statistics
- **Network Topology**: Details about active network clients

This information is accessible **without authentication**, allowing any user with network access to the router's web interface to extract sensitive data about the network and connected devices.

### Impact

The vulnerability enables attackers to:
- Map the internal network structure
- Identify connected devices by hostname
- Determine the router's uptime and infer reboot patterns
- Potentially use time information for geolocation inference
- Gather reconnaissance data for further attacks

### MITRE CVE Reference

For official vulnerability details, see: [CVE-2018-18287 on MITRE](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-18287)

## Affected Devices

### Confirmed Vulnerable Configuration

- **Router Model**: ASUS RT-AC58U
- **Vendor**: ASUS
- **Vulnerable Firmware Version**: 3.0.0.4.380_6516

**Note**: Other ASUS router models and firmware versions may also be affected. Users should verify their specific model and firmware version against vendor security advisories.

## Installation

### Prerequisites

- Python 3.x
- Required Python packages:
  - `requests`
  - `argparse` (included in Python standard library)
  - `re` (included in Python standard library)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/syrex1013/AsusLeak.git
cd AsusLeak
```

2. Install dependencies:
```bash
pip install requests
```

## Usage

### Basic Usage

Run the script by specifying the target router's IP address:

```bash
python AsusLeak.py -ip 192.168.1.1
```

### Example Output

```
192.168.1.100 DESKTOP-PC01
192.168.1.101 LAPTOP-USER
192.168.1.102 SMARTPHONE-DEVICE
Time data:
Sun, 14 Oct 2018 12:44:06 +0200(317023 secs since boot)
```

### Command-Line Arguments

- `-ip`: Target router IP address (required)
  - Default router IP is typically `192.168.1.1` or `192.168.50.1`

## How It Works

The tool exploits the information disclosure vulnerability through the following mechanism:

1. **DHCP Leak Extraction**: 
   - Sends an HTTP GET request to `http://[router-ip]/Main_Login.asp`
   - Parses the JavaScript variable `dhcpLeaseInfo` from the response
   - Extracts and formats the list of connected devices with their IP addresses and hostnames

2. **Time Information Extraction**:
   - Sends an HTTP GET request to `http://[router-ip]/update_clients.asp`
   - Extracts the `current_time` value from the response
   - Displays the router's current time, date, and uptime information

Both requests are made **without any authentication**, demonstrating the severity of the vulnerability.

## Security Disclaimer

⚠️ **IMPORTANT**: This tool is provided for educational and security research purposes only.

- **Authorized Testing Only**: Use this tool only on networks and devices you own or have explicit written permission to test
- **Legal Compliance**: Unauthorized access to computer systems is illegal in many jurisdictions
- **Responsible Disclosure**: Report vulnerabilities through proper channels following responsible disclosure guidelines
- **No Warranty**: This software is provided "as-is" without any warranty

The authors and contributors are not responsible for misuse or damage caused by this tool.

## Remediation

### For End Users

1. **Update Firmware**: Check for and install the latest firmware updates from ASUS
2. **Disable Remote Management**: If not needed, disable remote access to the router's web interface
3. **Network Segmentation**: Place the router's management interface on a separate, trusted network
4. **Monitor for Updates**: Regularly check ASUS security advisories for your router model

### For Network Administrators

- Implement network access controls to restrict access to router management interfaces
- Monitor for unauthorized access attempts
- Consider using VPNs or other secure access methods for router administration
- Replace vulnerable devices if patches are not available

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests for:
- Additional affected device detection
- Improved output formatting
- Documentation improvements
- Security enhancements

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## References

- [CVE-2018-18287 - MITRE](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-18287)
- [ASUS Security Advisory Center](https://www.asus.com/support/security-advisory/)
- [National Vulnerability Database](https://nvd.nist.gov/vuln/detail/CVE-2018-18287)

## Acknowledgments

This research was conducted to improve security awareness and help users protect their network infrastructure.

---

**Ethical Use Notice**: This tool is intended for security researchers, penetration testers, and network administrators to assess the security of systems they are authorized to test. Always obtain proper authorization before testing any system.

