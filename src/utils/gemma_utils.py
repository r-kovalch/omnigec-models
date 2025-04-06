from src.instruction_templates import multigec_prompts
from src.utils.multigec import LANG_CODE_TO_TOKEN, LANG_TO_CODE


def formatting_prompts_func(example):
    language_code = LANG_TO_CODE[example["language"]]
    # Since special tokens for Gemma models does not have |, we remove them
    language_token = LANG_CODE_TO_TOKEN[language_code].replace("|", "")

    user_input = example['feature']
    prompt_template = multigec_prompts[example["language"]].prompt_template
    instruction = prompt_template.format(original_text=user_input)
    target = example['target']

    text = f"<start_of_turn>user\n{language_token}{instruction}<end_of_turn>\n<start_of_turn>model\n{target}<end_of_turn>\n"

    return text
