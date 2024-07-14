from langchain.llms import OpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate
)
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

import logging

logging.basicConfig(level=logging.INFO)

class InsuranceTemplate:
    """Classe para criar templates de prompts para o corretor de seguros."""
    
    def __init__(self):
        """Inicializa o template do sistema e do usuário."""
        self.system_template = """
        Você é um corretor de seguros especializado em seguros de vida no Brasil. 
        Seu principal objetivo é informar o usuário sobre as melhores opções de seguros de vida com base no perfil fornecido, incluindo idade, ocupação, condição de saúde, histórico médico familiar, estilo de vida, e hábitos (como tabagismo e prática de exercícios físicos).

        A solicitação do usuário será marcada por quatro hashtags (####). 

        Para cada solicitação, forneça pelo menos três planos de seguro de vida das principais seguradoras, incluindo:
        - A média de prêmio em caso de sinistro.
        - As coberturas e assistências incluídas.
        - A faixa de preço do seguro.
        - Seguradoras recomendadas.
    
        Exemplo de resposta:

        Planos de Seguro de Vida Recomendados:

        1. Seguro de Vida com Cobertura Ampliada para Doenças Graves:
        - Coberturas: Morte acidental e natural, cobertura adicional para doenças graves.
        - Média de prêmio R$: 100.000,00.
        - Faixa de preço R$: 100 a 300. 
        - Benefícios adicionais: Assistência de eco descarte, serviços domésticos como chaveiro e eletricista.
        - Seguradoras recomendadas: Capemisa, Bradesco, Itaú.

        2. [Nome do Plano]:
        - Coberturas: [Detalhes das coberturas].
        - Média de prêmio R$: [Valor do prêmio].
        - Faixa de preço R$: [Faixa de preço].
        - Benefícios adicionais: [Benefícios adicionais].
        - Seguradoras recomendadas: [Lista de seguradoras].

        3. [Nome do Plano]:
        - Coberturas: [Detalhes das coberturas].
        - Média de prêmio R$: [Valor do prêmio].
        - Faixa de preço R$: [Faixa de preço].
        - Benefícios adicionais: [Benefícios adicionais].
        - Seguradoras recomendadas: [Lista de seguradoras].
        """
        self.human_template = """
        ####{request}####
        """
        self.system_message_prompt = SystemMessagePromptTemplate.from_template(self.system_template)
        self.human_message_prompt = HumanMessagePromptTemplate.from_template(self.human_template, input_variables=["request"])
        self.chat_prompt = ChatPromptTemplate.from_messages([self.system_message_prompt, self.human_message_prompt])

class Agent:
    """Classe para interagir com o modelo de linguagem da OpenAI e obter sugestões de seguros de vida."""
    
    def __init__(self, open_ai_api_key, model='gpt-4-turbo', temperature=0, verbose=True):
        """Inicializa o agente com a chave da API, o modelo, a temperatura e o nível de verbosidade.
        
        Args:
            open_ai_api_key (str): Chave da API da OpenAI.
            model (str): Nome do modelo da OpenAI a ser utilizado.
            temperature (float): Temperatura do modelo para controle de aleatoriedade.
            verbose (bool): Define se o logging deve ser detalhado.
        """
        self.logger = logging.getLogger(__name__)
        if verbose:
            self.logger.setLevel(logging.INFO)
        
        self._openai_key = open_ai_api_key
        self.chat_model = ChatOpenAI(model=model, temperature=temperature, openai_api_key=self._openai_key)
        self.verbose = verbose
        
    def get_suggestion(self, request):
        """Obtém sugestões de seguros de vida com base na solicitação do usuário.
        
        Args:
            request (str): Solicitação do usuário com detalhes do perfil.
        
        Returns:
            dict: Sugestões de seguros de vida fornecidas pelo modelo.
        """
        insurance_template = InsuranceTemplate()
        
        insurance_advisor = LLMChain(
            llm=self.chat_model,
            prompt=insurance_template.chat_prompt,
            verbose=self.verbose,
            output_key='agent_suggestion'
        )

        return insurance_advisor({"request": request}, return_only_outputs=True)
