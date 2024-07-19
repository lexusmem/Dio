
# pep257 - convensões da docstring

def kos_root():
    """Return the pathname of the KOS root directory."""
    global kos_root
    if kos_root:
        return kos_root
