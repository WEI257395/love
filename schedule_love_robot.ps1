# 恋爱机器人定时任务脚本
# 每天早上9点自动运行

# 设置执行策略（如果需要）
# Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# 创建定时任务
$action = New-ScheduledTaskAction -Execute "python.exe" -Argument "love_robot.py" -WorkingDirectory "C:\Users\bo.wei\PycharmProjects\love"
$trigger = New-ScheduledTaskTrigger -Daily -At "09:00"
$settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -StartWhenAvailable
$principal = New-ScheduledTaskPrincipal -UserId $env:USERNAME -LogonType InteractiveToken -RunLevel Highest

# 注册任务
Register-ScheduledTask -TaskName "恋爱机器人自动发送" -Action $action -Trigger $trigger -Settings $settings -Principal $principal -Description "每天早上9点自动发送温馨消息给女朋友"

Write-Host "任务已创建成功！每天早上9点会自动运行恋爱机器人脚本。"
Write-Host "你可以在任务计划程序中查看和管理这个任务。"

