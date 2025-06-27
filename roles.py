import streamlit as st
import matplotlib.pyplot as plt

philanthrophe = 0
socialiseur = 0
esprit_libre = 0
disrupteur = 0
realisateur = 0

#descriptions des rôles
description_philanthrope1 = """Ils sont altruistes, aiment donner sans attendre de récompense, et valorisent le bien-être des autres.  

:sparkles: Motivés par le but, par le fait de partager, donner...  

:sparkles: Ils ont besoin de partager leurs connaissances et ont envie d’aider les autres."""  

description_philantrophe2 = """

- Exemples : Dans le Discord ce sont les personnes les plus susceptibles de devenir modérateur, elles sont là pour aider les personnes dans le besoin  

:arrow_forward: Auraient la charge du salon SOS.  

*Sous rôle :* Soutien"""

description_socialiseur1 = """" Ils recherchent l'interaction avec les autres et la création de liens sociaux.

:sparkles: Motivés par le lien, la connexion sociale…"""

description_socialiseur2 = """

- Exemples : Dans le Discord ce sont les personnes qui créent des évènements, réalisent des projets qui rassemble.

:arrow_forward: Pourraient avoir la charge de la partie rencontres et évènements.

*Sous rôle :* Porteur de voix / Ambassadeur"""

description_realisateur1 = """Ils cherchent à progresser, relever des défis, et maîtriser des tâches difficiles.

:sparkles: Motivés par la compétence…

:sparkles: Ils ont besoin de quêtes à accomplir et de défis."""

description_realisateur2= """ 

- Exemples : Ce sont les personnes qui sont plus discrètes mais qui montrent le bout de leur nez pour réaliser les défis et obtenir des récompenses comme des badges ou des niveaux.

:arrow_forward: Pourraient être en charge des défis.

*Sous rôle :* Moteur"""

description_esprit_libre1 = """Ils aiment explorer, créer, et agir sans contrainte externe.

:sparkles: Motivés par l’autonomie…

:sparkles: Ils ont besoin de personnalisation et de questionner."""

description_esprit_libre2 = """

- Exemples : Dans le Discord ce sont des vagabonds en recherche d’informations utiles pour eux, ce sont les premiers à poser des questions et ils aiment être challengés.

:arrow_forward: Pourraient être en charge de remonter des infos.

*Sous rôle :* Observateur
    """

description_disrupteur1 = """Ils cherchent à perturber le système, soit pour provoquer des changements positifs, soit pour tester ses limites.

:sparkles: Motivés par le changement...

:sparkles: Ils ont besoin de créer et d’échanger."""

description_disrupteur2 = """
    
- Exemples : Dans le Discord ce sont des personnes qui utilisent l’outil de questionnaires, qui ouvrent des débats et essaient de faire changer les états d’esprit

:arrow_forward: Pourraient être en charge de la newsletter collective, et de trouver des thématiques et sujets d’échanges.

*Sous rôle* : Contributeur"""

st.title("Questionnaire sur les Rôles pour la Communauté des Vigies")

st.write("Choisissez une réponse de 1 à 7 pour chaque question: 0 = pas du tout, 7 = complètement")
st.header("Philanthrope")
p1 = st.slider("Cela me rend heureux si je peux aider les autres", 0, 7, 0)
p2 = st.slider("J'aime aider les autres à s'orienter dans de nouvelles situations.", 0, 7, 0)
p3 = st.slider("J'aime partager mes connaissances.", 0, 7, 0)
p4 = st.slider("Le bien-être des autres est important pour moi.", 0, 7, 0)

st.header("Socialiseur")
s1 = st.slider("Interagir avec les autres est important pour moi.", 0, 7, 0)
s2 = st.slider("J'aime faire partie d'une équipe.", 0, 7, 0)
s3 = st.slider("Il est important pour moi de me sentir membre d'une communauté.", 0, 7, 0)
s4 = st.slider("J'apprécie les activités de groupe.", 0, 7, 0)

st.header("Esprit Libre")
f1 = st.slider("Il est important pour moi de suivre mon propre chemin.", 0, 7, 0)
f2 = st.slider("Je suis souvent guidé par ma curiosité.", 0, 7, 0)
f3 = st.slider("J'aime essayer de nouvelles choses.", 0, 7, 0)
f4 = st.slider("Être indépendant est important pour moi.", 0, 7, 0)

st.header("Disrupteur")
d1 = st.slider("J'aime provoquer.", 0, 7, 0)
d2 = st.slider("J'aime remettre en question les choses.", 0, 7, 0)
d3 = st.slider("Je me considère comme un rebelle.", 0, 7, 0)
d4 = st.slider("Je n'aime pas suivre les règles.", 0, 7, 0)

st.header("Réalisateur")   
a1 = st.slider("J'aime surmonter les obstacles.", 0, 7, 0)
a2 = st.slider("Il est important pour moi de toujours accomplir mes tâches complètement.", 0, 7, 0)
a3 = st.slider("Il m'est difficile d'abandonner un problème avant d'avoir trouvé une solution.", 0, 7, 0)
a4 = st.slider("J'aime maîtriser les tâches difficiles.", 0, 7, 0)

philanthrophe = p1 + p2 + p3 + p4
socialiseur = s1 + s2 + s3 + s4
esprit_libre = f1 + f2 + f3 + f4
disrupteur = d1 + d2 + d3 + d4
realisateur = a1 + a2 + a3 + a4

results = {"philanthrophe":philanthrophe, "socialiseur":socialiseur, "esprit libre":esprit_libre, "disrupteur":disrupteur, "réalisateur":realisateur}
sorted_results = sorted(results, key=results.get, reverse=False)
main_roles = [sorted_results[4], sorted_results[3], sorted_results[2]]

#termine = st.button("Terminer le questionnaire")
if "termine" not in st.session_state:
    st.session_state.termine = False
if st.button("Terminer le questionnaire"):
    st.session_state.termine = True
termine = st.session_state.termine
if termine:
    if sum(results.values()) == 0:
        st.error("Veuillez répondre à toutes les questions avant de soumettre.")
        show_everything = st.button("Afficher tous les rôles, je vais choisir moi-même")
        if show_everything:
            st.header("Voici tous les rôles disponibles")
            st.header("Philanthrope")
            st.markdown(description_philanthrope1, unsafe_allow_html=True)
            col1, col2 = st.columns([1,2])
            with col1:
                st.image('Philantropist.png', width=200)
            with col2:
                st.markdown(description_philantrophe2, unsafe_allow_html=True)
            st.header("Socialiseur")
            st.markdown(description_socialiseur1, unsafe_allow_html=True)
            col1, col2 = st.columns([1,2])
            with col1:
                st.image('Socializer.png', width=200)
            with col2:
                st.markdown(description_socialiseur2, unsafe_allow_html=True)
            st.header("Esprit Libre")
            st.markdown(description_esprit_libre1, unsafe_allow_html=True)
            col1, col2 = st.columns([1,2])
            with col1:
                st.image('Free spirit.png', width=200)
            with col2:
                st.markdown(description_esprit_libre2, unsafe_allow_html=True)
            st.header("Disrupteur")
            st.markdown(description_disrupteur1, unsafe_allow_html=True)
            col1, col2 = st.columns([1,2])
            with col1:
                st.image('Disruptor.png', width=200)
            with col2:
                st.markdown(description_disrupteur2, unsafe_allow_html=True)
            st.header("Réalisateur")
            st.markdown(description_realisateur1, unsafe_allow_html=True)
            col1, col2 = st.columns([1,2])
            with col1:
                st.image('Achiever.png', width=200)
            with col2:
                st.markdown(description_realisateur2, unsafe_allow_html=True)
    else:
        st.header("Résultats")
        st.write(f"Votre score pour le philanthrope est de {philanthrophe}")
        st.write(f"Votre score pour le socialiseur est de {socialiseur}")
        st.write(f"Votre score pour l'esprit libre est de {esprit_libre}")
        st.write(f"Votre score pour le disrupteur est de {disrupteur}")
        st.write(f"Votre score pour le réalisateur est de {realisateur}")

        fig, ax = plt.subplots()
        ax.bar(results.keys(), results.values(), color='aliceblue', edgecolor='darkblue')
        ax.set_ylabel('Score')
        ax.set_title('Scores par Rôle')
        plt.xticks(rotation=30)

        st.pyplot(fig)

        st.write(f"""Vos 3 rôles les plus forts sont :
                * {sorted_results[4]},
                * {sorted_results[3]},
                * et {sorted_results[2]}""")



        # display main roles
        if sorted_results[4] == "philanthrophe":
            st.header("Votre rôle principal est : Philanthrope")
            st.markdown(description_philanthrope1, unsafe_allow_html=True)
            col1, col2 = st.columns([1,2])
            with col1:
                st.image('Philantropist.png', width=200)
            with col2:
                st.markdown(description_philantrophe2, unsafe_allow_html=True)
        elif sorted_results[4] == "socialiseur":
            st.header("Votre rôle principal est : Socialiseur")
            st.markdown(description_socialiseur1, unsafe_allow_html=True)
            col1, col2 = st.columns([1,2])
            with col1:
                st.image('Philantropist.png', width=200)
            with col2:
                st.markdown(description_philanthrope1, unsafe_allow_html=True)
            st.markdown(description_philantrophe2, unsafe_allow_html=True)
        elif sorted_results[4] == "réalisateur":
            st.header("Votre rôle principal est : Réalisateur")
            st.markdown(description_realisateur1, unsafe_allow_html=True)
            col1, col2 = st.columns([1,2])
            with col1:
                st.image('Achiever.png', width=200)
            with col2:
                st.markdown(description_realisateur2, unsafe_allow_html=True)
            st.markdown(description_realisateur2, unsafe_allow_html=True)
        elif sorted_results[4] == "esprit libre":
            st.header("Votre rôle principal est : Esprit Libre")
            st.markdown(description_esprit_libre1, unsafe_allow_html=True)
            col1, col2 = st.columns([1,2])
            with col1:
                st.image('Free spirit.png', width=200)
            with col2:
                st.markdown(description_esprit_libre2, unsafe_allow_html=True)
        elif sorted_results[4] == "disrupteur":
            st.header("Votre rôle principal est : Disrupteur")
            st.markdown(description_disrupteur1,unsafe_allow_html=True)
            col1, col2 = st.columns([1,2])
            with col1:
                st.image('Disruptor.png', width=200)
            with col2:
                st.markdown(description_disrupteur2, unsafe_allow_html=True)

        #display secondary roles
        if sorted_results[3] == "philanthrophe":
            st.header("Votre second rôle est : Philanthrope")
            col1, col2 = st.columns([1,2])
            with col1:
                st.image('Philantropist.png', width=200)
            with col2:
                st.markdown(description_philanthrope1, unsafe_allow_html=True)
            st.markdown(description_philantrophe2, unsafe_allow_html=True)
        elif sorted_results[3] == "socialiseur":    
            st.header("Votre second rôle est : Socialiseur")
            st.markdown(description_socialiseur1, unsafe_allow_html=True)
            col1, col2 = st.columns([1,2])
            with col1:
                st.image('Socializer.png', width=200)
            with col2:
                st.markdown(description_socialiseur2, unsafe_allow_html=True)
        elif sorted_results[3] == "réalisateur":
            st.header("Votre second rôle est : Réalisateur")
            st.markdown(description_realisateur1, unsafe_allow_html=True)
            col1, col2 = st.columns([1,2])
            with col1:
                st.image('Achiever.png', width=200)
            with col2:
                st.markdown(description_realisateur2, unsafe_allow_html=True)
        elif sorted_results[3] == "esprit libre":
            st.header("Votre second rôle est : Esprit Libre")
            st.markdown(description_esprit_libre1, unsafe_allow_html=True)
            col1, col2 = st.columns([1,2])
            with col1:
                st.image('Free spirit.png', width=200)
            with col2:
                st.markdown(description_esprit_libre2, unsafe_allow_html=True)
        elif sorted_results[3] == "disrupteur":
            st.header("Votre second rôle est : Disrupteur")
            st.markdown(description_disrupteur1, unsafe_allow_html=True)
            col1, col2 = st.columns([1,2])
            with col1:
                st.image('Disruptor.png', width=200)
            with col2:
                st.markdown(description_disrupteur2, unsafe_allow_html=True)    

        #display ternary roles
        if sorted_results[2] == "philanthrophe":
            st.header("Votre troisième rôle est : Philanthrope")
            st.markdown(description_philanthrope1, unsafe_allow_html=True)
            col1, col2 = st.columns([1,2])
            with col1:
                st.image('Philantropist.png', width=200)
            with col2:
                st.markdown(description_philanthrope1, unsafe_allow_html=True)
            st.markdown(description_philantrophe2, unsafe_allow_html=True)
        elif sorted_results[2] == "socialiseur":
            st.header("Votre troisième rôle est : Socialiseur")
            st.markdown(description_socialiseur1, unsafe_allow_html=True)
            col1, col2 = st.columns([1,2])
            with col1:
                st.image('Socializer.png', width=200)
            with col2:
                st.markdown(description_socialiseur2, unsafe_allow_html=True)
        elif sorted_results[2] == "réalisateur":
            st.header("Votre troisième rôle est : Réalisateur")
            st.markdown(description_realisateur1, unsafe_allow_html=True)
            col1, col2 = st.columns([1,2])
            with col1:
                st.image('Achiever.png', width=200)
            with col2:
                st.markdown(description_realisateur2, unsafe_allow_html=True)
        elif sorted_results[2] == "esprit libre":
            st.header("Votre troisième rôle est : Esprit Libre")
            st.markdown(description_esprit_libre1, unsafe_allow_html=True)
            col1, col2 = st.columns([1,2])
            with col1:
                st.image('Free spirit.png', width=200)
            with col2:
                st.markdown(description_esprit_libre2, unsafe_allow_html=True)
        elif sorted_results[2] == "disrupteur":
            st.header("Votre troisième rôle est : Disrupteur")
            st.markdown(description_disrupteur1, unsafe_allow_html=True)
            col1, col2 = st.columns([1,2])
            with col1:
                st.image('Disruptor.png', width=200)
            with col2:
                st.markdown(description_disrupteur2, unsafe_allow_html=True)                        
        st.write("Merci d'avoir rempli le questionnaire !")

