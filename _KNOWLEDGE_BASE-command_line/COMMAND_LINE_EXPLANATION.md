# Command Line Arguments Explained

## Overview
The command line approach uses Python's built-in `argparse` module to handle command line arguments. Here's how it works:

## 1. **Import the Required Module**

```python
import argparse
```

**What it does:** `argparse` is Python's standard library for parsing command line arguments. It's built into Python, so no installation needed.

## 2. **Create an Argument Parser**

```python
parser = argparse.ArgumentParser(description='VERKADA API Operations')
```

**What it does:** 
- Creates a parser object that will handle command line arguments
- `description='VERKADA API Operations'` - This text appears when you run `python script.py --help`

## 3. **Define Available Arguments**

```python
parser.add_argument('action', choices=[
    'list-groups',
    'list-users', 
    'deactivated-cards',
    'reactivate-cards',
    'compare-groups',
    'compare-users',
    'create-groups',
    'create-users',
    'add-users-to-groups'
], help='Action to perform')
```

**What it does:**
- `'action'` - This is the name of the argument (what you type after the script name)
- `choices=[...]` - Only these values are allowed. If you type something else, you get an error
- `help='Action to perform'` - This text appears in the help message

## 4. **Parse the Arguments**

```python
args = parser.parse_args()
```

**What it does:** 
- Reads the command line arguments you typed
- Stores them in the `args` object
- If you typed `python script.py list-groups`, then `args.action` will contain `'list-groups'`

## 5. **Use the Arguments**

```python
if args.action == 'list-groups':
    INSTANCE_GET_ACCESS_GROUPS_list(class_0)
elif args.action == 'list-users':
    INSTANCE_get_the_users(class_0)
# ... and so on
```

**What it does:**
- Checks what action the user requested
- Calls the appropriate function based on the argument

## 6. **The Entry Point**

```python
if __name__ == "__main__":
    main()
```

**What it does:**
- This is the "entry point" - where the program starts when you run it
- Calls the `main()` function which contains all the argument parsing logic

## How It Works in Practice

### When you run:
```bash
python ESSENTIAL_instance.py list-groups
```

### Here's what happens:

1. **Python starts the script** → `if __name__ == "__main__":` is True
2. **Calls main()** → `main()` function executes
3. **Creates parser** → `parser = argparse.ArgumentParser(...)`
4. **Defines arguments** → `parser.add_argument(...)`
5. **Parses command line** → `args = parser.parse_args()` reads `'list-groups'`
6. **Checks argument** → `if args.action == 'list-groups':` is True
7. **Executes function** → `INSTANCE_GET_ACCESS_GROUPS_list(class_0)` runs

## Built-in Help System

The `argparse` module automatically creates help text:

```bash
python ESSENTIAL_instance.py --help
```

**Output:**
```
usage: ESSENTIAL_instance.py [-h] {list-groups,list-users,deactivated-cards,reactivate-cards,compare-groups,compare-users,create-groups,create-users,add-users-to-groups}

VERKADA API Operations

positional arguments:
  {list-groups,list-users,deactivated-cards,reactivate-cards,compare-groups,compare-users,create-groups,create-users,add-users-to-groups}
                        Action to perform

optional arguments:
  -h, --help            show this help message and exit
```

## Error Handling

If you type an invalid command:
```bash
python ESSENTIAL_instance.py invalid-command
```

**Output:**
```
usage: ESSENTIAL_instance.py [-h] {list-groups,list-users,deactivated-cards,reactivate-cards,compare-groups,compare-users,create-groups,create-users,add-users-to-groups}
ESSENTIAL_instance.py: error: argument action: invalid choice: 'invalid-command' (choose from 'list-groups', 'list-users', 'deactivated-cards', 'reactivate-cards', 'compare-groups', 'compare-users', 'create-groups', 'create-users', 'add-users-to-groups')
```

## Advantages of This Approach

1. **No Code Editing**: You don't need to edit the script to run different operations
2. **Built-in Validation**: Only valid commands are accepted
3. **Help System**: Automatic help text explains how to use the script
4. **Scriptable**: Can be easily automated or used in scripts
5. **Professional**: This is how most command-line tools work

## Common Patterns

### Optional Arguments
```python
parser.add_argument('--verbose', action='store_true', help='Enable verbose output')
```

### Arguments with Values
```python
parser.add_argument('--file', type=str, help='Input file path')
```

### Multiple Arguments
```python
parser.add_argument('--users', nargs='+', help='List of user names')
```

This approach makes your script behave like professional command-line tools you're familiar with (like `git`, `docker`, `pip`, etc.)! 