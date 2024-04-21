import subprocess

# 定义要执行的脚本列表
scripts = ['转成json.py','main.py', '增加合集.py','清空数据库.py','推送git.py']

# 依次执行每个脚本
for script in scripts:
    print(f"开始执行 {script}...")
    
    # 尝试执行当前脚本
    result = subprocess.run(['python', script], capture_output=True, text=True)
    
    # 如果脚本执行失败，则打印错误信息并退出
    if result.returncode != 0:
        print(f"{script} 执行失败！")
        print("错误信息：")
        print(result.stderr)
        break
    else:
        print(f"{script} 执行成功！")