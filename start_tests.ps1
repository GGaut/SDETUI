# Run script with -rrf flag to run failed tests only
param(
    [Parameter(Position=0)]
    # ThreadCount
    [int]$tc = 3,

    [Parameter(position=1)]
    #RerunFailed flag
    [switch]$rrf
)

$pytestArgs = @(
    "-n", "$tc",
    "--dist=loadfile"
)



docker-compose up -d --scale chrome=$tc

Write-Host "Waiting for Grid to be ready..." -ForegroundColor Yellow
Start-Sleep -Seconds 10

if ($rrf) {
    Write-Host "Rerunning failed tests ..." -ForegroundColor Yellow
    $pytestArgs += " --lfnf=none"
}

uv run pytest $pytestArgs
$testExitCode = $LASTEXITCODE

Write-Host "Stopping Selenium Grid..." -ForegroundColor Yellow
docker-compose down

exit $testExitCode
