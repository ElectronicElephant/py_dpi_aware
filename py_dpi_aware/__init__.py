import sys
if sys.platform == 'win32':
    try:
        import ctypes
        import platform
        release, _, _, _ = platform.win32_ver()

        if release in ['10', '8']:
            # Set DPI Awareness
            errorCode = ctypes.windll.shcore.SetProcessDpiAwareness(2)

            # Check DPI Awareness
            awareness = ctypes.c_int()
            errorCode = ctypes.windll.shcore.GetProcessDpiAwareness(0, ctypes.byref(awareness))

            if errorCode:
                print('Setting DPI Awareness failed with errorCode %d. OS: Windows %s.', (errorCode, release))
            elif awareness.value == 2:
                print('Per monitor DPI aware is set.')
            else:
                print('Setting DPI Awareness failed. Unknown Error.')
        elif release in ['7', 'Vista']:
            # Set DPI Awareness
            success = ctypes.windll.user32.SetProcessDPIAware()
            print('Setting DPI Awareness OK.')

    except (ImportError, AttributeError, OSError):
        print('Setting DPI Awareness failed. Unknown Error.')
