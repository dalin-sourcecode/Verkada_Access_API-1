# VERKADA API Usage Guide

## Running Different Instances

Instead of commenting/uncommenting function calls, use command line arguments:

### Available Commands

```bash
# List all access groups
python ESSENTIAL_instance.py list-groups

# List all users
python ESSENTIAL_instance.py list-users

# Get users with deactivated cards
python ESSENTIAL_instance.py deactivated-cards

# Reactivate access cards
python ESSENTIAL_instance.py reactivate-cards

# Compare groups between CSV and Verkada
python ESSENTIAL_instance.py compare-groups

# Compare users between CSV and Verkada
python ESSENTIAL_instance.py compare-users

# Create missing groups
python ESSENTIAL_instance.py create-groups

# Create missing users
python ESSENTIAL_instance.py create-users

# Add users to groups
python ESSENTIAL_instance.py add-users-to-groups
```

### Get Help

```bash
python ESSENTIAL_instance.py --help
```

### Example Workflow

```bash
# 1. First, check what groups exist
python ESSENTIAL_instance.py list-groups

# 2. Compare what groups are missing
python ESSENTIAL_instance.py compare-groups

# 3. Create missing groups
python ESSENTIAL_instance.py create-groups

# 4. Compare what users are missing
python ESSENTIAL_instance.py compare-users

# 5. Create missing users
python ESSENTIAL_instance.py create-users

# 6. Add users to groups
python ESSENTIAL_instance.py add-users-to-groups
```

## Alternative Options

### Option 2: Individual Script Files

You could also create separate files for each operation:

- `list_groups.py`
- `create_users.py`
- `add_to_groups.py`
- etc.

### Option 3: Interactive Menu

Create an interactive menu system that prompts the user to choose an action.

### Option 4: Configuration File

Use a configuration file to specify which operations to run. 