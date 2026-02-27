<#
.PARAMETER tc
    Number of threads. Default = 3.

.PARAMETER browser
    Browser (chrome, firefox, edge, ie(only local)). Default = chrome.

.PARAMETER rrf
    Rerun only failed tests flag.

.PARAMETER local
    Flag for runnning tests locally.

.EXAMPLE
    .\start_tests.ps1 -tc 5 -browser firefox
    5 threads with Firefox by Selenium Grid.

.EXAMPLE
    .\start_tests.ps1 -browser ie -local
    local run with 3 threads(default) and Internet Explorer.
#>


param(
    [Parameter(Position=0)]
    [int]$tc = 3,
    [string]$browser = "chrome",
    [switch]$rrf,
    [switch]$local
)

$allowedBrowsers = @("chrome", "firefox", "edge", "ie")

if ($allowedBrowsers -notcontains $browser.ToLower()) {
    Write-Host "Error: '$browser' not in allowed list(chrome, firefox, edge, ie)." -ForegroundColor Red
    exit 1
}

if ($browser -eq "ie") {
    $local = $true
    $tc = 1
    Write-Host "Warning: Internet Explorer can only be run with the -local flag and one thread." -ForegroundColor Yellow
}

$pytestArgs = @(
    "-n", "$tc",
    "--browser=$browser"
)

if ($local) {
    Write-Host "Run locally" -ForegroundColor Green
    $pytestArgs += "--local"
} else {
    Write-Host "Run Grid" -ForegroundColor Green
    docker-compose up -d --scale ${browser}=$tc selenium-hub ${browser}
    if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: Failed to start Docker services for $browser." -ForegroundColor Red
    exit 1
    }
    Write-Host "Waiting for Grid to be ready..." -ForegroundColor Yellow
    Start-Sleep -Seconds 10
}

if ($rrf) {
    Write-Host "Rerunning failed tests ..." -ForegroundColor Yellow
    $pytestArgs += "--lf"
    $pytestArgs += "--lfnf=none"
}

uv run pytest @pytestArgs
$testExitCode = $LASTEXITCODE

if (-not $local) {
    Write-Host "Stopping Selenium Grid..." -ForegroundColor Yellow
    docker-compose down
}

exit $testExitCode
