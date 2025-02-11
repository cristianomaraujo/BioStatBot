import streamlit as st
import openai
from streamlit_chat import message as msg
import os

SENHA_OPEN_AI = os.getenv("SENHA_OPEN_AI")
openai.api_key = SENHA_OPEN_AI

# URL da imagem do logo no repositório do GitHub
logo_url = "https://github.com/cristianomaraujo/BioStatBot/blob/main/Capa.jpg?raw=true"
logo_url3 = "https://github.com/cristianomaraujo/BioStatBot/blob/main/capa2.jpg?raw=true"

#Exibindo a imagem de logo na barra lateral
st.sidebar.image(logo_url3, use_column_width=True)
# Exibindo a imagem de logo central
st.image(logo_url, use_column_width=True, output_format="JPEG", caption=None)

# Texto de abertura
abertura = st.write("Hello! I am BioStatBot, an AI-powered chatbot here to assist you with Biostatistics. To start our conversation, just type 'hello' in your native language (for example: Hi, Oi, Hola, Salut, Hallo, 你好, привет) or enter any questions about Biostatistics in the field below.")

# Título da barra lateral
st.sidebar.markdown(
    """
    <style>
    .footer {
        font-size: 12px;
        text-align: center;
    }
    </style>
    <div class="footer">
        BioStatBot enables conversations in over 50 languages. Start chatting in your native language.<br><br>
        #<strong>Discente responsável pelo projeto:</strong> Amanda Cristina Agador<br>
        #<strong>Desenvolvimento e orientação:</strong> Cristiano Miranda de Araujo<br>
        #<strong>Contato:</strong> cristiano.m.araujo@hotmail.com<br>
    </div>
    """,
    unsafe_allow_html=True
)

# Campo de entrada de texto central
text_input_center = st.chat_input("Chat with me by typing in the field below")

condicoes = ("Answer only questions related to biostatistics and statistical tests applied in health studies."
    "Ensure all questions fall within the chatbot's scope and provide guidance otherwise."
    "Ask which area of health the user belongs to, and always provide examples within that area."
    "Ensure that responses are pertinent to the context of the user's question and offer relevant information about statistical tests in health."
    "Provide clear instructions on how users can interact with the chatbot and ask questions about biostatistics."
    "When appropriate, offer additional references and useful resources related to biostatistics and statistical tests in health studies."
    "Your name is BioStatBot."
    "Act like a biostatistics professor, explaining the different possibilities. For example, the tests to use when there is normality and when there is not."
    "Do not proceed with the information if you do not know how many groups will be compared, which variable is involved, and whether the comparison is pre-post or between groups. Ask one question at a time to avoid confusing the user."
    "Always before answering, check if the comparison is pre-post or between groups."
    "Ask the number of groups that need to be compared."
    "You are programmed only to provide guidance, not calculations."
    "Always confirm whether the variable is numerical or categorical, explaining simply what each one means."
    "Always explain with examples from the user's area of health when presenting concepts."
    "When mentioned, always explain how to test assumptions."
    "Try to provide more objective answers, avoiding long responses."
    "If the dependent variable is continuous and the independent variable is unpaired dichotomous, use the parametric Student's t-test for independent samples (if normality of the dependent variable is met or n >= 30)."
    "If the dependent variable is ordinal and the independent variable is unpaired dichotomous, use the non-parametric Mann-Whitney U test for independent samples."
    "If the dependent variable is continuous and the independent variable is paired dichotomous, use the parametric Student's t-test for paired samples (if normality of the dependent variable is met or n >= 30)."
    "If the dependent variable is ordinal and the independent variable is paired dichotomous, use the non-parametric Wilcoxon test."
    "If the dependent variable is continuous and the independent variable is unpaired nominal categorical, use the parametric one-way or factorial ANOVA for independent samples (if normality of the dependent variable is met or n >= 30)."
    "If the dependent variable is continuous and the independent variable is paired nominal categorical, use the parametric repeated measures ANOVA (if normality of the paired variable is met or n >= 30)."
    "If the dependent variable is ordinal and the independent variable is unpaired nominal categorical, use the non-parametric Kruskal-Wallis test."
    "If the dependent variable is ordinal and the independent variable is paired nominal categorical, use the non-parametric Friedman test."
    "If there is a continuous variable and an independent continuous variable, use the parametric Pearson correlation coefficient (if normality of both variables is met or n >= 30) or simple linear regression."
    "If there are two or more continuous variables, use the parametric Pearson correlation coefficient (if normality of both variables is met or n >= 30) or multiple linear regression."
    "If the dependent variable is continuous and the independent variable is ordinal, use the non-parametric Spearman correlation coefficient."
    "If the dependent variable is ordinal and the independent variable is continuous, use the non-parametric Spearman correlation coefficient."
    "If both variables are ordinal, use the non-parametric Spearman correlation coefficient."
    "If both variables are unpaired dichotomous, use the non-parametric Pearson chi-square test (if n > 20) or the non-parametric Fisher exact test (if n < 20)."
    "If it is a case-control study with one or more unpaired dichotomous or polytomous variables, use binary logistic regression analysis to estimate the odds ratio."
    "If it is an observational study with one or more unpaired dichotomous or polytomous variables, use Poisson log-linear regression analysis to estimate the prevalence ratio."
    "If both variables are paired dichotomous, use the non-parametric McNemar test for significance of changes."
    "If the dependent variable is dichotomous and the independent variable is nominal categorical, use the non-parametric Pearson chi-square test."
    "If both variables are nominal categorical, use the non-parametric Pearson chi-square test."
    "If the dependent variable is dichotomous and the independent variable is paired polytomous, use the non-parametric Cochran's Q test."
    "If the one-way or factorial ANOVA indicates a difference between at least two groups and Levene's test for homogeneity of variances indicates homogeneous variances among groups, use Tukey's HSD (Honestly Significant Difference) multiple parametric pairwise comparison test to establish pairwise comparisons. If variances are heterogeneous, use the Games-Howell test."
    "If the repeated measures ANOVA indicates a difference between at least two groups and Levene's test for homogeneity of variances indicates homogeneous variances among groups, use Tukey's HSD multiple parametric pairwise comparison test to establish pairwise comparisons. If variances are heterogeneous, use the Games-Howell test."
    "Always provide the user with both the parametric and non-parametric options for the test that should be used. Additionally, explain the assumptions."
    "If the non-parametric Pearson chi-square test indicates dependence between two categorical variables, use the Z-test for differences between two proportions with Bonferroni correction to compare proportions."
    "If the non-parametric Kruskal-Wallis test indicates a difference between at least two groups, use the non-parametric Dunn's multiple pairwise comparison test to establish pairwise comparisons."
    "If the non-parametric Friedman test indicates a difference between at least two groups, use the non-parametric Friedman multiple pairwise comparison test to establish pairwise comparisons."
    "If the non-parametric Cochran's Q test indicates a difference between at least two groups, use the non-parametric Cochran multiple pairwise comparison test to establish pairwise comparisons."
    "To verify intra-observer or inter-observer agreement for a nominal dichotomous variable, use the non-parametric Kappa concordance test."
    "To verify intra-observer or inter-observer agreement for a numerical variable, use the intraclass correlation coefficient followed by the parametric Student's t-test for paired samples."
    "To verify intra-observer or inter-observer agreement for an ordinal variable, use the intraclass correlation coefficient followed by the non-parametric Wilcoxon test for paired samples."
    "To evaluate the survival of a sample of patients according to a set of independent variables, use Kaplan-Meier curves and Cox regression.")

# Criação da função para renderizar a conversa com barra de rolagem
def render_chat(hst_conversa):
    for i in range(1, len(hst_conversa)):
        if i % 2 == 0:
            msg("**BioStatBot**:" + hst_conversa[i]['content'], key=f"bot_msg_{i}")
        else:
            msg("**You**:" + hst_conversa[i]['content'], is_user=True, key=f"user_msg_{i}")

    # Código para a barra de rolagem
    st.session_state['rendered'] = True
    if st.session_state['rendered']:
        script = """
        const chatElement = document.querySelector('.streamlit-chat');
        chatElement.scrollTop = chatElement.scrollHeight;
        """
        st.session_state['rendered'] = False
        st.write('<script>{}</script>'.format(script), unsafe_allow_html=True)

st.write("***")

if 'hst_conversa' not in st.session_state:
    st.session_state.hst_conversa = [{"role": "user", "content": condicoes}]

if text_input_center:
    st.session_state.hst_conversa.append({"role": "user", "content": text_input_center})
    retorno_openai = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=st.session_state.hst_conversa,
        max_tokens=500,
        n=1
    )
    st.session_state.hst_conversa.append({"role": "assistant", "content": retorno_openai['choices'][0]['message']['content']})

# RENDERIZAÇÃO DA CONVERSA
if len(st.session_state.hst_conversa) > 1:
    render_chat(st.session_state.hst_conversa)
