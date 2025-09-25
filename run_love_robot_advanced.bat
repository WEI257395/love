@echo off
echo ========================================
echo 恋爱机器人自动发送脚本
echo 开始时间：%date% %time%
echo ========================================

cd /d "C:\Users\bo.wei\PycharmProjects\love"

echo 正在运行恋爱机器人脚本...
python love_robot.py

if %errorlevel% equ 0 (
    echo 脚本执行成功！
    echo 结束时间：%date% %time%
) else (
    echo 脚本执行失败，错误代码：%errorlevel%
    echo 结束时间：%date% %time%
)

echo ========================================
echo 按任意键退出...
pause >nul

