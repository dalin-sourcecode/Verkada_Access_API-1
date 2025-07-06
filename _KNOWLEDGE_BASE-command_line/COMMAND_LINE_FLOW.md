# Command Line Flow Diagram

## Visual Flow

```
User types: python ESSENTIAL_instance.py list-groups
                                           ↓
                                    ┌─────────────────┐
                                    │ Python starts   │
                                    │ the script      │
                                    └─────────────────┘
                                           ↓
                                    ┌─────────────────┐
                                    │ if __name__ ==  │
                                    │ "__main__":     │
                                    │     main()      │
                                    └─────────────────┘
                                           ↓
                                    ┌─────────────────┐
                                    │ Create parser   │
                                    │ parser =        │
                                    │ ArgumentParser  │
                                    └─────────────────┘
                                           ↓
                                    ┌─────────────────┐
                                    │ Define args     │
                                    │ parser.add_     │
                                    │ argument(...)   │
                                    └─────────────────┘
                                           ↓
                                    ┌─────────────────┐
                                    │ Parse args      │
                                    │ args = parser.  │
                                    │ parse_args()    │
                                    │ args.action =   │
                                    │ "list-groups"   │
                                    └─────────────────┘
                                           ↓
                                    ┌─────────────────┐
                                    │ Check action    │
                                    │ if args.action  │
                                    │ == "list-groups"│
                                    └─────────────────┘
                                           ↓
                                    ┌─────────────────┐
                                    │ Execute         │
                                    │ INSTANCE_GET_   │
                                    │ ACCESS_GROUPS_  │
                                    │ list(class_0)   │
                                    └─────────────────┘
                                           ↓
                                    ┌─────────────────┐
                                    │ Display         │
                                    │ results         │
                                    └─────────────────┘
```

## Key Components Summary

| Component | Purpose | Example |
|-----------|---------|---------|
| `argparse` | Parse command line arguments | `import argparse` |
| `ArgumentParser` | Create the parser object | `parser = argparse.ArgumentParser()` |
| `add_argument` | Define what arguments are allowed | `parser.add_argument('action', choices=[...])` |
| `parse_args()` | Read the actual command line input | `args = parser.parse_args()` |
| `args.action` | Access the parsed argument | `if args.action == 'list-groups':` |
| `if __name__ == "__main__"` | Entry point when script is run | `if __name__ == "__main__": main()` |

## The Magic Happens Here

The key insight is that **`args.action` contains whatever the user typed after the script name**.

- User types: `python script.py list-groups`
- `args.action` becomes: `"list-groups"`
- Code checks: `if args.action == "list-groups":`
- Result: The correct function gets called

This is much cleaner than editing code every time you want to run a different operation! 