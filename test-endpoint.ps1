# PowerShell script to test the Dynamic Profile Endpoint API

Write-Host "===================================" -ForegroundColor Cyan
Write-Host "  Dynamic Profile Endpoint Tester  " -ForegroundColor Cyan
Write-Host "===================================" -ForegroundColor Cyan
Write-Host ""

$baseUrl = "http://localhost:8000"

# Test 1: Health Check
Write-Host "[1] Testing Health Check Endpoint..." -ForegroundColor Yellow
try {
    $response = Invoke-RestMethod -Uri "$baseUrl/health" -Method Get
    Write-Host "✓ Health Check Response:" -ForegroundColor Green
    $response | ConvertTo-Json -Depth 3
} catch {
    Write-Host "✗ Health check failed: $_" -ForegroundColor Red
}
Write-Host ""

# Test 2: Root Endpoint
Write-Host "[2] Testing Root Endpoint..." -ForegroundColor Yellow
try {
    $response = Invoke-RestMethod -Uri "$baseUrl/" -Method Get
    Write-Host "✓ Root Response:" -ForegroundColor Green
    $response | ConvertTo-Json -Depth 3
} catch {
    Write-Host "✗ Root endpoint failed: $_" -ForegroundColor Red
}
Write-Host ""

# Test 3: Profile Endpoint (Main Test)
Write-Host "[3] Testing Profile Endpoint (/me)..." -ForegroundColor Yellow
try {
    $response = Invoke-RestMethod -Uri "$baseUrl/me" -Method Get
    Write-Host "✓ Profile Response:" -ForegroundColor Green
    $response | ConvertTo-Json -Depth 3
    Write-Host ""
    
    # Validate response structure
    Write-Host "Validation:" -ForegroundColor Cyan
    
    if ($response.status -eq "success") {
        Write-Host "  ✓ Status field is 'success'" -ForegroundColor Green
    } else {
        Write-Host "  ✗ Status field is incorrect" -ForegroundColor Red
    }
    
    if ($response.user.email) {
        Write-Host "  ✓ User email present: $($response.user.email)" -ForegroundColor Green
    } else {
        Write-Host "  ✗ User email missing" -ForegroundColor Red
    }
    
    if ($response.user.name) {
        Write-Host "  ✓ User name present: $($response.user.name)" -ForegroundColor Green
    } else {
        Write-Host "  ✗ User name missing" -ForegroundColor Red
    }
    
    if ($response.user.stack) {
        Write-Host "  ✓ User stack present: $($response.user.stack)" -ForegroundColor Green
    } else {
        Write-Host "  ✗ User stack missing" -ForegroundColor Red
    }
    
    if ($response.timestamp) {
        Write-Host "  ✓ Timestamp present: $($response.timestamp)" -ForegroundColor Green
    } else {
        Write-Host "  ✗ Timestamp missing" -ForegroundColor Red
    }
    
    if ($response.fact) {
        Write-Host "  ✓ Cat fact present (${$response.fact.Length} chars)" -ForegroundColor Green
    } else {
        Write-Host "  ✗ Cat fact missing" -ForegroundColor Red
    }
    
} catch {
    Write-Host "✗ Profile endpoint failed: $_" -ForegroundColor Red
}
Write-Host ""

# Test 4: Multiple requests to verify dynamic data
Write-Host "[4] Testing Dynamic Behavior (3 requests)..." -ForegroundColor Yellow
Write-Host "Fetching timestamps and cat facts to verify they change..." -ForegroundColor Gray
Write-Host ""

for ($i = 1; $i -le 3; $i++) {
    try {
        $response = Invoke-RestMethod -Uri "$baseUrl/me" -Method Get
        Write-Host "Request $i" -ForegroundColor Cyan -NoNewline
        Write-Host " | Timestamp: $($response.timestamp)" -ForegroundColor White
        Write-Host "           | Fact: $($response.fact.Substring(0, [Math]::Min(60, $response.fact.Length)))..." -ForegroundColor White
        Start-Sleep -Seconds 1
    } catch {
        Write-Host "Request $i failed: $_" -ForegroundColor Red
    }
}

Write-Host ""
Write-Host "===================================" -ForegroundColor Cyan
Write-Host "  Testing Complete!                " -ForegroundColor Cyan
Write-Host "===================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "To view interactive docs, visit: http://localhost:8000/docs" -ForegroundColor Yellow

