@echo off
echo 测试恋爱机器人定时任务...
echo 当前时间：%date% %time%
echo.

cd /d "C:\Users\bo.wei\PycharmProjects\love"
echo 正在运行恋爱机器人脚本...
python love_robot.py

if %errorlevel% equ 0 (
    echo.
    echo ✅ 测试成功！脚本运行正常
    echo 消息应该已经发送到企业微信
) else (
    echo.
    echo ❌ 测试失败！请检查Python环境和网络连接
)

echo.
echo 按任意键退出...
pause >nul
