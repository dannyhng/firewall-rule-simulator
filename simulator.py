import json

def load_rules():
    with open('rules.json') as f:
        return json.load(f)

def load_traffic():
    with open('test_traffic.json') as f:
        return json.load(f)

def check_packet(packet, rules):
    for rule in rules:
        if (
            rule['ip'] == packet['ip'] and
            rule['port'] == packet['port'] and
            rule['protocol'] == packet['protocol']
        ):
            return rule['action']
    return 'allow'  # default action

def main():
    rules = load_rules()
    traffic = load_traffic()

    for pkt in traffic:
        action = check_packet(pkt, rules)
        print(f"Packet to {pkt['ip']}:{pkt['port']} via {pkt['protocol'].upper()} is {action.upper()}.")

if __name__ == '__main__':
    main()
