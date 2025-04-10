import os
import subprocess
from datetime import datetime

# 경로 설정
repo_path = "C:/Users/cross/Documents/kb_ir_repo"
log_path = os.path.join(repo_path, "log.txt")

def log(message):
    timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    with open(log_path, "a", encoding="utf-8") as log_file:
        log_file.write(f"{timestamp} {message}\n")
    print(f"{timestamp} {message}")

try:
    log("=== 자동 실행 시작 ===")

    # Git add
    subprocess.run(["git", "add", "."], cwd=repo_path, check=True)
    log("git add 완료")

    # Git commit
    commit_msg = f"자동 업데이트: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    subprocess.run(["git", "commit", "-m", commit_msg], cwd=repo_path, check=True)
    log(f"커밋 완료: {commit_msg}")

    # Git push
    subprocess.run(["git", "push"], cwd=repo_path, check=True)
    log("푸시 완료 → GitHub Pages 배포 성공")

except subprocess.CalledProcessError as e:
    log(f"❌ 오류 발생: {e}")

log("=== 자동 실행 종료 ===\n")
