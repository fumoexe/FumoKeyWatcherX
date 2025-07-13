
# FumoKeyWatcherX

> **Educational Input Monitoring & Security Tool by Fumo**

**FumoMonitor** is a Python-based educational tool designed for ethical hacking demonstrations, red team simulations, and security research. It includes features such as input tracking, screenshot capture, self-replication, and basic command handling.

> ⚠️ This project is for **educational purposes only**. Do not use it on any system without **explicit permission**.

---

## Features

* **Input Monitoring** – Tracks keystrokes (including special characters) for security research.
* **Screenshot Capture** – Takes periodic screenshots (can be remotely controlled).
* **Persistence** – Copies itself to `%APPDATA%` and registers for automatic startup.
* **Auto-Restore** – Re-downloads itself from a backup URL if deleted.
* **Remote Commands via Discord Webhook** – Allows simple remote commands.
* **Remote Control via Discord Webhook** – Commands and screenshots are managed through a Discord webhook.
* **Single Instance Check** – Ensures only one instance is running at a time.
* **Shutdown Trigger** – Stops if a specific shutdown code is typed.

⚠️ Currently, there are some bugs; improvements and fixes are coming soon.

---

## Modules Used

### Built-in Modules

* os
* sys
* shutil
* subprocess
* threading
* platform
* uuid
* time
* io
* winreg

### External Modules

* pynput – Input monitoring
* Pillow – Screenshot handling
* requests – HTTP requests

Install them with:

```bash
pip install pynput Pillow requests
```

---

## How to Use

> **Test only in controlled environments**!

1. Install the required libraries:

   ```bash
   pip install pynput Pillow requests
   ```

2. Edit the script:

   * Replace the Discord webhook and backup URL as needed.
   * Or disable the webhook section for local testing.

3. Run the script:

   ```bash
   python fumo_monitor.py
   ```

4. On first run:

   * It copies itself to `%APPDATA%\WindowsUpdater\main.exe`
   * Registers to start automatically with Windows
   * Starts monitoring inputs and taking screenshots

5. Remote Commands via Discord Webhook:

   * `!stop` – Shut down the tool
   * `!clean` – Remove from startup and delete files
   * `!stop_screenshot` – Pause screenshotting
   * `!start_screenshot` – Resume screenshotting

---

## License

```
MIT License

Copyright (c) 2025 Fumo

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software for educational purposes only, including without limitation the rights
to use, copy, modify, merge, publish, distribute copies of the Software,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND.
```

---

## Disclaimer

> This tool is intended for **educational** and **ethical** use only. Misuse may violate laws in your country. Always get permission before running it on a device.

---

## Author

**Created by:** Fumo  
**Year:** 2025
