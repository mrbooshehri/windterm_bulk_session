import sys
import json

def read_file_into_dict(filename):
    data = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split('|')[1:-1]
            if len(parts) ==  4:
                ip = parts[0].strip()
                hostname = parts[1].strip()
                group = parts[2].strip()
                icon = parts[3].strip()
                data.append({'session.group': group , 'session.icon': icon, 'session.label': f"{hostname} - {ip}", 'session.port': 22, 'session.protocol': "SSH", 'session.target': ip, 'session.uuid': "512c7488-e5f1-4909-b390-a4dda358305f"})
    return data

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Parse simple table to windterm session json format")
        print("\tSample file: |IP_ADDRESS|LABLE|GROUP|ICON|")
        sys.exit(1)

    input_file = sys.argv[1]
    data = read_file_into_dict(input_file)
    json_data = json.dumps(data,indent=4)
    print(json_data)
