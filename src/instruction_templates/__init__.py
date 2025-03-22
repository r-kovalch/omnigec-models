from src.instruction_templates.multigec import (
    CzechInstructionTemplate,
    EnglishInstructionTemplate,
    EstonianInstructionTemplate,
    GermanInstructionTemplate,
    GreekInstructionTemplate,
    ItalianInstructionTemplate,
    IcelandicInstructionTemplate,
    LatvianInstructionTemplate,
    SloveneInstructionTemplate,
    SwedishInstructionTemplate,
    UkrainianInstructionTemplate
)
from src.utils.base_prompt import BasePrompt


multigec_prompts: dict[str, BasePrompt] = {
    "czech":     CzechInstructionTemplate(),
    "english":   EnglishInstructionTemplate(),
    "estonian":  EstonianInstructionTemplate(),
    "german":    GermanInstructionTemplate(),
    "greek":     GreekInstructionTemplate(),
    "icelandic": IcelandicInstructionTemplate(),
    "italian":   ItalianInstructionTemplate(),
    "latvian":   LatvianInstructionTemplate(),
    "slovene":   SloveneInstructionTemplate(),
    "swedish":   SwedishInstructionTemplate(),
    "ukrainian": UkrainianInstructionTemplate(),
}
