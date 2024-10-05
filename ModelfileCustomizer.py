# Import necessary modules
import subprocess
import os

# Define a class for customizing model files
class ModelfileCustomizor:
    # Initialize the class with a configuration dictionary
    def __init__(self, config):
        self.config = config  # Store the configuration dictionary as an instance variable

    # Create a model file based on the provided model name
    def create_model(self, model_name):
        """
        Creates a blank model file with given name.

        Args:
            model_name (str): The name of the model to create.

        Returns:
            None
        """
        model_file_path = f"./Modelfiles/{model_name}.Modelfile"
        if not os.path.exists(model_file_path):
            print(f"Error: Model file {model_file_path} does not exist.")
            return
        try:
            output = subprocess.check_output(f"ollama create {model_name} -f {model_file_path}", shell=True)
            print(output.decode('utf-8'))
        except subprocess.CalledProcessError as e:
            print(f"Error: {e}")

    # Confirm that a model has been created
    def confirm_model_creation(self, model_name):
        """
        Confirms that a model has been created.

        Args:
            model_name (str): The name of the model to confirm.

        Returns:
            None
        """
        try:
            output = subprocess.check_output(f"ollama show {model_name}", shell=True)
        except subprocess.CalledProcessError as e:
            print(f"Error: {e}")

    # Confirm that models are listed correctly
    #TODO - parameterize the modelnames to filter out properly
    def confirm_model_listing(self):
        """
        Confirms that models are listed correctly.

        Returns:
            None
        """
        try:
            output = subprocess.check_output("ollama list | grep 'apachehttp\|ciscofw\|ciscoace\|judge'", shell=True)
            print(output.decode('utf-8'))
        except subprocess.CalledProcessError as e:
            print(f"Error: {e}")

    # Create and confirm all models in the configuration
    def create_and_confirm_all_models(self):
        """
        Creates and confirms all models in the configuration.

        Returns:
            None
        """
        for model_name in self.config:
            self.create_model(model_name)
            self.confirm_model_creation(model_name)
        self.confirm_model_listing()