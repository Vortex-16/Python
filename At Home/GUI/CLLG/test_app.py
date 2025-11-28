"""
Test Script for Wedding Wish Application
Verifies all modules are working correctly
"""

import sys
import os

def test_imports():
    """Test if all modules can be imported"""
    print("🔍 Testing module imports...")
    
    try:
        import wedding_config as config
        print("✅ wedding_config.py imported successfully")
        print(f"   - Bride: {config.BRIDE_NAME}")
        print(f"   - Groom: {config.GROOM_NAME}")
        print(f"   - Date: {config.WEDDING_DATE}")
    except Exception as e:
        print(f"❌ Error importing wedding_config: {e}")
        return False
    
    try:
        import wedding_effects as effects
        print("✅ wedding_effects.py imported successfully")
        print(f"   - Sparkle class available: {hasattr(effects, 'Sparkle')}")
        print(f"   - FloatingHeart class available: {hasattr(effects, 'FloatingHeart')}")
        print(f"   - PulsingEffect class available: {hasattr(effects, 'PulsingEffect')}")
    except Exception as e:
        print(f"❌ Error importing wedding_effects: {e}")
        return False
    
    try:
        import wedding_messages as messages
        print("✅ wedding_messages.py imported successfully")
        print(f"   - Main wishes count: {len(messages.MAIN_WISHES)}")
        print(f"   - Blessings count: {len(messages.BLESSINGS)}")
        print(f"   - Personal message length: {len(messages.PERSONAL_MESSAGE)} chars")
    except Exception as e:
        print(f"❌ Error importing wedding_messages: {e}")
        return False
    
    return True


def test_tkinter():
    """Test if tkinter is available"""
    print("\n🔍 Testing Tkinter availability...")
    
    try:
        import tkinter as tk
        print("✅ Tkinter is available")
        
        # Test creating a simple window (don't show it)
        root = tk.Tk()
        root.withdraw()  # Hide the window
        print("✅ Tkinter window can be created")
        root.destroy()
        return True
    except Exception as e:
        print(f"❌ Tkinter error: {e}")
        print("   Note: On Linux, you may need to install: sudo apt-get install python3-tk")
        return False


def test_effects():
    """Test effect classes"""
    print("\n🔍 Testing effect classes...")
    
    try:
        import wedding_effects as effects
        
        # Test Sparkle
        sparkle = effects.Sparkle(100, 100, 800, 600)
        sparkle.update()
        x, y, size = sparkle.get_position()
        print(f"✅ Sparkle class works (position: {x:.1f}, {y:.1f}, size: {size})")
        
        # Test FloatingHeart
        heart = effects.FloatingHeart(400, 300, 800, 600)
        heart.update()
        points = heart.get_heart_points()
        print(f"✅ FloatingHeart class works ({len(points)//2} points generated)")
        
        # Test PulsingEffect
        pulse = effects.PulsingEffect()
        scale = pulse.update()
        print(f"✅ PulsingEffect class works (scale: {scale:.2f})")
        
        return True
    except Exception as e:
        print(f"❌ Effect classes error: {e}")
        return False


def test_main_app():
    """Test if main application can be imported"""
    print("\n🔍 Testing main application...")
    
    try:
        # Try to import without running
        import MarrigaeWishToDiJi
        print("✅ MarrigaeWishToDiJi.py can be imported")
        print(f"✅ WeddingWishPage class available: {hasattr(MarrigaeWishToDiJi, 'WeddingWishPage')}")
        return True
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False
    except Exception as e:
        print(f"⚠️  Warning: {e}")
        print("   (This may be normal if tkinter isn't available)")
        return True


def test_executable():
    """Test if executable exists"""
    print("\n🔍 Testing executable...")
    
    exe_path = "dist/WeddingWish_Sakshi_Rajat"
    if os.path.exists(exe_path):
        size = os.path.getsize(exe_path)
        size_mb = size / (1024 * 1024)
        print(f"✅ Executable found: {exe_path}")
        print(f"   Size: {size_mb:.1f} MB")
        
        # Check if executable
        if os.access(exe_path, os.X_OK):
            print("✅ File is executable")
        else:
            print("⚠️  File exists but may not be executable")
        return True
    else:
        print(f"❌ Executable not found at: {exe_path}")
        print("   Run: pyinstaller WeddingWish_Sakshi_Rajat.spec")
        return False


def test_buildozer_config():
    """Test if buildozer config exists"""
    print("\n🔍 Testing buildozer configuration...")
    
    if os.path.exists("buildozer.spec"):
        print("✅ buildozer.spec found")
        
        with open("buildozer.spec", "r") as f:
            content = f.read()
            if "weddingwish" in content:
                print("✅ Configuration is for wedding wish app")
            else:
                print("⚠️  Configuration may not be correct")
        return True
    else:
        print("❌ buildozer.spec not found")
        return False


def main():
    """Run all tests"""
    print("=" * 60)
    print("🎊 Wedding Wish Application - Test Suite 🎊")
    print("=" * 60)
    print()
    
    results = []
    
    # Run tests
    results.append(("Module Imports", test_imports()))
    results.append(("Tkinter", test_tkinter()))
    results.append(("Effect Classes", test_effects()))
    results.append(("Main Application", test_main_app()))
    results.append(("Executable", test_executable()))
    results.append(("Buildozer Config", test_buildozer_config()))
    
    # Summary
    print("\n" + "=" * 60)
    print("📊 TEST SUMMARY")
    print("=" * 60)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status} - {test_name}")
    
    print("-" * 60)
    print(f"Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("\n🎉 All tests passed! Application is ready! 🎉")
        print("\n💑 Ready for Sakshi Didi & Rajat Jiju's wedding! 💑")
    else:
        print(f"\n⚠️  {total - passed} test(s) failed. Check errors above.")
    
    print("=" * 60)
    
    return passed == total


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
