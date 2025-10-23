# Quick Start Guide

Get your Dynamic Profile Endpoint running in under 2 minutes!

## Step 1: Navigate to Directory

```powershell
cd "C:\Program Files\MS\CORES\HNTASKT001"
```

## Step 2: Create Virtual Environment (First Time Only)

```powershell
python -m venv venv
```

## Step 3: Activate Virtual Environment

```powershell
# PowerShell
.\venv\Scripts\Activate.ps1

# Or CMD
.\venv\Scripts\activate.bat
```

## Step 4: Install Dependencies

```powershell
pip install -r requirements.txt
```

## Step 5: Configure Your Profile (Optional)

Create a `.env` file:

```env
USER_EMAIL=your.email@example.com
USER_NAME=Your Full Name
USER_STACK=Python/FastAPI
```

Or skip this step to use default values.

## Step 6: Run the Server

```powershell
# Option 1: Direct Python
python main.py

# Option 2: Using uvicorn
uvicorn main:app --reload

# Option 3: Using the run script
.\run.ps1
```

## Step 7: Test the API

### In Browser
Visit: http://localhost:8000/me

### Using PowerShell
```powershell
Invoke-RestMethod -Uri "http://localhost:8000/me" -Method Get
```

### Using the Test Script
```powershell
.\test-endpoint.ps1
```

### Interactive Docs
Visit: http://localhost:8000/docs

## That's It! 🎉

Your API is now running and returning profile data with dynamic cat facts!

## Expected Response

```json
{
  "status": "success",
  "user": {
    "email": "your.email@example.com",
    "name": "Your Full Name",
    "stack": "Python/FastAPI"
  },
  "timestamp": "2025-10-23T12:34:56.789Z",
  "fact": "A cat's purr vibrates at a frequency of 25 to 150 hertz."
}
```

## Troubleshooting

**Port already in use?**
```powershell
uvicorn main:app --reload --port 8001
```

**Import errors?**
```powershell
pip install -r requirements.txt --upgrade
```

**Can't activate venv?**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

