# 💑 Wedding Wish Application for Sakshi Didi & Rajat Jiju 💑

## 🎊 About This Application

A beautiful, animated wedding wish page created with love for **Sakshi Didi & Rajat Jiju's** wedding on **30th November 2025**!

This application features:
- ✨ Stunning animations with floating hearts and sparkles
- 💖 Pulsing effects and rotating messages
- 🎨 Beautiful color scheme with gold and pink
- 📱 Both Desktop (Tkinter) and Mobile (Kivy) versions
- 🎁 Heartfelt personalized messages

## 📁 Project Structure

```
GUI/
├── MarrigaeWishToDiJi.py      # Main Tkinter application (Desktop)
├── wedding_config.py           # Configuration and styling constants
├── wedding_effects.py          # Animation effects classes
├── wedding_messages.py         # All wedding wishes and messages
├── wedding_kivy.py            # Kivy version for Android
├── build.py                   # Build script for executables
├── buildozer.spec             # Android build configuration
├── requirements.txt           # Python dependencies
├── README.md                  # This file
└── WeddingWish.spec           # PyInstaller specification
```

## 🚀 Running the Application

### Desktop Version (Windows/Linux/Mac)

**Requirements:**
- Python 3.7 or higher
- tkinter (usually comes with Python)

**Run:**
```bash
python MarrigaeWishToDiJi.py
```

### Mobile Version (Android Testing)

**Requirements:**
- Python 3.7 or higher
- Kivy and KivyMD

**Install and Run:**
```bash
pip install kivy kivymd
python wedding_kivy.py
```

## 📦 Creating Executables

### 🪟 Windows .EXE File

1. **Install PyInstaller:**
   ```bash
   pip install pyinstaller
   ```

2. **Create the .exe (Option 1 - Automated):**
   ```bash
   python build.py
   ```

3. **Create the .exe (Option 2 - Manual):**
   ```bash
   pyinstaller WeddingWish.spec
   ```
   OR
   ```bash
   pyinstaller --onefile --windowed --name="WeddingWish_Sakshi_Rajat" MarrigaeWishToDiJi.py
   ```

4. **Find your .exe:**
   - Location: `dist/WeddingWish_Sakshi_Rajat.exe`
   - This is a standalone executable that can run on any Windows PC
   - No Python installation needed on target machine!

### 📱 Android .APK File

**Important:** Tkinter doesn't work on Android, so we use the Kivy version.

#### Prerequisites (Linux/Mac):
```bash
# Install buildozer
pip install buildozer

# Install required system packages (Ubuntu/Debian)
sudo apt update
sudo apt install -y git zip unzip openjdk-17-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev

# Install Android SDK dependencies
sudo apt install -y build-essential ccache libncurses5:i386 libstdc++6:i386 libgtk2.0-0:i386 libpangox-1.0-0:i386 libpangoxft-1.0-0:i386 libidn11:i386 python3.8 python3-pip openjdk-17-jdk unzip
```

#### Build the APK:

1. **Initialize buildozer (first time only):**
   ```bash
   buildozer init
   # Use the provided buildozer.spec file
   ```

2. **Build the APK:**
   ```bash
   buildozer -v android debug
   ```

3. **Find your .apk:**
   - Location: `bin/weddingwish-1.0-debug.apk`
   - Transfer to Android phone and install
   - May need to enable "Install from Unknown Sources"

#### Alternative - Build with Docker:
```bash
# Use buildozer docker image
docker run --rm -v "$(pwd)":/home/user/hostcwd buildozer/buildozer android debug
```

## 🎨 Features

### Desktop Version (Tkinter)
- Full-screen experience with animations
- Floating hearts and sparkles
- Pulsing title effect
- Rotating congratulation messages
- Beautiful decorative frame around personal message
- Cycling blessings with emojis

### Mobile Version (Kivy)
- Mobile-optimized layout
- Portrait mode
- Scrollable personal message
- Pulsing animations
- Touch-friendly interface
- Beautiful gradient effects

## 🎯 Customization

You can easily customize the application by editing these files:

### `wedding_config.py`
- Change names, date, venue
- Modify colors and fonts
- Adjust animation settings

### `wedding_messages.py`
- Edit wishes and blessings
- Change personal message
- Add more celebration emojis

### `wedding_effects.py`
- Modify animation behaviors
- Adjust sparkle and heart counts
- Change movement patterns

## 📤 Uploading to GitHub

### Create a new repository:
```bash
# Initialize git (if not already done)
git init

# Add files
git add MarrigaeWishToDiJi.py wedding_*.py build.py buildozer.spec requirements.txt README.md WeddingWish.spec

# Commit
git commit -m "Wedding wish application for Sakshi & Rajat - 30 Nov 2025"

# Add remote (replace with your GitHub repo URL)
git remote add origin https://github.com/Vortex-16/WeddingWish.git

# Push
git push -u origin main
```

### Include built executables:
```bash
# Add the dist folder with .exe
git add dist/WeddingWish_Sakshi_Rajat.exe

# Add the bin folder with .apk (if created)
git add bin/*.apk

# Commit and push
git commit -m "Add executable files"
git push
```

## 🎁 Sharing the Application

### For Windows Users:
1. Share the `WeddingWish_Sakshi_Rajat.exe` file
2. Double-click to run (no installation needed)

### For Android Users:
1. Share the `.apk` file
2. Enable "Install from Unknown Sources" in phone settings
3. Install the APK
4. Open the app and enjoy!

### For Python Users:
1. Share the entire folder
2. Run: `pip install -r requirements.txt`
3. Run: `python MarrigaeWishToDiJi.py`

## 🐛 Troubleshooting

### Tkinter not found:
```bash
# Ubuntu/Debian
sudo apt-get install python3-tk

# Fedora
sudo dnf install python3-tkinter

# Mac (with brew)
brew install python-tk
```

### PyInstaller issues:
```bash
# Upgrade PyInstaller
pip install --upgrade pyinstaller

# Clear cache
pyinstaller --clean WeddingWish.spec
```

### Buildozer issues:
```bash
# Clean buildozer
buildozer android clean

# Update buildozer
pip install --upgrade buildozer
```

## 💝 Credits

Created with love for Sakshi Didi & Rajat Jiju's wedding!
Date: 30th November 2025

**Technologies Used:**
- Python 3
- Tkinter (Desktop GUI)
- Kivy (Mobile GUI)
- PyInstaller (Windows executable)
- Buildozer (Android APK)

## 📝 License

This is a personal wedding gift application. Feel free to modify and use for your own occasions!

---

## 🎊 Wishing Sakshi Didi & Rajat Jiju a lifetime of happiness! 🎊

**May your marriage be filled with:**
- ❤️ Endless love
- 😊 Boundless joy
- 🌟 Eternal happiness
- 💑 Togetherness forever

**Happy Wedding Day! 🎉👰🤵💍**
