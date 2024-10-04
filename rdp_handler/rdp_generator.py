import os


def generate_rdp_file(params: dict, output_dir: str) -> str:
    if 'v' not in params or 'username' not in params:
        raise ValueError("Missing required parameters 'v' (server address) or 'username'")

    rdp_content = f"""full address:s:{params['v']}
prompt for credentials:i:1
remoteapplicationmode:i:0
authentication level:i:2
administrative session:i:0
username:s:{params['username']}
"""

    if params.get('f', False):
        rdp_content += "screen mode id:i:2\n"  # Full-screen mode

    if 'w' in params and 'h' in params:
        rdp_content += f"desktopwidth:i:{params['w']}\ndesktopheight:i:{params['h']}\n"

    if params.get('multimon', False):
        rdp_content += "use multimon:i:1\n"

    # Additional settings
    rdp_content += """audiocapturemode:i:1
audiomode:i:0
camerastoredirect:s:*
devicestoredirect:s:*
drivestoredirect:s:*
redirectsmartcards:i:1
redirectclipboard:i:1
redirectprinters:i:1
redirectcomports:i:1
redirectwebauthn:i:1
"""

    # Write to a temporary file
    rdp_filename = f"connection_{os.getpid()}.rdp"
    rdp_filepath = os.path.join(output_dir, rdp_filename)

    with open(rdp_filepath, 'w', encoding='utf-8') as file:
        file.write(rdp_content)

    return rdp_filepath
