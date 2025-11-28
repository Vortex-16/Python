"""
Build Script for Wedding Wish Application
Generates .exe for Windows and .apk for Android
"""

import os
import sys
import subprocess


def create_exe():
    """Create Windows executable using PyInstaller"""
    print("\n" + "="*60)
    print("Creating Windows .exe file...")
    print("="*60 + "\n")
    
    # PyInstaller command
    cmd = [
        "pyinstaller",
        "--onefile",
        "--windowed",
        "--name=WeddingWish_Sakshi_Rajat",
        "--icon=NONE",
        "--add-data=wedding_config.py:.",
        "--add-data=wedding_effects.py:.",
        "--add-data=wedding_messages.py:.",
        "MarrigaeWishToDiJi.py"
    ]
    
    try:
        subprocess.run(cmd, check=True)
        print("\n✅ .exe file created successfully!")
        print("📁 Location: dist/WeddingWish_Sakshi_Rajat.exe")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error creating .exe: {e}")
        return False
    except FileNotFoundError:
        print("❌ PyInstaller not found. Installing...")
        subprocess.run([sys.executable, "-m", "pip", "install", "pyinstaller"])
        print("Please run this script again.")
        return False
    
    return True


def create_spec_file():
    """Create PyInstaller spec file for better control"""
    spec_content = '''# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['MarrigaeWishToDiJi.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('wedding_config.py', '.'),
        ('wedding_effects.py', '.'),
        ('wedding_messages.py', '.')
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='WeddingWish_Sakshi_Rajat',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
'''
    
    with open('WeddingWish.spec', 'w') as f:
        f.write(spec_content)
    
    print("✅ Spec file created: WeddingWish.spec")


def print_instructions():
    """Print instructions for building"""
    print("\n" + "="*60)
    print("📋 BUILD INSTRUCTIONS")
    print("="*60 + "\n")
    
    print("🪟 FOR WINDOWS .EXE:")
    print("  1. Install PyInstaller: pip install pyinstaller")
    print("  2. Run: python build.py")
    print("  OR")
    print("  2. Run: pyinstaller WeddingWish.spec")
    print("  3. Find the .exe in: dist/WeddingWish_Sakshi_Rajat.exe")
    
    print("\n📱 FOR ANDROID .APK:")
    print("  1. Install buildozer: pip install buildozer")
    print("  2. Convert the Tkinter app to Kivy (see wedding_kivy.py)")
    print("  3. Create buildozer.spec: buildozer init")
    print("  4. Build: buildozer -v android debug")
    print("  5. Find .apk in: bin/")
    
    print("\n⚠️  NOTES:")
    print("  - .exe creation works on Windows, Linux, Mac")
    print("  - .apk creation requires Linux or Mac with buildozer")
    print("  - Tkinter doesn't work on Android, use Kivy instead")
    print("  - For Android, use the Kivy version provided")
    
    print("\n" + "="*60 + "\n")


if __name__ == "__main__":
    print("\n🎊 Wedding Wish Application Builder 🎊")
    print("For Sakshi Didi & Rajat Jiju's Wedding\n")
    
    create_spec_file()
    print_instructions()
    
    response = input("\nDo you want to create the .exe now? (y/n): ")
    if response.lower() == 'y':
        create_exe()
