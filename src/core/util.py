



def find_first_file_byExt(pasta: str, prefix: str, ext: list[str]) -> str:
    """
    Finds the first file in the given directory with the specified prefix and extension.
    
    :param pasta: Directory to search in.
    :param prefix: Prefix of the file name.
    :param ext: List of file extensions to check.
    :return: Full path of the first matching file, or an empty string if not found.
    """
    from pathlib import Path
    
    for ext_item in ext:
        for file in Path(pasta).glob(f"{prefix}*{ext_item}"):
            return str(file)
    
    return ""