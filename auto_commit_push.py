# auto_commit_push.py
import subprocess
import datetime

# 경로 설정 (사용자 로컬의 kb_ir_repo 폴더로 수정)
repo_path = "C:/Users/cross/Documents/kb_ir_repo"

# Git 명령어 실행 함수
def run_git_command(command, cwd):
    result = subprocess.run(command, cwd=cwd, shell=True, capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print(result.stderr)

# 현재 시간 기반 커밋 메시지
now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
commit_message = f"자동 업데이트: {now}"

# Git 커밋 & 푸시 순서
commands = [
    "git add sample_data_extended.json",
    f"git commit -m \"{commit_message}\"",
    "git push origin main"
]

# 실행
for cmd in commands:
    run_git_command(cmd, repo_path)