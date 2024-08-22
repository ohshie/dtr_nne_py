from typing import TypeVar, Generic, Union

from openai import OpenAI
from zenrows import ZenRowsClient

from core.config import settings
from models.domainmodels.chatgptmodel import ChatGptModel
from models.domainmodels.deepl import Deepl
from models.domainmodels.zenrows import Zenrows
import deepl
import logging

T = TypeVar("T", bound=Union[Deepl, ChatGptModel, Zenrows])
logger = logging.getLogger(__name__)


async def check_service_key_validity(service: Generic[T], model: Generic[T]) -> bool:
    if not model or model is None:
        return False

    apiKey = getattr(service, "ApiKey", None)
    if apiKey is None:
        logger.error("Invalid class provided")
        return False

    if service is Zenrows:
        logger.info(f"Checking key of type: {Zenrows}")
        success = await check_zenrows_key_validity(model)
    elif service is Deepl:
        logger.info(f"Checking key of type: {Deepl}")
        success = await check_deepl_key_validity(model)
    elif service is ChatGptModel:
        logger.info(f"Checking key of type: {ChatGptModel}")
        success = await check_chatgpt_key_validity(model)
    else:
        logger.warning(f"Provided model: {model} is not considered external service")
        success = False

    logger.info(f"Service key is valid: {success}")
    return success


async def check_zenrows_key_validity(zenrows_model: Zenrows) -> bool:
    client = ZenRowsClient(zenrows_model.ApiKey)
    url = "https://httpbin.io/anything"

    response = await client.get_async(url)

    if response.status_code is not 200:
        logger.error("Provided Zenrows apikey is not valid")
        return False

    return True


async def check_deepl_key_validity(deepl_model: Deepl) -> bool:
    translator = deepl.Translator(deepl.AiohttpAdapter(deepl_model.ApiKey))

    try:
        result = await translator.translate(
            "Hello, World!", target_lang=deepl.TargetLang.Russian
        )
        test = result.lower()
        if test != "привет, мир!":
            return False

    except Exception as e:
        logger.error(f"Error occurred during checking deepl key: {str(e)}")
        return False

    return True


async def check_chatgpt_key_validity(chatgpt_model: ChatGptModel) -> bool:
    client = OpenAI(
        api_key=chatgpt_model.ApiKey,
        organization=settings.chatgpt_organization_key,
        project=settings.chatgpt_project_key,
    )

    stream = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": "Say this is a test"}],
        stream=True,
    )
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            return True
        else:
            return False
