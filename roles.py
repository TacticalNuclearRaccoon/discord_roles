import streamlit as st
import matplotlib.pyplot as plt

philanthrophe = 0
socialiseur = 0
esprit_libre = 0
disrupteur = 0
achiever = 0

st.title("Questionnaire sur les Rôles pour la Communauté des Vigies")

st.write("Choisissez une réponse de 1 à 5 pour chaque question: 1 = pas du tout, 5 = complètement")
st.header("Philanthrope")
p1 = st.slider("Cela me rend heureux si je peux aider les autres", 0, 7, 1)
p2 = st.slider("J'aime aider les autres à s'orienter dans de nouvelles situations.", 0, 7, 1)
p3 = st.slider("J'aime partager mes connaissances.", 0, 7, 1)
p4 = st.slider("Le bien-être des autres est important pour moi.", 0, 7, 1)

st.header("Socialiseur")
s1 = st.slider("Interagir avec les autres est important pour moi.", 0, 7, 1)
s2 = st.slider("J'aime faire partie d'une équipe.", 0, 7, 1)
s3 = st.slider("Il est important pour moi de me sentir membre d'une communauté.", 0, 7, 1)
s4 = st.slider("J'apprécie les activités de groupe.", 0, 7, 1)

st.header("Esprit Libre")
f1 = st.slider("Il est important pour moi de suivre mon propre chemin.", 0, 7, 1)
f2 = st.slider("Je suis souvent guidé par ma curiosité.", 0, 7, 1)
f3 = st.slider("J'aime essayer de nouvelles choses.", 0, 7, 1)
f4 = st.slider("Être indépendant est important pour moi.", 0, 7, 1)

st.header("Disrupteur")
d1 = st.slider("J'aime provoquer.", 0, 7, 1)
d2 = st.slider("J'aime remettre en question les choses.", 0, 7, 1)
d3 = st.slider("Je me considère comme un rebelle.", 0, 5, 1)
d4 = st.slider("Je n'aime pas suivre les règles.", 0, 7, 1)

st.header("Achiever")   
a1 = st.slider("J'aime surmonter les obstacles.", 0, 7, 1)
a2 = st.slider("Il est important pour moi de toujours accomplir mes tâches complètement.", 0, 7, 1)
a3 = st.slider("Il m'est difficile d'abandonner un problème avant d'avoir trouvé une solution.", 0, 7, 1)
a4 = st.slider("J'aime maîtriser les tâches difficiles.", 0, 7, 1)

philanthrophe = p1 + p2 + p3 + p4
socialiseur = s1 + s2 + s3 + s4
esprit_libre = f1 + f2 + f3 + f4
disrupteur = d1 + d2 + d3 + d4
achiever = a1 + a2 + a3 + a4

st.header("Résultats")
st.write(f"Votre score pour le philanthrope est de {philanthrophe}")
st.write(f"Votre score pour le socialiseur est de {socialiseur}")
st.write(f"Votre score pour l'esprit libre est de {esprit_libre}")
st.write(f"Votre score pour le disrupteur est de {disrupteur}")
st.write(f"Votre score pour l'achiever est de {achiever}")

results = {"philanthrophe":philanthrophe, "socialiseur":socialiseur, "esprit libre":esprit_libre, "disrupteur":disrupteur, "achiever":achiever}
sorted_results = sorted(results, key=results.get, reverse=False)

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




