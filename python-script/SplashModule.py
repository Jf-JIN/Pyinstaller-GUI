from contextlib import suppress

with suppress(ModuleNotFoundError):
    import pyi_splash
    pyi_splash.close()