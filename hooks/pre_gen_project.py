import re
import sys


def validate_monorepo_directory(name: str):
    """
    Validate a monorepo name with the PEP 508 rules.
    
    Rules:
    - Must consist of ASCII letters, digits, underscores, hyphens, and periods
    - Must not start or end with an underscore, hyphen, or period
    
    Args:
        name: The project name to validate
        
    Returns:
        A tuple of (is_valid, error_message)
        If valid, returns (True, None)
        If invalid, returns (False, error_message)
    """
    if not name:
        return False, "Monorepo directory cannot be empty"
    
    # Check if name starts or ends with invalid characters
    if name[0] in ('_', '-', '.'):
        return False, f"Monorepo directory cannot start with '{name[0]}'"
    
    if name[-1] in ('_', '-', '.'):
        return False, f"Monorepo directory cannot end with '{name[-1]}'"
    
    # Check if all characters are valid (ASCII letters, digits, _, -, .)
    if not re.match(r'^[a-zA-Z0-9._-]+$', name):
        return False, "Monorepo directory must only contain ASCII letters, digits, underscores, hyphens, and periods"
    
    return True, None


if __name__ == "__main__":
    monorepo_directory = "{{ cookiecutter.__monorepo_directory }}"
    valid, error = validate_monorepo_directory(monorepo_directory)
    if not valid:
        print(f"ERROR: The monorepo directory ('{monorepo_directory}') is not a valid. {error}.")

        # exit to cancel recipe
        sys.exit(1)
