import os
import sys
import subprocess
from pathlib import Path

# 마야 스크립트 경로 가져오기 (Windows 기준)
maya_scripts_dir = Path.home() / "OneDrive"/ "문서" / "maya" / "2023" /"scripts"
site_packages_dir = maya_scripts_dir / "site-packages"
print(maya_scripts_dir)
# 1. 라이브러리 설치

subprocess.run([
    sys.executable,
    "-m", "pip", "install", "-r", "D:/gitclonetest/gp/requirements.txt",
    "--target", str(site_packages_dir)
])

source_dir = "D:/gitclonetest/gp/gpclean"
# 2. 툴 소스코드 복사
import shutil
shutil.copytree(source_dir, maya_scripts_dir / "gpclean", dirs_exist_ok=True)

# 3. userSetup.py 덮어쓰기
shutil.copy("D:/gitclonetest/gp/userSetup.py", maya_scripts_dir / "userSetup.py")

print("[+] 설치 완료! 마야를 실행하면 gpclean 이 자동 로드됩니다.")
