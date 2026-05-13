# Raw JPEG Recovery Tool

A Python script that scans a raw disk drive byte-by-byte to recover deleted or lost JPEG images by identifying JPEG signatures (`FF D8 FF E0`) and extracting them.

## 🚨 Important Warning

**This script reads raw disk data. Running it incorrectly can cause data loss or system instability.**

- Always run as **Administrator**
- Always test on a **USB drive or backup** first
- Do **NOT** write to the same drive you are recovering from

---

## 🧠 How It Works

1. Opens a disk drive in raw read mode (`\\.\D:`)
2. Scans bytes looking for JPEG header: `FF D8 FF E0 00 10 4A 46`
3. When header is found, starts writing to a new `.jpg` file
4. Continues until JPEG footer `FF D9` is found
5. Saves the complete JPEG and continues scanning

---

## 📋 Requirements

| Requirement | Details |
|-------------|---------|
| **OS** | Windows (7, 8, 10, 11) |
| **Python** | Version 3.6 or higher |
| **Permissions** | Administrator rights |
| **Drive** | A raw drive letter (C:, D:, E:, USB, SD card) |

No external libraries needed — uses only Python built-ins.

---

## 🛠️ Installation & Setup

### 1. Install Python (if not already installed)

Download from [python.org](https://python.org) — check **"Add Python to PATH"** during installation.

Verify installation:

```cmd
python --version
