import schedule
import time
import subprocess

def lancer_quiz():
    # Exécute ton script Selenium (par exemple quiz.py)
    subprocess.run(["python", "test.py"])

# Planifie toutes les 1 minutes
schedule.every(1).minutes.do(lancer_quiz)

print("Le script sera lancé toutes les 1 minutes...")

while True:
    schedule.run_pending()
    time.sleep(1)
