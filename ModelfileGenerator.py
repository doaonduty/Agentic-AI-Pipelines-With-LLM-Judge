import os
from log_config import logger

class ModelfileGenerator:
    """
    A class for generating model files based on a provided configuration.
    """

    def __init__(self, config):
        """
        Initializes the ModelfileGenerator with a configuration dictionary.

        Args:
            config (dict): A dictionary containing model configurations.
        """
        self.config = config

    # Get the absolute path of the current directory
    current_dir = os.path.dirname(__file__)

    # Create the Modelfiles directory if it does not exist
    if not os.path.exists(os.path.join(current_dir, 'Modelfiles')):
        os.makedirs(os.path.join(current_dir, 'Modelfiles'))

    def generate_model_file(self, model_config):
        """
        Generates the contents of a model file based on the provided model configuration.

        Args:
            model_config (dict): A dictionary containing the model configuration.

        Returns:
            str: The contents of the model file.
        """
        model_file_contents = f"""
         FROM {model_config["model"]} \n PARAMETER temperature {model_config["temperature"]}\n PARAMETER num_ctx {model_config["num_ctx"]}\n SYSTEM """
        model_file_contents += f'"""{model_config["system_prompt"]}"""'
        model_file_contents += """ 
        """
        return model_file_contents.strip()

    def save_model_file(self, output_dir="./Modelfiles"):
        """
        Saves the generated model files to the specified output directory.

        Args:
            output_dir (str, optional): The directory to save the model files to. Defaults to "./Modelfiles".

        Returns:
            dict: A dictionary containing the model file names and their corresponding paths.
        """
        modelfiledetails = {}
        for model_name, model_config in self.config.items():
            model_file_name = f"{model_name}.Modelfile"
            model_file_path = f"{output_dir}/{model_file_name}"
            with open(model_file_path, "w") as f:
                f.write(self.generate_model_file(model_config))
            modelfiledetails[model_name] = model_file_path  
            logger.info(f"Model file saved to {model_file_path}")
        return modelfiledetails