import streamlit as st
from streamlit_option_menu import option_menu

# Vos données d'authentification
lesDonneesDesComptes = {
    'usernames': {
        'utilisateur': {
            'name': 'utilisateur',
            'password': 'utilisateurMDP',
            'email': 'utilisateur@gmail.com',
            'failed_login_attemps': 0,
            'logged_in': False,
            'role': 'utilisateur'
        },
        'root': {
            'name': 'root',
            'password': 'mdp',
            'email': 'admin@gmail.com',
            'failed_login_attemps': 0,
            'logged_in': False,
            'role': 'administrateur'
        }
    }
}

# Classe Authenticate
class Authenticate:
    def __init__(self, lesDonneesDesComptes, cookie_name, cookie_key, cookie_expiry_days):
        self.lesDonneesDesComptes = lesDonneesDesComptes
        self.cookie_name = cookie_name
        self.cookie_key = cookie_key
        self.cookie_expiry_days = cookie_expiry_days

    def login(self):
        if "username" in st.session_state and st.session_state["username"] in self.lesDonneesDesComptes['usernames']:
            user = self.lesDonneesDesComptes['usernames'][st.session_state["username"]]
            if user['password'] == st.session_state["password"]:
                st.session_state["logged_in"] = True
                return True
        return False

    def logout(self):
        st.session_state.clear()

# Instanciation de l'authenticator
authenticator = Authenticate(
    lesDonneesDesComptes,
    "cookie_name",
    "cookie_key",
    30
)

# Fonction pour les voyages déjà faits
def voyages_deja_faits():
    with st.container():
        st.title("Mes voyages")
        st.write("Voici les voyages que j'ai faits dans ma vie, pour l'instant ;) ")
        st.image("https://blog.likibu.com/fr/wp-content/uploads/2018/05/Rome_Italie_37045590.jpg", caption="Voyage à Rome", use_container_width=True)
        st.image("https://www.civitatis.com/blog/wp-content/uploads/2024/01/shutterstock_607235345-scaled.jpg", caption="Voyage à Londres", use_container_width=True)
        st.image("https://media.tacdn.com/media/attractions-splice-spp-674x446/0a/66/c8/04.jpg", caption="Voyage à Séville", use_container_width=True)
        st.image("https://images.prismic.io/siestacampers/c726188f-6b84-4cc8-9c82-89d1b11989f3_malaga-beach-malagueta.jpg?auto=compress,format", caption="Voyage à Malaga", use_container_width=True)
        st.image("https://barcelonesite.fr/images/barcelona_2.jpg", caption="Voyage à Barcelone", use_container_width=True)
        st.image("https://cdn.britannica.com/89/140989-050-C58C985F/Lighthouse-Jersey-Channel-Islands.jpg", caption="Week end à Jersey", use_container_width=True)

# Fonction pour les voyages à faire
def voyages_a_faire():
    with st.container():
        st.title("Les voyages à faire")
        st.write("Voici les voyages que j'aimerais faire prochainement :")
        st.image("https://www.agoda.com/wp-content/uploads/2024/04/Featured-image-Scenic-Prague-panorama-with-Hradcany-castle-and-Vltava-river-in-spring-Czech-Republic-1244x700.jpg", caption="Voyage à Prague", use_container_width=True)
        st.image("https://cdn-imgix.headout.com/media/images/1300daf8e72cbe5623b8a4d84a398f1f-Duomo%20Florence%20golden%20hour.jpg?auto=format&w=900&h=562.5&q=90&fit=crop&ar=16%3A10", caption="Voyage à Florence", use_container_width=True)
        st.image("https://media.routard.com/image/78/7/edimbourg.1475787.w430.jpg", caption="Voyage à Edimbourg", use_container_width=True)
        st.image("https://etourisme.blog/wp-content/uploads/2023/02/islande-aurores-boreales.jpg", caption="Voyage en Islande", use_container_width=True)
        st.image("https://visiterathenes.fr/images/athenes.jpg", caption="Voyage à Athènes", use_container_width=True)


# Vérification de la connexion
def check_login():
    if authenticator.login():
        st.write("Connexion réussie !")
        
        # Créer deux onglets distincts
        tab1, tab2 = st.tabs(["Voyages à faire", "Voyages déjà faits"])

        with tab1:
            voyages_a_faire()

        with tab2:
            voyages_deja_faits()

    else:
        st.title("Connexion")
        st.write("Veuillez vous connecter pour accéder à l'application.")

        # Formulaire de connexion
        with st.form(key='login_form'):
            username = st.text_input("Nom d'utilisateur")
            password = st.text_input("Mot de passe", type='password')
            submit_button = st.form_submit_button(label="Se connecter")

            if submit_button:
                st.session_state["username"] = username
                st.session_state["password"] = password

                if authenticator.login():
                    st.session_state["logged_in"] = True
                    st.success("Connexion réussie !")
                    check_login()
                else:
                    st.error("Identifiants incorrects. Veuillez réessayer.")

# Appel de la fonction de vérification de la connexion
check_login()





