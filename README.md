# PWSH-Env-Enc

## Overview

- This Python script is use to encode a powershell commands and scripts into environment variable indexes which can be ran in a PS console. It helps in obfuscating PowerShell commands for various purposes such as penetration testing, malware development, or system administration tasks.

Inspired by John Hammonds methodology in this [video](https://www.youtube.com/watch?v=8CiNx4nNqQ0)

## Features

- Encodes PowerShell commands to bypass security restrictions.
- Supports encoding of arbitrary PowerShell commands.
- Pre-encodes commands to handle special characters like single quotes, double quotes, or dollar signs.
- Generates encoded PowerShell commands ready for execution.


## How to Use

1. Clone the Repository:

```
git clone https://github.com/malwarekid/PWSH-Env-Enc.git &&
cd PWSH-Env-Enc
```

2. Run the Script:

```
python3 PWSH-Env-Enc.py
```

```
    ____ _       _______ __  __      ______                 ______          
   / __ \ |     / / ___// / / /     / ____/___ _   __      / ____/___  _____
  / /_/ / | /| / /\__ \/ /_/ /_____/ __/ / __ \ | / /_____/ __/ / __ \/ ___/
 / ____/| |/ |/ /___/ / __  /_____/ /___/ / / / |/ /_____/ /___/ / / / /__  
/_/     |__/|__//____/_/ /_/     /_____/_/ /_/|___/     /_____/_/ /_/\___/  
                                                             By @malwarekid

Powershell command (leave empty for SCRIPT file) : net user
Pre encode the command? (helpful if your command has ' or " or $ characters) [y/n]y
Wants to save the file? [y/n]n
Original Command
================================
net user
================================
Encoded Command
================================
Start-Process PowerShell.exe -ArgumentList ('-ep bypass -w h -e bgBlAHQAIAB1AHMAZQByAA==')
================================
FINAL Encoded Command
================================
& ($( [char]105,[char]101,[char]120 ) -Join $($null)) ($( [char]83,[char]116,[char]97,[char]114,[char]116,[char]45,[char]80,[char]114,[char]111,[char]99,[char]101,[char]115,[char]115,[char]32,[char]80,[char]111,[char]119,[char]101,[char]114,[char]83,[char]104,[char]101,[char]108,[char]108,[char]46,[char]101,[char]120,[char]101,[char]32,[char]45,[char]65,[char]114,[char]103,[char]117,[char]109,[char]101,[char]110,[char]116,[char]76,[char]105,[char]115,[char]116,[char]32,[char]40,[char]39,[char]45,[char]101,[char]112,[char]32,[char]98,[char]121,[char]112,[char]97,[char]115,[char]115,[char]32,[char]45,[char]119,[char]32,[char]104,[char]32,[char]45,[char]101,[char]32,[char]98,[char]103,[char]66,[char]108,[char]65,[char]72,[char]81,[char]65,[char]73,[char]65,[char]66,[char]49,[char]65,[char]72,[char]77,[char]65,[char]90,[char]81,[char]66,[char]121,[char]65,[char]65,[char]61,[char]61,[char]39,[char]41 ) -Join $($null))
```

3. Enter the PowerShell command you want to encode. If you leave it empty, you can provide the path to a script file.

4. Optionally, choose to pre-encode the command if it contains special characters like `'`, `"`, or `$`.

5. Choose whether to save the encoded command to a PowerShell script file.

6. The encoded PowerShell command will be displayed, and if chosen, saved to a file named `encoded.ps1`.

7. Run in the PS console like that: `powershell.exe -NoP -Ep Bypass -W h -File .\encoded.ps1`

## Requirements

- Python 3.x
- Base64 library (should be included in standard Python installations)

## Contributors

- [MalwareKid](https://github.com/malwarekid)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Notes

Feel free to contribute, report issues, or provide feedback and dont forget to follow me on [Instagram](https://www.instagram.com/malwarekid/) and [github](https://github.com/malwarekid/) Happy Hacking!
