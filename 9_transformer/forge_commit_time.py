import subprocess
from datetime import datetime, timedelta

# Calculate the time 9 hours ago
time_9_hours_ago = (datetime.now() - timedelta(hours=9)).strftime("%a, %d %b %Y %H:%M:%S %z")

# Get the current commit hash
try:
    result = subprocess.run(["git", "log", "-1", "--pretty=%H"], capture_output=True, text=True, check=True)
    commit_hash = result.stdout.strip()
    print(f"Latest commit hash: {commit_hash}")
except subprocess.CalledProcessError as e:
    print(f"Error retrieving commit hash: {e}")
    exit(1)

# Amend the commit date
try:
    subprocess.run(
        ["git", "commit", "--amend", "--no-edit", "--date", time_9_hours_ago],
        env={**subprocess.os.environ, "GIT_COMMITTER_DATE": time_9_hours_ago},
        check=True,
    )
    print("Commit date amended successfully.")
except subprocess.CalledProcessError as e:
    print(f"Error amending commit date: {e}")
    exit(1)

# Force-push the changes (uncomment the following lines if needed)
# try:
#     subprocess.run(['git', 'push', '--force'], check=True)
#     print("Changes pushed successfully.")
# except subprocess.CalledProcessError as e:
#     print(f"Error pushing changes: {e}")
#     exit(1)
