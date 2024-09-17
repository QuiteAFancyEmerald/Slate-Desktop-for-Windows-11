$ConfigPath = (Resolve-Path './config/ChrisWinUtil.json').Path

# Invoke the remote script with the config parameter
Invoke-Expression "& { $(irm 'https://christitus.com/win') } -Config $ConfigPath -Run"
