# Windterm Session Converter

Converts a table containing IP, label, group, and icon separated by
pipes (|) into Windterm session JSON format.

## Introduction

This Python project aims to simplify the conversion of tabular data,
typically found in pipe-separated files, into the JSON format required
by Windterm session configurations.

## Usage

1. Prepare your input file containing the table with IP, label, group,
	 and icon separated by pipes (|).
   
   Example input file (input.txt):
	 
   ```
   |192.168.1.1|Server 1|Production| server-icon.png|
   |192.168.1.2|Server 2|Test| test-icon.png|
   ```

2. Run the converter script, specifying the input file:

    ```bash
    python main.py input.txt
    ```

3. The converted Windterm session JSON will be generated and printed to the console.

4. You can then copy the JSON output and use it to configure your Windterm sessions.

## Input Format

The input file should follow the format below:

```
|IP|Label|Group|Icon|
```

- **IP**: The IP address of the server or device.
- **Label**: A descriptive label for the session.
- **Group**: The group or category the session belongs to.
- **Icon**: The icon associated with the session.

Ensure that each field is separated by a pipe (|) character.

## Example

Consider the following input file (input.txt):

```
|192.168.1.1|Server 1|Production|linux|
|192.168.1.2|Server 2|Test|centos|
```

Running the converter will produce the following JSON output:




```json
[
    {
        "session.group": "Production",
        "session.icon": "linux",
        "session.label": "Server 1 - 192.168.1.1",
        "session.port": 22,
        "session.protocol": "SSH",
        "session.target": "192.168.1.1",
        "session.uuid": "sdfkjs33-e5f1-4909-b390-a4dda358305f"
    },
    {
        "session.group": "Test",
        "session.icon": "centos",
        "session.label": "Server 2 - 192.168.1.2",
        "session.port": 22,
        "session.protocol": "SSH",
        "session.target": "192.168.1.2",
        "session.uuid": "5sdf55pw-e5f1-4909-b390-a4dda358305f"
    }
]
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
