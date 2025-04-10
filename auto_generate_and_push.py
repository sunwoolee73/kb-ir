import os
import subprocess
from datetime import datetime

# 1. HTML 생성 (예시 - 이미 HTML 생성 완료 상태라면 이 줄 생략 가능)
# os.system("python generate_html.py")  # 필요 시 HTML 생성 스크립트 실행

# 2. Git add
subprocess.run(["git", "add", "."], cwd="C:/Users/cross/Documents/kb_ir_repo")

# 3. Git commit (현재 시간 포함)
commit_msg = f"자동 업데이트: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
subprocess.run(["git", "commit", "-m", commit_msg], cwd="C:/Users/cross/Documents/kb_ir_repo")

# 4. Git push
subprocess.run(["git", "push"], cwd="C:/Users/cross/Documents/kb_ir_repo")
