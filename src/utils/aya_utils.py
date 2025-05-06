from src.instruction_templates import multigec_prompts
from src.utils.multigec import LANG_CODE_TO_TOKEN, LANG_TO_CODE


def get_message_format(prompts):
  messages = []

  for p in prompts:
    messages.append(
        [{"role": "user", "content": p}]
      )

  return messages


def inference_formatting_prompts_func(example):
    language_code = LANG_TO_CODE[example["language"]]
    language_token = LANG_CODE_TO_TOKEN[language_code]

    user_input = example['feature']
    prompt_template = multigec_prompts[example["language"]].prompt_template
    instruction = prompt_template.format(original_text=user_input)

    text = f"<|START_OF_TURN_TOKEN|><|USER_TOKEN|>{language_token}{instruction}<|END_OF_TURN_TOKEN|><|START_OF_TURN_TOKEN|><|CHATBOT_TOKEN|>"

    return text


def training_formatting_prompts_func(example):
    language_code = LANG_TO_CODE[example["language"]]
    language_token = LANG_CODE_TO_TOKEN[language_code]

    user_input = example['feature']
    prompt_template = multigec_prompts[example["language"]].prompt_template
    instruction = prompt_template.format(original_text=user_input)
    target = example['target']

    text = f"<|START_OF_TURN_TOKEN|><|USER_TOKEN|>{language_token}{instruction}<|END_OF_TURN_TOKEN|><|START_OF_TURN_TOKEN|><|CHATBOT_TOKEN|>{target}"

    return text
