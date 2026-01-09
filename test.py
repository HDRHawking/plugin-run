from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Lance Chrome (assure-toi d'avoir installé le bon ChromeDriver)
driver = webdriver.Chrome() 

# Ouvre la page du quiz
driver.get("https://boamadagascar.com/quiz-challenge/")

wait = WebDriverWait(driver, 20)

print("Remplissage du formulaire...")

# --- Étape 1 : basculer dans l'iframe ---
iframe = wait.until(EC.presence_of_element_located((By.TAG_NAME, "iframe")))
driver.switch_to.frame(iframe)

# --- Étape 2 : remplir les champs ---
# Remplir "Nom"
nom_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//mat-label[contains(text(),'Nom')]/ancestor::mat-form-field//input")))
nom_input.send_keys("R.")

# Remplir "Prénom"
prenom_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//mat-label[contains(text(),'Prénom')]/ancestor::mat-form-field//input")))
prenom_input.send_keys("Francois")

print("Nom et prénom remplis.")

# Remplir "Téléphone"
tel_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//mat-label[contains(text(),'Téléphone')]/ancestor::mat-form-field//input")))
tel_input.send_keys("261346330608")

# Remplir "Email"
email_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//mat-label[contains(text(),'Email')]/ancestor::mat-form-field//input")))
email_input.send_keys("francoisnomena@gmail.com")
print("Téléphone et email remplis.")

# Remplir "Ville"
ville_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//mat-label[contains(text(),'Ville')]/ancestor::mat-form-field//input")))
ville_input.send_keys("Antananarivo")

print("Ville remplie.")

# Cliquer sur "Continuer"
continuer_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@form='dynamic-form']")))
continuer_btn.click()

print("Formulaire soumis.")

time.sleep(5) # garde la fenêtre ouverte 15 secondes driver.quit()

# Ton tableau de questions/réponses
quiz_data = {
    "Combien de joueurs formés en Afrique évoluent dans les championnats européens ?": "Plus de 1000", # mety ---
    "Quelle est la dernière filiale installée de BOA?": "Congo",  # mety
    "Combien de téléspectateurs suivront la compétition ?": "Plus de 1 milliard", # mety ---
    "Combien d'académies certifiées compte l'Afrique ?": "Plus de 350 académies", # mety ---
    "Combien de stades homologués compte l'Afrique ?": "60 stades homologués", # mety ---
    "Depuis quelle année BOA est présent en Afrique ?": "1982", # mety ---
    "Bank of Africa est-elle un groupe bancaire :": "Panafricain", # mety ---
    "Combien de filiales compte le Groupe BOA ?": "20", # mety ---
    "Combien de pays des filiales BOA participent à la plus belle des compétitions africaines, édition 2025 ?": "8",  # mety ---
    "À combien s'élèvent les droits TV en Afrique ?": "1,25 Milliard" # mety ---
}

# --- Boucle sur les questions ---
for i in range(len(quiz_data)):
    # Attendre que la question apparaisse
    question_elem = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//app-text-rich//div[contains(@class,'mat-headline-large')]"))
    )
    question_text = question_elem.text.strip()
    print("Question détectée:", question_text)

    # Trouver la bonne réponse dans le dictionnaire
    if question_text in quiz_data:
        reponse_text = quiz_data[question_text]
        print("Réponse choisie:", reponse_text)

        # Cliquer sur la réponse correspondante
        reponse_elem = wait.until( EC.presence_of_element_located((By.XPATH, f"//div[contains(text(),\"{reponse_text}\")]")) )
        driver.execute_script("arguments[0].scrollIntoView(true);", reponse_elem)
        driver.execute_script("arguments[0].click();", reponse_elem) 
        print(f"Réponse '{reponse_text}' sélectionnée.")
        time.sleep(5)  # Attendre un peu avant de passer à la question suivante
    else:
        print("⚠️ Question non reconnue:", question_text)

    # # Attendre le bouton "Continuer" ou "Suivant"
    # suivant_btn = wait.until(
    #     EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Continuer') or contains(.,'Suivant')]"))
    # )
    # suivant_btn.click()

print("Quiz terminé ✅")
time.sleep(1)
driver.quit()