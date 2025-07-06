# VERKADA Vendor API Management System

A Python-based system for managing vendor access groups and users in the Verkada platform through their API.

## Overview

This project provides a comprehensive solution for:
- Managing vendor access groups in Verkada
- Creating and managing vendor users
- Comparing data between CSV files and Verkada
- Automating user and group management tasks

## Project Structure

```
├── ESSENTIAL_instance.py      # Main entry point with CLI interface
├── ESSENTIAL_Values.py        # Configuration values and constants
├── INFORMATION_logger.py      # Logging configuration and setup
├── METHOD_controller.py       # Main API controller class
├── METHOD_func.py            # Utility functions for data processing
├── METHOD_Parse.py           # Data parsing functions
├── METHOD_Requests.py        # HTTP request functions
├── logs/                     # Log files directory (created automatically)
├── requirements.txt          # Python dependencies
└── README.md                # This file
```

## Features

- **Command Line Interface**: Easy-to-use CLI for different operations
- **CSV Integration**: Reads vendor data from CSV files
- **API Management**: Full CRUD operations for Verkada API
- **Data Comparison**: Compare local data with Verkada data
- **Automated User Creation**: Generate users with fake emails
- **Group Management**: Create and manage access groups
- **Comprehensive Logging**: Detailed logging with file and console output
- **Error Handling**: Robust exception handling with detailed error messages

## Prerequisites

- Python 3.7 or higher
- Verkada API access (API key and token)
- CSV file with vendor employee data

## Installation

1. **Clone or download the project files**

2. **Install dependencies**:
   ```bash
   pip install -r _requirements.txt
   ```

3. **Configure your data**:
   - Update `ESSENTIAL_Values.py` with your API credentials
   - Ensure your CSV file (`Vendor Employee List.csv`) is in the project directory
   - Verify the CSV has the required columns: `VENDOR_GROUP`, `FIRST_NAME`, `LAST_NAME`

## Configuration

### Option 1: Environment Variables (Recommended)

1. Copy the example environment file:
   ```bash
   cp env.example .env
   ```

2. Edit `.env` and add your actual API key:
   ```
   VERKADA_API_KEY=your_actual_api_key_here
   ```

3. The application will automatically use the environment variable.

### Option 2: Direct Configuration

Edit `ESSENTIAL_Values.py` to set your configuration:

```python
# API Configuration
# SECURITY: Use environment variable for API key in production
# Set VERKADA_API_KEY environment variable or replace with your actual key
api_key = os.getenv("VERKADA_API_KEY", "YOUR_API_KEY_HERE")
token_url = "https://api.verkada.com/token"

# Email Configuration for new users
email_fake = "no-email"
email_random_number_start = 0
email_random_number_end = 900
emaiL_fake_domain = "@vendor.com"

# CSV Configuration
group_column = "VENDOR_GROUP"
```

## Usage

### Command Line Interface

The project uses a command-line interface for all operations:

```bash
# List all access groups
python ESSENTIAL_instance.py list-groups

# List all users
python ESSENTIAL_instance.py list-users

# Compare groups between CSV and Verkada
python ESSENTIAL_instance.py compare-groups

# Create missing groups
python ESSENTIAL_instance.py create-groups

# Compare users between CSV and Verkada
python ESSENTIAL_instance.py compare-users

# Create missing users
python ESSENTIAL_instance.py create-users

# Add users to groups
python ESSENTIAL_instance.py add-users-to-groups

# Get users with deactivated cards
python ESSENTIAL_instance.py deactivated-cards

# Reactivate access cards
python ESSENTIAL_instance.py reactivate-cards
```

### Get Help

```bash
python ESSENTIAL_instance.py --help
```

### Typical Workflow

1. **Check existing data**:
   ```bash
   python ESSENTIAL_instance.py list-groups
   python ESSENTIAL_instance.py list-users
   ```

2. **Compare with CSV data**:
   ```bash
   python ESSENTIAL_instance.py compare-groups
   python ESSENTIAL_instance.py compare-users
   ```

3. **Create missing data**:
   ```bash
   python ESSENTIAL_instance.py create-groups
   python ESSENTIAL_instance.py create-users
   ```

4. **Assign users to groups**:
   ```bash
   python ESSENTIAL_instance.py add-users-to-groups
   ```

## CSV File Format

Your CSV file should have the following structure:

| VENDOR_GROUP | FIRST_NAME | LAST_NAME |
|--------------|------------|-----------|
| VAC \| VENDOR \| JANITORIAL | John | Doe |
| VAC \| VENDOR \| PTM \| ABRAM | Jane | Smith |

## API Endpoints Used

- `GET /access/v1/access_groups` - List access groups
- `GET /access/v1/access_users` - List access users
- `POST /access/v1/access_groups/group` - Create access group
- `POST /core/v1/user` - Create user
- `POST /access/v1/access_groups/group?group_id={id}` - Add users to group

## Logging and Error Handling

### Logging System

The project includes a comprehensive logging system that provides:

- **File Logging**: Daily log files stored in the `logs/` directory
- **Console Logging**: User-friendly output for immediate feedback
- **Multiple Log Levels**: DEBUG, INFO, WARNING, ERROR
- **Detailed Context**: Function names, line numbers, and timestamps
- **Separate Loggers**: Different loggers for different components

### Log Files

Log files are automatically created in the `logs/` directory with the format:
- `verkada_api_YYYY-MM-DD.log` - Daily log files with detailed information

### Error Handling

The system includes robust error handling for:
- Invalid API credentials
- Network connectivity issues
- CSV file format errors
- Invalid command line arguments
- JSON parsing errors
- Missing data keys
- HTTP request failures

All errors are logged with full stack traces for debugging purposes.

## Security Notes

- **API Key Security**: Store API keys securely using environment variables
- **Version Control**: Never commit API keys to version control
- **Environment Variables**: Use the `.env` file for sensitive configuration
- **CSV Data**: The included CSV file contains sample data only - replace with your actual vendor data
- **Log Files**: Log files may contain sensitive information and are excluded from version control
- **Fake Emails**: The system generates fake email addresses for new users

### Security Checklist

Before deploying to production:
- [ ] Set up environment variables for API keys
- [ ] Replace sample CSV data with actual vendor information
- [ ] Review and configure logging levels
- [ ] Ensure `.env` file is in `.gitignore`
- [ ] Test with non-production API credentials first

## Troubleshooting

### Common Issues

1. **Import errors**: Ensure all dependencies are installed with `pip install -r requirements.txt`

2. **API errors**: Verify your API key and token URL in `ESSENTIAL_Values.py`

3. **CSV errors**: Check that your CSV file exists and has the correct column names

4. **Permission errors**: Ensure you have the necessary permissions in Verkada

### Getting Help

If you encounter issues:
1. Check the console output for immediate error messages
2. Review the log files in the `logs/` directory for detailed information
3. Verify your configuration in `ESSENTIAL_Values.py`
4. Test your API credentials manually
5. Ensure your CSV file format is correct

### Testing Logging

To test the logging system:
```bash
python test_logging.py
```

This will create sample log entries and verify the logging functionality is working correctly.

## Contributing

When contributing to this project:
1. Follow the existing code structure
2. Add appropriate error handling
3. Update documentation for new features
4. Test thoroughly before submitting changes

## License

This project is for internal use. Please ensure compliance with your organization's policies and Verkada's terms of service.

## Support

For support or questions about this project, please contact your system administrator or the development team. 