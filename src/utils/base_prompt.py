from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel


class BasePrompt(BaseModel):
    template: str = """"""
    input_variables: list[str] = []

    @property
    def prompt_template(self):
        return PromptTemplate(
            template=self.template,
            input_variables=self.input_variables
        )
