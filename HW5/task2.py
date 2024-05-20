def isIpValid(ip):
    octets = ip.split('.')
    for octet in octets:
        if not(0 <= int(octet) <= 255):
            return False
    return True

def isPrivate(ip):
    octets = list(map(int, ip.split('.')))
    if (octets[0] == 10
            or
            (octets[0] == 172 and 16 <= octets[1] <= 31)
            or
            (octets[0] == 192 and octets[1] == 168)):
        return True
    return False

def analyzeIP(file):
    public = {}
    private = {}
    unique_ips = set()
    unique_domains = set()

    try:
        with open(file, 'r') as f:
            for line in f:
                line = line.strip()

                for sign in [',', '\t', ' ']:
                    if sign in line:
                        parts = line.split(sign)
                        if len(parts) == 2:
                            ip, domain = parts
                            break
                else:
                    continue

                if isIpValid(ip):
                    is_private = isPrivate(ip)

                    unique_domains.add(domain)
                    unique_ips.add(ip)

                    if is_private:
                        private[ip] = domain
                    else:
                        public[ip] = domain
                else:
                    continue
        print()
        print("Public IPs:")
        for ip, domain in public.items():
            print(f"{ip} : {domain}")
        print()
        print("Private IPs:")
        for ip, domain in private.items():
            print(f"{ip} : {domain}")
        print()
        print("Unique IPs:")
        for ip in unique_ips:
            print(ip)
        print()
        print("Unique Domains:")
        for domain in unique_domains:
            print(domain)
    except FileNotFoundError:
        print(f"File not exist")
analyzeIP('ip.txt')