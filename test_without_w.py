from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Options pour Chrome en mode headless
options = webdriver.ChromeOptions()
options.add_argument("--headless")           # pas d'interface graphique
options.add_argument("--disable-gpu")        # utile sur Windows
options.add_argument("--no-sandbox")         # utile sur Linux
options.add_argument("--disable-dev-shm-usage")

# Lance Chrome en arrière-plan
driver = webdriver.Chrome(options=options)

# Ouvre la page du quiz
driver.get("https://boamadagascar.com/quiz-challenge/")

wait = WebDriverWait(driver, 40)

print(driver.page_source)

print("Remplissage du formulaire...")

# --- Étape 1 : basculer dans l'iframe ---
iframe = wait.until(EC.presence_of_element_located((By.TAG_NAME, "iframe")))
driver.switch_to.frame(iframe)

# --- Étape 2 : remplir les champs ---
nom_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//mat-label[contains(text(),'Nom')]/ancestor::mat-form-field//input")))
nom_input.send_keys("R.")

prenom_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//mat-label[contains(text(),'Prénom')]/ancestor::mat-form-field//input")))
prenom_input.send_keys("Francois")

tel_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//mat-label[contains(text(),'Téléphone')]/ancestor::mat-form-field//input")))
tel_input.send_keys("261346330608")

email_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//mat-label[contains(text(),'Email')]/ancestor::mat-form-field//input")))
email_input.send_keys("francoisnomena@gmail.com")

ville_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//mat-label[contains(text(),'Ville')]/ancestor::mat-form-field//input")))
ville_input.send_keys("Antananarivo")

continuer_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@form='dynamic-form']")))
continuer_btn.click()

print("Formulaire soumis.")

time.sleep(5)

quiz_data = {
    "Combien de joueurs formés en Afrique évoluent dans les championnats européens ?": "Plus de 1000",
    "Quelle est la dernière filiale installée de BOA?": "Congo",
    "Combien de téléspectateurs suivront la compétition ?": "Plus de 1 milliard",
    "Combien d'académies certifiées compte l'Afrique ?": "Plus de 350 académies",
    "Combien de stades homologués compte l'Afrique ?": "60 stades homologués",
    "Depuis quelle année BOA est présent en Afrique ?": "1982",
    "Bank of Africa est-elle un groupe bancaire :": "Panafricain",
    "Combien de filiales compte le Groupe BOA ?": "20",
    "Combien de pays des filiales BOA participent à la plus belle des compétitions africaines, édition 2025 ?": "8",
    "À combien s'élèvent les droits TV en Afrique ?": "1,25 Milliard"
}

for i in range(len(quiz_data)):
    question_elem = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//app-text-rich//div[contains(@class,'mat-headline-large')]"))
    )
    question_text = question_elem.text.strip()
    print("Question détectée:", question_text)

    if question_text in quiz_data:
        reponse_text = quiz_data[question_text]
        print("Réponse choisie:", reponse_text)

        reponse_elem = wait.until(EC.presence_of_element_located((By.XPATH, f"//div[contains(text(),\"{reponse_text}\")]")))
        driver.execute_script("arguments[0].scrollIntoView(true);", reponse_elem)
        driver.execute_script("arguments[0].click();", reponse_elem)
        print(f"Réponse '{reponse_text}' sélectionnée.")
        time.sleep(5)
    else:
        print("⚠️ Question non reconnue:", question_text)

print("Quiz terminé ✅")
driver.quit()
