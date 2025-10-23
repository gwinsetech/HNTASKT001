# PowerShell script to run the Dynamic Profile Endpoint

Write-Host "Starting Dynamic Profile Endpoint..." -ForegroundColor Cyan
Write-Host ""

# Check if virtual environment exists
if (-Not (Test-Path "venv")) {
    Write-Host "Virtual environment not found. Creating one..." -ForegroundColor Yellow
    python -m venv venv
    Write-Host "✓ Virtual environment created" -ForegroundColor Green
    Write-Host ""
}

# Use direct paths to avoid activation issues
$pythonExe = ".\venv\Scripts\python.exe"
$pipExe = ".\venv\Scripts\pip.exe"

# Check if requirements are installed
Write-Host "Installing/updating dependencies..." -ForegroundColor Yellow
& $pipExe install -r requirements.txt --quiet
Write-Host "✓ Dependencies ready" -ForegroundColor Green
Write-Host ""

# Check if .env exists
if (-Not (Test-Path ".env")) {
    Write-Host "WARNING: .env file not found!" -ForegroundColor Red
    Write-Host "Please create a .env file based on .env.example" -ForegroundColor Yellow
    Write-Host "Using default configuration for now..." -ForegroundColor Gray
    Write-Host ""
}

# Run the application
Write-Host "Starting FastAPI server..." -ForegroundColor Green
Write-Host "API will be available at: http://localhost:8000" -ForegroundColor Cyan
Write-Host "Interactive docs at: http://localhost:8000/docs" -ForegroundColor Cyan
Write-Host ""
Write-Host "Press Ctrl+C to stop the server" -ForegroundColor Gray
Write-Host ""

& $pythonExe main.py

