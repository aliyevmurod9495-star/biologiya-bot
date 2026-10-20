$files = @(
    'F:\Antigravity A.I\biologiya_test_bot\questions.json',
    'F:\Antigravity A.I\biologiya_test_bot\materials.py',
    'F:\Antigravity A.I\biologiya_test_bot\materials_5.py',
    'F:\Antigravity A.I\biologiya_test_bot\materials_7.py',
    'F:\Antigravity A.I\biologiya_test_bot\materials_10.py',
    'F:\Antigravity A.I\biologiya_test_bot\materials_11.py',
    'F:\Antigravity A.I\biologiya_test_bot\images_5',
    'F:\Antigravity A.I\biologiya_test_bot\problems.py',
    'F:\Antigravity A.I\biologiya_test_bot\main.py',
    'F:\Antigravity A.I\biologiya_test_bot\database.py',
    'F:\Antigravity A.I\biologiya_test_bot\config.py',
    'F:\Antigravity A.I\biologiya_test_bot\requirements.txt',
    'F:\Antigravity A.I\biologiya_test_bot\Procfile'
)

Compress-Archive -Path $files -DestinationPath 'F:\Antigravity A.I\biologiya_test_bot\bot_update.zip' -Force

$z = Get-Item 'F:\Antigravity A.I\biologiya_test_bot\bot_update.zip'
Write-Host "Created bot_update.zip successfully! Size: $([Math]::Round($z.Length / 1KB, 2)) KB"
