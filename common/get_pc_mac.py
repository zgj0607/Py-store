import platform
import re
import subprocess


def find_all_ip(platform):
    ipstr = '([0-9]{1,3}\.){3}[0-9]{1,3}'
    if platform == "Darwin" or platform == "Linux":
        ipconfig_process = subprocess.Popen("ifconfig", stdout=subprocess.PIPE)
        output = ipconfig_process.stdout.read()
        ip_pattern = re.compile('(inet %s)' % ipstr)
        if platform == "Linux":
            ip_pattern = re.compile('(inet addr:%s)' % ipstr)
        pattern = re.compile(ipstr)
        iplist = []
        for ipaddr in re.finditer(ip_pattern, str(output)):
            ip = pattern.search(ipaddr.group())
            if ip.group() != "127.0.0.1":
                iplist.append(ip.group())
        return iplist
    elif platform == "Windows":
        ipconfig_process = subprocess.Popen("ipconfig", stdout=subprocess.PIPE)
        output = ipconfig_process.stdout.read()
        ip_pattern = re.compile("IPv4 Address(\. )*: %s" % ipstr)
        pattern = re.compile(ipstr)
        iplist = []
        for ipaddr in re.finditer(ip_pattern, str(output)):
            ip = pattern.search(ipaddr.group())
            if ip.group() != "127.0.0.1":
                iplist.append(ip.group())
        return iplist


def find_all_mask(platform):
    ipstr = '([0-9]{1,3}\.){3}[0-9]{1,3}'
    maskstr = '0x([0-9a-f]{8})'
    if platform == "Darwin" or platform == "Linux":
        ipconfig_process = subprocess.Popen("ifconfig", stdout=subprocess.PIPE)
        output = ipconfig_process.stdout.read()
        mask_pattern = re.compile('(netmask %s)' % maskstr)
        pattern = re.compile(maskstr)
        if platform == "Linux":
            mask_pattern = re.compile(r'Mask:%s' % ipstr)
            pattern = re.compile(ipstr)
        masklist = []
        for maskaddr in mask_pattern.finditer(str(output)):
            mask = pattern.search(maskaddr.group())
            if mask.group() != '0xff000000' and mask.group() != '255.0.0.0':
                masklist.append(mask.group())
        return masklist
    elif platform == "Windows":
        ipconfig_process = subprocess.Popen("ipconfig", stdout=subprocess.PIPE)
        output = ipconfig_process.stdout.read()
        mask_pattern = re.compile(r"Subnet Mask (\. )*: %s" % ipstr)
        pattern = re.compile(ipstr)
        masklist = []
        for maskaddr in mask_pattern.finditer(str(output)):
            mask = pattern.search(maskaddr.group())
            if mask.group() != '255.0.0.0':
                masklist.append(mask.group())
        return masklist


def get_broad_addr(ipstr, maskstr):
    iptokens = map(int, ipstr.split("."))
    masktokens = map(int, maskstr.split("."))
    broadlist = []
    for i in range(len(iptokens)):
        ip = iptokens[i]
        mask = masktokens[i]
        broad = ip & mask | (~mask & 255)
        broadlist.append(broad)
    return '.'.join(map(str, broadlist))


def find_all_broad(platform):
    ipstr = '([0-9]{1,3}\.){3}[0-9]{1,3}'
    if platform == "Darwin" or platform == "Linux":
        ipconfig_process = subprocess.Popen("ifconfig", stdout=subprocess.PIPE)
        output = (ipconfig_process.stdout.read())
        broad_pattern = re.compile('(broadcast %s)' % ipstr)
        if platform == "Linux":
            broad_pattern = re.compile(r'Bcast:%s' % ipstr)
        pattern = re.compile(ipstr)
        broadlist = []
        for broadaddr in broad_pattern.finditer(str(output)):
            broad = pattern.search(broadaddr.group())
            broadlist.append(broad.group())
        return broadlist
    elif platform == "Windows":
        iplist = find_all_ip(platform)
        masklist = find_all_mask(platform)
        broadlist = []
        for i in range(len(iplist)):
            broadlist.append(get_broad_addr(iplist[i], masklist[i]))
        return broadlist


def get_pc_mac(platform):
    if platform == "Darwin" or platform == "Linux":
        get_linux_mac()

    elif platform == "Windows":
        iplist = find_all_ip(platform)
        masklist = find_all_mask(platform)
        broadlist = []
        for i in range(len(iplist)):
            broadlist.append(get_broad_addr(iplist[i], masklist[i]))
        return broadlist


def get_linux_mac():
    mac_str_pattern = re.compile('\w{2}:\w{2}:\w{2}:\w{2}:\w{2}:\w{2}')
    inf_name_pattern = re.compile('en[0-9]:')
    status_pattern = re.compile('status: active')
    ipconfig_process = subprocess.Popen("ifconfig", stdout=subprocess.PIPE)
    output = (ipconfig_process.stdout.readlines())
    print(str(output))
    for row_num, line in enumerate(output):
        result = re.findall(inf_name_pattern, str(line))
        if result:
            temp_line = str(output[row_num + 1])
            if not re.findall(mac_str_pattern, temp_line):
                continue

            temp_mac = temp_line.split(' ')[1]
            name = ''
            i = 1
            while not name:
                next_line = str(output[row_num + i])
                if re.findall(status_pattern, next_line):
                    mac = temp_mac.replace(':', '').upper()
                    return mac
                name = re.findall(inf_name_pattern, str(output[row_num + i + 1]))
                i += 1


def get_windows_mac():
    ipconfig_process = subprocess.Popen("ipconfig /all", stdout=subprocess.PIPE)
    output = (ipconfig_process.stdout.encoding('UTF-8'))


system = platform.system()
print(find_all_ip(system))
print(find_all_mask(system))
print(find_all_broad(system))
print(find_all_mac(system))
