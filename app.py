from flask import Flask, render_template, request
import os  # Pour récupérer le port fourni par la plateforme

app = Flask(__name__)

# Infos globales
NOM_CABINET = "EASYPAIE"
SLOGAN = "Gestion de paie simple et sécurisée"

# Tarifs
BASE_BASIC = 15000
PER_EMPLOYEE_BASIC = 15000
BASE_PREMIUM = 25000
PER_EMPLOYEE_PREMIUM = 25000

# Filtre pour formater en MGA
@app.template_filter('format_mga')
def format_mga(nombre):
    try:
        return f"{int(nombre):,}".replace(",", " ") + " Ar"
    except (ValueError, TypeError):
        return "- Ar"

@app.route("/", methods=["GET", "POST"])
def index():
    simulateur_result = None
    if request.method == "POST":
        try:
            offre = request.form.get("offre")
            nb_salaries = int(request.form.get("nb_salaries"))
            periode = int(request.form.get("periode"))

            if offre == "basique":
                total = (BASE_BASIC + PER_EMPLOYEE_BASIC * nb_salaries) * periode
            else:
                total = (BASE_PREMIUM + PER_EMPLOYEE_PREMIUM * nb_salaries) * periode
            simulateur_result = total
        except:
            simulateur_result = None

    return render_template("index.html",
                           cabinet=NOM_CABINET,
                           slogan=SLOGAN,
                           base_basic=BASE_BASIC,
                           per_employee_basic=PER_EMPLOYEE_BASIC,
                           base_premium=BASE_PREMIUM,
                           per_employee_premium=PER_EMPLOYEE_PREMIUM,
                           simulateur_result=simulateur_result
                           )

if __name__ == "__main__":
    # Pour le développement local seulement
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
