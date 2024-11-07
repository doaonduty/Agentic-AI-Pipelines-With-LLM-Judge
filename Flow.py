# Import necessary modules and classes
from ModelfileGenerator import ModelfileGenerator
from ModelfileCustomizer import ModelfileCustomizer
from ModelfileConfig import config
from ModelInvoker import ModelInvoker
import os
import pprint
from log_config import logger

# Create a ModelfileGenerator instance with the provided configuration
generator = ModelfileGenerator(config)

# Get the absolute path of the current directory
current_dir = os.path.dirname(__file__)

# Generate and save model files
modelfiledetails = generator.save_model_file(os.path.join(current_dir, 'Modelfiles'))
logger.info(f"Model files generated: {modelfiledetails}")

# Create a ModelfileCustomizor instance with the provided configuration
model_customizor = ModelfileCustomizer(config)

# Create and confirm all models
model_customizor.create_and_confirm_all_models()

# Create a ModelInvoker instance with the provided configuration and run_judge flag
model_invoker = ModelInvoker(config, run_judge=True)

# Invoke each model with a generated prompt and run the judge model for evaluation
for model in modelfiledetails.keys():
    if model != "judge":
        model_invoker.invoke_model_with_generated_prompt(model, 2)

# Get the outputs of the models
outputs = model_invoker.get_outputs()

# Save the outputs to a file
with open(os.path.join(current_dir, 'flow_output.py'), 'w') as f:
    pprint.pprint("output=", stream=f, width=1500)
    pprint.pprint(outputs, stream=f, width=1500)

# Print the outputs of each model
for model_name, output in outputs.items():
    if model_name!= 'judge':
        logger.info(f"Model: {model_name}")
        logger.info(f"Ranking: {output[f'{model_name}_judge_rating']}")
        logger.info(f"Judge Evaluation: {output[f'{model_name}_judge_evaluation']}")
        logger.info("")