import os
import subprocess
import tempfile
import shutil
# 配置您的GitHub用户名、仓库名、本地文件路径以及目标分支
GITHUB_USER = "GitHub用户名"
REPO_NAME = "仓库名"
LOCAL_FILE_PATH = "本地文件路径"
TARGET_BRANCH = "目标分支"
# 设置Git相关配置
os.environ["GIT_AUTHOR_EMAIL"] = "邮箱"
os.environ["GIT_AUTHOR_NAME"] = "GitHub用户名"
# 初始化临时目录并克隆仓库（使用SSH方式）
with tempfile.TemporaryDirectory() as TEMP_DIR:
    os.chdir(TEMP_DIR)
    subprocess.run(["git", "clone", "--depth=1", f"git@github.com:{GITHUB_USER}/{REPO_NAME}.git"])
    # 将本地文件复制到临时目录的仓库中
    shutil.copy(LOCAL_FILE_PATH, os.path.join(TEMP_DIR, REPO_NAME))
    # 进入仓库目录
    os.chdir(os.path.join(TEMP_DIR, REPO_NAME))
    # 添加文件、提交更改并推送至目标分支
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", "Update video.txt from local"])
    subprocess.run(["git", "push", "origin", TARGET_BRANCH])
print("File successfully pushed to GitHub repository.")
